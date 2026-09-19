from collections.abc import Sequence
from typing import Any

import numpy as np
import pandas as pd


DynFleetSchema = {
    "time": {
        "key": "t",
        "dims": ("year",),
    },
    "technology": {
        "key": "T",
        "dims": ("technology",),
    },
    "inflow": {
        "key": "I_Veh_cT",
        "dims": ("cohort", "technology"),
    },
    "stock": {
        "key": "S_Veh_tcT",
        "dims": ("year", "cohort", "technology"),
    },
    "outflow": {
        "key": "O_Veh_tcT",
        "dims": ("year", "cohort", "technology"),
    },
    "specific_use": {
        "key": "km_t",
        "dims": ("year",),
    },
    "fleet_use": {
        "key": "KM_tcT",
        "dims": ("year", "cohort", "technology"),
    },
    "specific_consumption": {
        "key": "mj_cT",
        "dims": ("cohort", "technology"),
    },
    "fleet_consumption": {
        "key": "E_tcT",
        "dims": ("year", "cohort", "technology"),
    },
}


class FunctionalMetabolism:
    """
    Bridge a dynamic MFA dataset to LCA function profiles.

    The dynamic MFA stock is decomposed into homogeneous populations
    identified by (inflow_year, outflow_year[, technology]). Each
    population consists of objects that enter together and leave together.

    ``function_profile()`` requests functional use at one or more points
    in time. ``lifetime_profile()`` selects populations and returns their
    complete lifetime use.

    Optional LCA flows can be added to either profile:

        use
        ├── consumption
        ├── production
        └── disposal

    The schema maps conceptual quantities to arrays in the MFA dataset
    and permits arbitrary dimension ordering.
    """

    DEFAULT_SCHEMA = {
        "time": {
            "key": "time",
            "dims": ("year",),
        },
        "inflow": {
            "key": "inflow",
            "dims": ("year",),
        },
        "stock": {
            "key": "stock",
            "dims": ("year", "cohort"),
        },
        "outflow": {
            "key": "outflow",
            "dims": ("year", "cohort"),
        },
        "specific_use": {
            "key": "specific_use",
            "dims": ("year",),
        },
    }

    REQUIRED_CONCEPTS = (
        "time",
        "inflow",
        "stock",
        "outflow",
        "specific_use",
    )

    def __init__(
        self,
        data: dict[str, np.ndarray],
        schema: dict[str, dict[str, Any]] | None = None,
    ):
        self.data = data

        self.schema = {
            concept: {
                **self.DEFAULT_SCHEMA.get(concept, {}),
                **spec,
            }
            for concept, spec in (schema or {}).items()
        }

        for concept, spec in self.DEFAULT_SCHEMA.items():
            self.schema.setdefault(concept, spec.copy())

        self._validate_schema()

        self.years = list(self.get("time"))
        self._year_index = {
            year: i for i, year in enumerate(self.years)
        }

        if len(self._year_index) != len(self.years):
            raise ValueError(
                "The time axis contains duplicate years."
            )

        self.technologies = self._get_technologies()

        self._build_lifetime_expansion()

    # ------------------------------------------------------------------
    # Dataset access
    # ------------------------------------------------------------------

    def has(self, concept: str) -> bool:
        """Return True when a concept is defined and present."""
        return (
            concept in self.schema
            and self.schema[concept].get("key") in self.data
        )

    def get(self, concept: str) -> np.ndarray:
        """Return the array associated with a conceptual quantity."""
        if not self.has(concept):
            raise KeyError(
                f"Concept '{concept}' is not available."
            )

        return self.data[self.schema[concept]["key"]]

    def dims(self, concept: str) -> tuple[str, ...]:
        """Return the declared dimensions of a concept."""
        return tuple(self.schema[concept]["dims"])

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def _validate_schema(self) -> None:
        for concept in self.REQUIRED_CONCEPTS:
            if concept not in self.schema:
                raise ValueError(
                    f"Required concept '{concept}' has no schema entry."
                )

            key = self.schema[concept].get("key")

            if key not in self.data:
                raise KeyError(
                    f"Concept '{concept}' maps to '{key}', "
                    "but that key is not present in the data."
                )

        for concept, spec in self.schema.items():
            key = spec.get("key")

            # Optional concepts may legitimately be absent.
            if key not in self.data:
                continue

            dims = tuple(spec["dims"])
            array = self.data[key]

            if len(dims) != array.ndim:
                raise ValueError(
                    f"Concept '{concept}' declares dimensions {dims}, "
                    f"but '{key}' has shape {array.shape}."
                )

            if len(dims) != len(set(dims)):
                raise ValueError(
                    f"Concept '{concept}' contains duplicate dimensions: "
                    f"{dims}."
                )

        if "technology" in self.schema:
            self._validate_technology_dimension()

    def _validate_technology_dimension(self) -> None:
        technologies = self._get_technologies()

        if len(technologies) != len(set(technologies)):
            raise ValueError(
                "Technology labels must be unique."
            )

        for concept, spec in self.schema.items():
            if concept == "technology" or not self.has(concept):
                continue

            dims = self.dims(concept)

            if "technology" not in dims:
                continue

            axis = dims.index("technology")
            n_technologies = self.get(concept).shape[axis]

            if n_technologies != len(technologies):
                raise ValueError(
                    f"Concept '{concept}' has {n_technologies} entries "
                    f"on its technology axis, but {len(technologies)} "
                    "technologies are configured."
                )

    def _get_technologies(self) -> list[Any]:
        if "technology" not in self.schema:
            return None

        key = self.schema["technology"].get("key")

        if key not in self.data:
            raise KeyError(
                f"Technology concept maps to '{key}', "
                "but that key is not present in the data."
            )

        return list(self.data[key])

    # ------------------------------------------------------------------
    # Dimension resolution
    # ------------------------------------------------------------------

    def _index(
        self,
        dimension: str,
        value: Any,
    ) -> int:
        if dimension in {"year", "cohort", "lifetime"}:
            try:
                return self._year_index[value]
            except KeyError:
                raise ValueError(
                    f"{value!r} is not present in the time axis."
                ) from None

        if dimension == "technology":
            if self.technologies is None:
                raise ValueError(
                    "The dataset has no technology dimension."
                )

            try:
                return self.technologies.index(value)
            except ValueError:
                raise ValueError(
                    f"Technology {value!r} is not recognised. "
                    f"Available technologies: {self.technologies}"
                ) from None

        raise ValueError(
            f"Unknown dimension '{dimension}'."
        )

    def _resolve(
        self,
        concept: str,
        **fixed: Any,
    ) -> tuple[np.ndarray, list[str]]:
        """
        Fix selected dimensions and return:

            resolved_array, remaining_dimensions

        The schema determines the mapping between conceptual dimensions
        and physical array axes.
        """
        array = self.get(concept)
        dimensions = list(self.dims(concept))

        for dimension, value in fixed.items():
            if value is None or dimension not in dimensions:
                continue

            axis = dimensions.index(dimension)

            array = np.take(
                array,
                self._index(dimension, value),
                axis=axis,
            )

            dimensions.pop(axis)

        return array, dimensions

    def _scalar(
        self,
        concept: str,
        **fixed: Any,
    ) -> float:
        """Resolve a concept to a scalar."""
        array, remaining = self._resolve(
            concept,
            **fixed,
        )

        if remaining:
            raise ValueError(
                f"Concept '{concept}' still has unresolved dimensions "
                f"{remaining}."
            )

        return float(array)

    def _year_series(
        self,
        concept: str,
        *,
        inflow_year: int | None = None,
        technology: Any = None,
    ) -> np.ndarray:
        """
        Resolve a concept to a series over the full time axis.

        If the concept does not vary over year, its value is broadcast.
        """
        array, remaining = self._resolve(
            concept,
            cohort=inflow_year,
            technology=technology,
        )

        if remaining == ["year"]:
            return np.asarray(array)

        if not remaining:
            return np.full(
                len(self.years),
                float(array),
            )

        raise ValueError(
            f"Concept '{concept}' cannot be reduced to a year series; "
            f"remaining dimensions: {remaining}."
        )

    # ------------------------------------------------------------------
    # Lifetime decomposition
    # ------------------------------------------------------------------

    def _build_lifetime_expansion(self) -> None:
        """
        Decompose cohorts by outflow year.

        Creates:

            inflow_by_lifetime
                cohort × lifetime [× technology]

            stock_by_lifetime
                year × cohort × lifetime [× technology]

        A subgroup is therefore a homogeneous population with one
        inflow year and one outflow year.
        """
        if (
            self.has("inflow_by_lifetime")
            and self.has("stock_by_lifetime")
        ):
            return

        n = len(self.years)
        indices = np.arange(n)

        # year × cohort × lifetime
        alive = (
            (indices[:, None, None] >= indices[None, :, None])
            & (indices[:, None, None] < indices[None, None, :])
        )

        outflow_dims = self.dims("outflow")
        outflow = self.get("outflow")

        if "technology" in outflow_dims:
            outflow = np.moveaxis(
                outflow,
                [
                    outflow_dims.index("year"),
                    outflow_dims.index("cohort"),
                    outflow_dims.index("technology"),
                ],
                [0, 1, 2],
            )
            # year × cohort × technology

            inflow_by_lifetime = np.moveaxis(
                outflow,
                0,
                1,
            )
            # cohort × lifetime × technology

            stock_by_lifetime = (
                alive[..., None]
                * inflow_by_lifetime[None, ...]
            )

            self.data["_inflow_by_lifetime"] = (
                inflow_by_lifetime
            )
            self.data["_stock_by_lifetime"] = (
                stock_by_lifetime
            )

            self.schema["inflow_by_lifetime"] = {
                "key": "_inflow_by_lifetime",
                "dims": (
                    "cohort",
                    "lifetime",
                    "technology",
                ),
            }

            self.schema["stock_by_lifetime"] = {
                "key": "_stock_by_lifetime",
                "dims": (
                    "year",
                    "cohort",
                    "lifetime",
                    "technology",
                ),
            }

        else:
            outflow = np.moveaxis(
                outflow,
                [
                    outflow_dims.index("year"),
                    outflow_dims.index("cohort"),
                ],
                [0, 1],
            )
            # year × cohort

            inflow_by_lifetime = outflow.T
            # cohort × lifetime

            stock_by_lifetime = (
                alive
                * inflow_by_lifetime[None, ...]
            )

            self.data["_inflow_by_lifetime"] = (
                inflow_by_lifetime
            )
            self.data["_stock_by_lifetime"] = (
                stock_by_lifetime
            )

            self.schema["inflow_by_lifetime"] = {
                "key": "_inflow_by_lifetime",
                "dims": (
                    "cohort",
                    "lifetime",
                ),
            }

            self.schema["stock_by_lifetime"] = {
                "key": "_stock_by_lifetime",
                "dims": (
                    "year",
                    "cohort",
                    "lifetime",
                ),
            }

    # ------------------------------------------------------------------
    # Population handling
    # ------------------------------------------------------------------

    def _population_sizes(
        self,
        *,
        inflow_years: list[int] | None = None,
        outflow_years: list[int] | None = None,
        technologies: list[Any] | None = None,
    ) -> dict[tuple[int, int, Any], float]:
        """
        Return selected homogeneous dMFA populations and their sizes.

        Keys are:

            (inflow_year, outflow_year, technology)

        For datasets without a technology dimension, technology is None.

        Population size is taken directly from ``inflow_by_lifetime``.
        """
        if technologies is None:
            technologies = [None]

        inflow_filter = (
            set(inflow_years)
            if inflow_years is not None
            else None
        )
        outflow_filter = (
            set(outflow_years)
            if outflow_years is not None
            else None
        )

        result = {}

        for technology in technologies:
            array, dimensions = self._resolve(
                "inflow_by_lifetime",
                technology=technology,
            )

            cohort_axis = dimensions.index("cohort")
            lifetime_axis = dimensions.index("lifetime")

            array = np.moveaxis(
                array,
                [cohort_axis, lifetime_axis],
                [0, 1],
            )

            cohort_idx, lifetime_idx = np.nonzero(array)

            for cohort, lifetime in zip(
                cohort_idx,
                lifetime_idx,
            ):
                inflow = self.years[cohort]
                outflow = self.years[lifetime]

                if (
                    inflow_filter is not None
                    and inflow not in inflow_filter
                ):
                    continue

                if (
                    outflow_filter is not None
                    and outflow not in outflow_filter
                ):
                    continue

                result[
                    (inflow, outflow, technology)
                ] = float(array[cohort, lifetime])

        return result

    def _active_population_sizes(
        self,
        use_year: int,
        population_sizes: dict[tuple[int, int, Any], float],
    ) -> dict[tuple[int, int, Any], float]:
        """
        Return the stock of the selected populations active in use_year.

        ``population_sizes`` supplies the already-selected complete
        dMFA populations; this method only applies the additional
        temporal stock condition.
        """
        active = {}

        for population in population_sizes:
            inflow, outflow, technology = population

            stock = self._stock_value(
                use_year=use_year,
                inflow_year=inflow,
                outflow_year=outflow,
                technology=technology,
            )

            if stock != 0:
                active[population] = stock

        return active

    def _stock_value(
        self,
        *,
        use_year: int,
        inflow_year: int,
        outflow_year: int,
        technology: Any = None,
    ) -> float:
        """Return stock in one homogeneous population."""
        return self._scalar(
            "stock_by_lifetime",
            year=use_year,
            cohort=inflow_year,
            lifetime=outflow_year,
            technology=technology,
        )
    
    def _full_lifetime_use(
        self,
        *,
        inflow_year: int,
        outflow_year: int,
        technology: Any = None,
    ) -> float:
        """
        Return the total use delivered by one object over its complete
        lifetime.
        """
        use = self._year_series(
            "specific_use",
            inflow_year=inflow_year,
            technology=technology,
        )

        start = self._year_index[inflow_year]
        end = self._year_index[outflow_year]

        if end <= start:
            raise ValueError(
                f"Outflow year {outflow_year} must follow "
                f"inflow year {inflow_year}."
            )

        return float(use[start:end].sum())
    
    # ------------------------------------------------------------------
    # Scaling
    # ------------------------------------------------------------------

    def _scale(
        self,
        df: pd.DataFrame,
        use_years: list[int],
        scale_to: float | Sequence[float] | None,
        scale_by: str,
        population_sizes: dict[tuple[int, int, Any], float] | None = None,
    ) -> pd.DataFrame:
        """
        Scale a use profile.

        ``scale_by="use"``
            Scale functional demand.

        ``scale_by="objects"``
            Scale the selected dMFA population sizes.
        """
        if scale_to is None:
            return df

        if scale_by not in {"use", "objects"}:
            raise ValueError(
                "scale_by must be either 'use' or 'objects'."
            )

        if scale_by == "objects":
            if isinstance(
                scale_to,
                (list, tuple, np.ndarray),
            ):
                raise ValueError(
                    "scale_to must be a scalar when "
                    "scale_by='objects'."
                )

            if population_sizes is None:
                raise ValueError(
                    "Population sizes are required when "
                    "scale_by='objects'."
                )

            current = sum(
                population_sizes.values()
            )

            if current == 0:
                raise ValueError(
                    "Cannot scale a profile representing zero objects."
                )

            df["value"] *= scale_to / current
            return df

        if isinstance(
            scale_to,
            (list, tuple, np.ndarray),
        ):
            targets = list(scale_to)

            if len(targets) != len(use_years):
                raise ValueError(
                    "A sequence supplied to scale_to must have "
                    "the same length as use_year."
                )

            for year, target in zip(
                use_years,
                targets,
            ):
                mask = df["year"] == year
                current = df.loc[mask, "value"].sum()

                if current == 0:
                    raise ValueError(
                        f"Cannot scale use_year {year}: "
                        "its demand is zero."
                    )

                df.loc[mask, "value"] *= (
                    target / current
                )

            return df

        current = df["value"].sum()

        if current == 0:
            raise ValueError(
                "Cannot scale a profile with zero total use."
            )

        df["value"] *= scale_to / current

        return df

    # ------------------------------------------------------------------
    # LCA flow construction
    # ------------------------------------------------------------------

    def _add_direct_consumption(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Add direct consumption associated with use.

        Consumption is calculated as:

            use × specific_consumption

        Only rows with ``flow == "use"`` are considered.
        """
        if not self.has("specific_consumption"):
            raise ValueError(
                "include_direct_consumption=True requires "
                "'specific_consumption' in the schema."
            )

        rows = []

        for row in df.loc[
            df["flow"] == "use"
        ].itertuples(index=False):
            technology = (
                row.technology
                if self.technologies is not None
                else None
            )

            consumption_per_use = self._scalar(
                "specific_consumption",
                year=row.year,
                cohort=row.inflow_year,
                technology=technology,
            )

            result = {
                "year": row.year,
                "inflow_year": row.inflow_year,
                "outflow_year": row.outflow_year,
                "flow": "consumption",
                "value": (
                    row.value * consumption_per_use
                ),
            }

            if self.technologies is not None:
                result["technology"] = technology

            rows.append(result)

        if not rows:
            return df

        return pd.concat(
            [
                df,
                pd.DataFrame(
                    rows,
                    columns=df.columns,
                ),
            ],
            ignore_index=True,
        )

    def _add_production_eol_from_profile(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Add production and disposal flows implied by a function profile.

        Only use rows are considered. For each population represented in
        the profile, the number of objects is inferred as:

            requested use
            ---------------------
            complete-lifetime use

        This preserves the original function_profile() semantics: only
        populations contributing to the requested use profile generate
        production and disposal flows.
        """
        group_columns = [
            "inflow_year",
            "outflow_year",
        ]

        if self.technologies is not None:
            group_columns.append("technology")

        use_df = df.loc[
            df["flow"] == "use"
        ]

        rows = []

        for keys, group in use_df.groupby(
            group_columns,
            sort=False,
        ):
            if self.technologies is None:
                inflow, outflow = keys
                technology = None
            else:
                inflow, outflow, technology = keys

            requested_use = group["value"].sum()

            if requested_use == 0:
                continue

            lifetime_use = self._full_lifetime_use(
                inflow_year=inflow,
                outflow_year=outflow,
                technology=technology,
            )

            if lifetime_use == 0:
                raise ValueError(
                    f"Cannot derive production/disposal for "
                    f"population ({inflow}, {outflow}) because its "
                    "lifetime use is zero."
                )

            objects = requested_use / lifetime_use

            common = {
                "inflow_year": inflow,
                "outflow_year": outflow,
            }

            if self.technologies is not None:
                common["technology"] = technology

            rows.extend(
                [
                    {
                        **common,
                        "year": inflow,
                        "flow": "production",
                        "value": objects,
                    },
                    {
                        **common,
                        "year": outflow,
                        "flow": "disposal",
                        "value": objects,
                    },
                ]
            )

        if not rows:
            return df

        return pd.concat(
            [
                df,
                pd.DataFrame(
                    rows,
                    columns=df.columns,
                ),
            ],
            ignore_index=True,
        )

    def _add_production_eol_from_population(
        self,
        df: pd.DataFrame,
        population_sizes: dict[tuple[int, int, Any], float],
        scale: float = 1.0,
    ) -> pd.DataFrame:
        """
        Add production and disposal flows directly from dMFA
        population sizes.

        This is used by lifetime_profile(), where the represented
        population is explicitly known.
        """
        rows = []

        for (
            inflow,
            outflow,
            technology,
        ), size in population_sizes.items():
            size *= scale

            common = {
                "inflow_year": inflow,
                "outflow_year": outflow,
            }

            if self.technologies is not None:
                common["technology"] = technology

            rows.extend(
                [
                    {
                        **common,
                        "year": inflow,
                        "flow": "production",
                        "value": size,
                    },
                    {
                        **common,
                        "year": outflow,
                        "flow": "disposal",
                        "value": size,
                    },
                ]
            )

        if not rows:
            return df

        return pd.concat(
            [
                df,
                pd.DataFrame(
                    rows,
                    columns=df.columns,
                ),
            ],
            ignore_index=True,
        )

    # ------------------------------------------------------------------
    # Public API: function profile
    # ------------------------------------------------------------------

    def function_profile(
        self,
        use_year: int | Sequence[int],
        *,
        inflow_year: int | Sequence[int] | None = None,
        outflow_year: int | Sequence[int] | None = None,
        technology: Any | Sequence[Any] | None = None,
        scale_to: float | Sequence[float] | None = None,
        scale_by: str = "use",
        include_production_eol: bool = False,
        include_direct_consumption: bool = False,
    ) -> pd.DataFrame:
        """
        Return a tidy profile of functional use demand.

        ``use_year`` specifies when function is requested.

        ``inflow_year`` and ``outflow_year`` restrict the homogeneous
        populations contributing that function.

        ``scale_by="use"`` scales functional demand.

        ``scale_by="objects"`` scales the selected dMFA populations.

        Optional production/EOL and direct-consumption flows are derived
        after the use profile has been scaled.

        Production and disposal are only added for populations that
        actually contribute to the requested use_year(s).
        """
        use_years = self._as_list(use_year)
        inflow_years = self._as_list(inflow_year)
        outflow_years = self._as_list(outflow_year)

        technologies = self._requested_technologies(
            technology
        )

        # Retrieve complete population sizes once. These are needed if
        # object-based scaling is requested.
        population_sizes = self._population_sizes(
            inflow_years=inflow_years,
            outflow_years=outflow_years,
            technologies=technologies,
        )

        if not population_sizes:
            raise ValueError(
                "No population matches the requested "
                "inflow_year, outflow_year, or technology."
            )

        rows = []

        for year in use_years:
            active = self._active_population_sizes(
                year,
                population_sizes,
            )

            for population, stock in active.items():
                inflow, outflow, tech = population

                specific_use = self._scalar(
                    "specific_use",
                    year=year,
                    cohort=inflow,
                    technology=tech,
                )

                row = {
                    "year": year,
                    "inflow_year": inflow,
                    "outflow_year": outflow,
                    "flow": "use",
                    "value": specific_use * stock,
                }

                if self.technologies is not None:
                    row["technology"] = tech

                rows.append(row)

        if not rows:
            raise ValueError(
                "No active population matches the requested "
                "use_year, inflow_year, outflow_year, or technology."
            )

        columns = [
            "year",
            "inflow_year",
            "outflow_year",
            "flow",
            "value",
        ]

        if self.technologies is not None:
            columns.append("technology")

        df = pd.DataFrame(
            rows,
            columns=columns,
        )

        df = self._scale(
            df,
            use_years,
            scale_to,
            scale_by,
            population_sizes=population_sizes,
        )

        if include_direct_consumption:
            df = self._add_direct_consumption(df)

        if include_production_eol:
            df = self._add_production_eol_from_profile(df)

        df.attrs.update(
            {
                "scale_by": scale_by,
                "technology": technology,
                "include_direct_consumption": (
                    include_direct_consumption
                ),
                "include_production_eol": (
                    include_production_eol
                ),
            }
        )

        return df

    # ------------------------------------------------------------------
    # Public API: lifetime profile
    # ------------------------------------------------------------------

    def lifetime_profile(
        self,
        *,
        number_of_objects: float | None = None,
        inflow_year: int | Sequence[int] | None = None,
        outflow_year: int | Sequence[int] | None = None,
        technology: Any | Sequence[Any] | None = None,
        include_production_eol: bool = False,
        include_direct_consumption: bool = False,
    ) -> pd.DataFrame:
        """
        Return the complete lifetime use profiles of selected populations.

        ``number_of_objects=None``
            Use the actual dMFA population sizes.

        ``number_of_objects=N``
            Scale the selected populations proportionally so that their
            combined size equals N.

        The relative composition of the selected populations is always
        inherited from the dMFA.

        Unlike ``function_profile()``, this method selects populations
        first and then expands each one over its complete lifetime.
        """
        if (
            number_of_objects is not None
            and number_of_objects < 0
        ):
            raise ValueError(
                "number_of_objects must be non-negative."
            )

        inflow_years = self._as_list(inflow_year)
        outflow_years = self._as_list(outflow_year)

        technologies = self._requested_technologies(
            technology
        )

        population_sizes = self._population_sizes(
            inflow_years=inflow_years,
            outflow_years=outflow_years,
            technologies=technologies,
        )

        if not population_sizes:
            raise ValueError(
                "No populations match the requested "
                "inflow_year, outflow_year, or technology."
            )

        total_objects = sum(
            population_sizes.values()
        )

        if total_objects == 0:
            raise ValueError(
                "The selected populations contain zero objects."
            )

        scale = (
            1.0
            if number_of_objects is None
            else number_of_objects / total_objects
        )

        rows = []

        for (
            inflow,
            outflow,
            tech,
        ), population_size in population_sizes.items():

            population_size *= scale

            start = self._year_index[inflow]
            end = self._year_index[outflow]

            use = self._year_series(
                "specific_use",
                inflow_year=inflow,
                technology=tech,
            )

            for year_idx in range(start, end):
                row = {
                    "year": self.years[year_idx],
                    "inflow_year": inflow,
                    "outflow_year": outflow,
                    "flow": "use",
                    "value": (
                        population_size
                        * use[year_idx]
                    ),
                }

                if self.technologies is not None:
                    row["technology"] = tech

                rows.append(row)

        columns = [
            "year",
            "inflow_year",
            "outflow_year",
            "flow",
            "value",
        ]

        if self.technologies is not None:
            columns.append("technology")

        df = pd.DataFrame(
            rows,
            columns=columns,
        )

        if include_direct_consumption:
            df = self._add_direct_consumption(df)

        if include_production_eol:
            df = self._add_production_eol_from_population(
                df,
                population_sizes,
                scale=scale,
            )

        df.attrs.update(
            {
                "number_of_objects": number_of_objects,
                "technology": technology,
                "include_direct_consumption": (
                    include_direct_consumption
                ),
                "include_production_eol": (
                    include_production_eol
                ),
            }
        )

        return df

    # ------------------------------------------------------------------
    # Small helpers
    # ------------------------------------------------------------------

    def _requested_technologies(
        self,
        technology: Any | Sequence[Any] | None,
    ) -> list[Any | None]:
        if self.technologies is None:
            if technology is not None:
                raise ValueError(
                    "This dataset has no technology dimension, so "
                    "'technology' must be None."
                )

            return [None]

        requested = self._as_list(technology)

        if requested is None:
            return list(self.technologies)

        unknown = [
            tech
            for tech in requested
            if tech not in self.technologies
        ]

        if unknown:
            raise ValueError(
                f"Unknown technologies: {unknown}. "
                f"Available technologies: {self.technologies}"
            )

        return requested

    @staticmethod
    def _as_list(
        value: Any,
    ) -> list | None:
        """Normalise scalar-or-sequence arguments to lists."""
        if value is None:
            return None

        if isinstance(value, (str, bytes)):
            return [value]

        if isinstance(value, np.ndarray):
            return value.tolist()

        if isinstance(value, Sequence):
            return list(value)

        return [value]