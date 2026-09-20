import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import numpy as np
import seaborn as sns
import re
import os

plt.rcParams.update({
    'font.size': 11,
    'axes.titlesize': 8,
    'axes.labelsize': 8,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'text.usetex': False, # if True, requires LaTeX installation; some figures will have visual errors without
    #'font.family': 'Helvetica',
})
plt.rcParams['text.latex.preamble'] = r'''
\usepackage{siunitx}
\sisetup{detect-all}
\usepackage{helvet}
\usepackage{sansmath}
\sansmath
'''

class BasePlotter:
    """Base class for creating consistent matplotlib plots with legends."""
    
    def __init__(self, figsize=(8, 5), color_func=None):
        self.figsize = figsize
        self.get_color_map = color_func or self._default_color_map

    def plot(self, ax=None, data=None, return_legend=False, add_legend=True, **kwargs):
        """
        Main plotting method.
        
        Parameters
        ----------
        ax : matplotlib.axes.Axes, optional
            Axes to plot on. If None, creates new figure.
        data : array-like, optional
            Data to plot. Passed to _draw method.
        return_legend : bool, default=False
            If True, returns legend handles as third return value.
        add_legend : bool, default=True
            If False, skips adding legend (useful for subplots where you'll add it manually).
        **kwargs : dict
            Additional arguments passed to _draw and _post_draw.
            
        Returns
        -------
        fig : matplotlib.figure.Figure
        ax : matplotlib.axes.Axes
        legend_handles : list, optional (if return_legend=True)
        """
        # Reset legend labels for each plot call
        self._legend_labels = {}
        
        internal_fig = False
        if ax is None:
            fig, ax = plt.subplots(figsize=self.figsize)
            internal_fig = True
        else:
            fig = ax.figure

        # Validate data
        if data is None:
            raise ValueError("Data must be provided to plot method")

        # Child class draws its data
        self._draw(ax=ax, data=data, **kwargs)

        # Post-draw formatting
        self._post_draw(ax=ax, data=data, **kwargs)

        # Add legend only if requested and labels exist
        legend_handles = None
        if add_legend and self._legend_labels:
            legend_handles = self._add_legend(ax, self._legend_labels, **kwargs)

        if internal_fig:
            plt.show()

        if return_legend:
            return fig, ax, legend_handles
        else:
            return fig, ax

    def save(self, filepath, fig=None, data=None, dpi=300, bbox_inches='tight', png_or_pdf='png'):
        """
        Save the plot as PDF and PNG files, and optionally save the data as CSV.
        """
        import os
        import re
        
        if fig is None:
            fig = plt.gcf()
        
        # Convert all backslashes to forward slashes
        filepath = str(filepath).replace('\\', '/')
        
        # Split path
        parts = filepath.rsplit('/', 1)
        if len(parts) == 2:
            directory, filename = parts
        else:
            directory = ''
            filename = parts[0]
        
        # Sanitize filename only
        safe_filename = re.sub(r'[^\w\-.]', '_', filename)
        safe_filename = re.sub(r'_+', '_', safe_filename)
        
        # Reconstruct with forward slashes
        if directory:
            safe_path = f"{directory}/{safe_filename}"
        else:
            safe_path = safe_filename
        
        # Remove extension
        if '.' in safe_filename:
            base_path = safe_path.rsplit('.', 1)[0]
        else:
            base_path = safe_path
        
        # Create directory (convert to OS-specific path only here)
        directory = base_path.rsplit('/', 1)[0] if '/' in base_path else ''
        if directory:
            os.makedirs(directory, exist_ok=True)
        
        # Save files
        result = {}
        if png_or_pdf in ['png', 'both']:
            png_path = f"{base_path}.png"
            fig.savefig(png_path, format='png', dpi=dpi, bbox_inches=bbox_inches)
            result['png'] = png_path
        if png_or_pdf in ['pdf', 'both']:
            pdf_path = f"{base_path}.pdf"
            fig.savefig(pdf_path, format='pdf', bbox_inches=bbox_inches)
            result['pdf'] = pdf_path 
        
        # Save data as CSV
        if data is not None:
            csv_paths = self._save_data_as_csv(base_path, data)
            result['csv'] = csv_paths
        
        return result

    def _save_data_as_csv(self, base_path, data):
        """
        Helper method to save data as CSV file(s).
        
        Parameters
        ----------
        base_path : str
            Base filepath without extension.
        data : pandas.DataFrame, list, or dict
            Data to save.
            
        Returns
        -------
        str, list, or dict
            Path(s) to saved CSV file(s).
        """
        import pandas as pd
        import re
        
        # Single DataFrame
        if isinstance(data, pd.DataFrame):
            csv_path = f"{base_path}.csv"
            data.to_csv(csv_path)
            return csv_path
        
        # List of DataFrames
        elif isinstance(data, list):
            csv_paths = []
            for idx, df in enumerate(data):
                if isinstance(df, pd.DataFrame):
                    csv_path = f"{base_path}_{idx}.csv"
                    df.to_csv(csv_path)
                    csv_paths.append(csv_path)
            return csv_paths
        
        # Dictionary of DataFrames
        elif isinstance(data, dict):
            csv_paths = {}
            for idx, (key, df) in enumerate(data.items()):
                if isinstance(df, pd.DataFrame):
                    # Use simple numbered files
                    csv_path = f"{base_path}_{idx}.csv"
                    df.to_csv(csv_path)
                    csv_paths[key] = csv_path
            return csv_paths
        
        else:
            # Unsupported data type, return None
            return None

    def _default_color_map(self, labels):
        """Create default color mapping using seaborn colorblind palette."""
        colors = sns.color_palette("colorblind", n_colors=len(labels))
        return {label: color for label, color in zip(labels, colors)}
    
    def _draw(self, ax, data, **kwargs):
        """
        Draw the plot. Must be implemented by child classes.
        
        Parameters
        ----------
        ax : matplotlib.axes.Axes
            Axes to draw on.
        data : array-like
            Data to plot.
        **kwargs : dict
            Additional plotting arguments.
        """
        raise NotImplementedError("Subclasses must implement _draw method")

    def _post_draw(self, ax, data, **kwargs):
        """
        Apply common formatting after drawing.
        
        Features:
        - Horizontal/vertical reference lines
        - Axis range setting
        - Scientific notation formatting
        - Tick label rotation
        - Title formatting
        """
        orientation = kwargs.get("orientation", "vertical")
        hlines = kwargs.get("hlines", [])
        title = kwargs.get("title", "")
        title_loc = kwargs.get("title_loc", "left")
        title_rotation = kwargs.get("title_rotation", 0)
        sci_notation = kwargs.get("sci_notation", True)
        keep_x = kwargs.get("keep_x", True)
        keep_y = kwargs.get("keep_y", True)
        turn_x_label = kwargs.get("turn_x_label", orientation == "vertical")
        x_label = kwargs.get("x_label", "")
        y_label = kwargs.get("y_label", "")
        x_tick_mult = kwargs.get("x_tick_mult", None)
        x_tick_int = kwargs.get("x_tick_int", None)

        axis_range = getattr(self, "_axis_range", None)
        x_axis_range = getattr(self, "_x_axis_range", None)
        y_axis_range = getattr(self, "_y_axis_range", None)

        # Add reference lines (if provided)
        if orientation == "vertical":
            for val in hlines:
                ax.axhline(val, color="black", linestyle="dotted", linewidth=1)
        else:
            for val in hlines:
                ax.axvline(val, color="black", linestyle="dotted", linewidth=1)

        # If specified, add reference lines to the legend under a single label 
        hlines_label = kwargs.get("hlines_label")
        if hlines_label and hlines:
            self._legend_labels[hlines_label] = mlines.Line2D(
                [], [], color="black", linestyle="dotted", linewidth=1, label=hlines_label
    )

        # Set axis range (if computed by subclass)
        if axis_range is not None:
            if orientation == "vertical":
                ax.set_ylim(*axis_range)
            else:
                ax.set_xlim(*axis_range)
        if x_axis_range is not None:
            ax.set_xlim(*x_axis_range)
        if y_axis_range is not None:
            ax.set_ylim(*y_axis_range)

        # Add annotations (if provided)
        self._add_annotations(ax, kwargs.get("annotations", []))

        # Apply scientific notation to value axis
        if sci_notation:
            formatter = mticker.ScalarFormatter(useMathText=True)
            formatter.set_scientific(True)
            formatter.set_powerlimits((0, 0))
            axis_to_format = ax.xaxis if orientation == "horizontal" else ax.yaxis
            axis_to_format.set_major_locator(mticker.MaxNLocator(steps=[1, 2, 5, 10]))
            axis_to_format.set_major_formatter(formatter)

        if x_tick_mult:
            ax.xaxis.set_major_locator(mticker.MultipleLocator(x_tick_mult))
        elif x_tick_int:
            ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))

        # Control axis tick labels & axis labels
        if not keep_y:
            ax.set_yticklabels([])
        else: ax.set_ylabel(y_label)
        if not keep_x:
            ax.set_xticklabels([])
        else: 
            ax.set_xlabel(x_label)
        
        # Rotate x-axis tick labels if specified
        ax.tick_params(axis="x", labelrotation=90 if turn_x_label else 0)

        # Add title
        if title:
            ax.set_title(title, loc=title_loc, rotation = title_rotation, fontweight="bold")

    def _add_legend(self, ax, legend_labels, **kwargs):
        """
        Add legend below the plot, dynamically positioned based on x-tick labels.
        
        Parameters
        ----------
        ax : matplotlib.axes.Axes
            Axes containing the plot.
        legend_labels : dict
            Dictionary mapping label strings to matplotlib artists.
        **kwargs : dict
            Additional arguments:
            - legend_ncol : int, default=3
            - legend_position : str, default='below' ('below' or 'right')
            - legend_padding : float, default=0.02 (extra space in figure coords)
            
        Returns
        -------
        legend : matplotlib.legend.Legend
        """
        fig = ax.figure
        legend_ncol = kwargs.get("legend_ncol", 3)
        legend_position = kwargs.get("legend_position", "below")
        legend_padding = kwargs.get("legend_padding", 0.02)
        legend_frameon = kwargs.get("legend_frameon", False)
        
        if legend_position == "below":
            # Force a draw to get accurate label measurements
            fig.canvas.draw()
            renderer = fig.canvas.get_renderer()
            
            # Get the axes position in figure coordinates
            bbox = ax.get_position()
            
            # Find the lowest point of x-tick labels
            x_labels = ax.get_xticklabels()
            if x_labels:
                # Get bounding boxes of all visible x-tick labels
                label_bboxes = []
                for label in x_labels:
                    if label.get_visible() and label.get_text():
                        # Get bbox in display coordinates
                        bbox_display = label.get_window_extent(renderer)
                        # Convert to figure coordinates
                        bbox_fig = bbox_display.transformed(fig.transFigure.inverted())
                        label_bboxes.append(bbox_fig)
                
                if label_bboxes:
                    # Find the lowest point (minimum y0) of all labels
                    min_y = min(bb.y0 for bb in label_bboxes)
                    # Position legend below the lowest label with padding
                    legend_y = min_y - legend_padding
                else:
                    # No visible labels, position below axes
                    legend_y = bbox.y0 - legend_padding
            else:
                # No labels, position below axes
                legend_y = bbox.y0 - legend_padding
            
            # Create the legend
            legend_handles = fig.legend(
                legend_labels.values(),
                legend_labels.keys(),
                ncol=legend_ncol,
                frameon=legend_frameon,
                bbox_to_anchor=(0.5, legend_y),
                loc='upper center'
            )
        else:
            # Position legend in provided location
            legend_handles = ax.legend(
                legend_labels.values(),
                legend_labels.keys(),
                loc=legend_position,
                ncol=legend_ncol,
                frameon=legend_frameon
            )
        
        return legend_handles

    def _add_annotations(self, ax, annotations):
        """
        Add text annotations to the plot.

        Parameters
        ----------
        annotations : list of dict
            Each dict supports:
            - text (str, required): annotation text
            - x (float, required): x position
            - y (float, required): y position
            - xycoords (str, default='data'): coordinate system for x/y.
                Common values:
                - 'data'          : axis data coordinates (default)
                - 'axes fraction' : 0–1 relative to axes box
                - 'figure fraction': 0–1 relative to figure
            - ha (str, default='left'): horizontal anchor ('left', 'center', 'right')
            - va (str, default='bottom'): vertical anchor ('top', 'center', 'bottom', 'baseline')
            - fontsize (int, default=10)
            - color (str, default='black')
            - fontweight (str, default='normal'): e.g. 'bold'
            - rotation (float, default=0): degrees counter-clockwise
            - arrow (dict, optional): if present, draws an arrow from text to target.
                Sub-keys:
                - tx, ty (float): arrow target coordinates
                - xycoords (str, default='data'): coord system for target
                - arrowprops (dict): passed directly to ax.annotate's arrowprops.
                    Defaults to a simple gray arrow if omitted.

        Examples
        --------
        annotations=[
            # Simple text at data coordinates
            {"text": "Peak", "x": 3, "y": 1500, "ha": "center", "color": "red"},

            # Text in axes-relative coordinates (i.e., independent of data range)
            {"text": "n=42", "x": 0.02, "y": 0.97, "xycoords": "axes fraction",
            "va": "top", "fontsize": 8},

            # Arrow pointing from label to a data point
            {"text": "Outlier", "x": 0.5, "y": 0.9, "xycoords": "axes fraction",
            "arrow": {"tx": 7, "ty": 2200, "xycoords": "data",
                    "arrowprops": {"arrowstyle": "->", "color": "black"}}},
        ]
        """
        for ann in annotations:
            text  = ann.get("text", "")
            x     = ann.get("x", 0)
            y     = ann.get("y", 0)
            coord = ann.get("xycoords", "data")
            ha    = ann.get("ha", "left")
            va    = ann.get("va", "bottom")

            style = dict(
                fontsize   = ann.get("fontsize", 8),
                color      = ann.get("color", "black"),
                fontweight = ann.get("fontweight", "normal"),
                rotation   = ann.get("rotation", 0),
            )

            arrow = ann.get("arrow")
            if arrow:
                # Arrow: text is at (x, y), arrowhead points at (tx, ty)
                default_arrowprops = {"arrowstyle": "->", "color": "gray", "lw": 1}
                ax.annotate(
                    text,
                    xy     = (arrow["tx"], arrow["ty"]),
                    xytext = (x, y),
                    xycoords      = arrow.get("xycoords", "data"),
                    textcoords    = coord,
                    ha=ha, va=va,
                    arrowprops    = arrow.get("arrowprops", default_arrowprops),
                    **style,
                )
            else:
                ax.text(x, y, text, ha=ha, va=va, transform=_resolve_transform(ax, coord), **style)

def _resolve_transform(ax, xycoords):
    """Map xycoords string to the correct matplotlib transform."""
    return {
        "data"            : ax.transData,
        "axes fraction"   : ax.transAxes,
        "figure fraction" : ax.figure.transFigure,
    }.get(xycoords, ax.transData)

class ContributionPlotter(BasePlotter):
    """
    Plot stacked bar charts showing positive and negative contributions.
    
    Automatically handles:
    - Separate stacking for positive and negative values
    - Color mapping for each column
    - Optional total markers
    - Dynamic axis range calculation
    """
    
    def _draw(self, ax, data, **kwargs):
        """
        Draw stacked contribution bars.
        
        Parameters
        ----------
        ax : matplotlib.axes.Axes
            Axes to draw on.
        data : pandas.DataFrame
            DataFrame where columns are contribution categories.
        **kwargs : dict
            orientation : str, default='vertical'
                'vertical' or 'horizontal' bars.
            show_total : bool, default=False
                Whether to show total markers.
            axis_range : tuple, default=computed based on range of data
                Custom range for axis along which values are plotted.
        """
        orientation = kwargs.get("orientation", "vertical")
        show_total = kwargs.get("show_total", False)
        total_marker_size = kwargs.get("total_marker_size", 50)

        if data is None or data.empty:
            raise ValueError("Data cannot be None or empty")
        
        df = data
        color_map = self.get_color_map(df.columns)
        self._axis_range = kwargs.get("axis_range", self._compute_axis_range(df))

        axis_labels = [str(idx) for idx in df.index]
        n = len(df)
        bottom_pos = np.zeros(n)
        bottom_neg = np.zeros(n)

        # Draw stacked bars for each column
        for col in df.columns:
            vals = df[col].values
            color = color_map[col]
            
            # Separate positive and negative values for proper stacking
            pos_vals = np.where(vals > 0, vals, 0)
            neg_vals = np.where(vals < 0, vals, 0)

            if orientation == "vertical":
                ax.bar(axis_labels, pos_vals, bottom=bottom_pos, 
                      color=color, zorder=0, width=0.8)
                ax.bar(axis_labels, neg_vals, bottom=bottom_neg, 
                      color=color, zorder=0, width=0.8)
            else:
                ax.barh(axis_labels, pos_vals, left=bottom_pos, 
                       color=color, zorder=0, height=0.8)
                ax.barh(axis_labels, neg_vals, left=bottom_neg, 
                       color=color, zorder=0, height=0.8)

            # Update cumulative bottoms/lefts
            bottom_pos += pos_vals
            bottom_neg += neg_vals

            # Add to legend (only once per column)
            if col not in self._legend_labels:
                self._legend_labels[col] = mpatches.Patch(color=color, label=col)

        # Add total markers if requested
        if show_total:
            self._add_totals(ax, df, orientation, total_marker_size)

        # Flip y-axis in case of horizontal orientation
        if orientation == "horizontal" and not ax.yaxis_inverted(): ax.invert_yaxis()

    def _compute_axis_range(self, df):
        """
        Calculate appropriate axis range with padding.
        
        Parameters
        ----------
        df : pandas.DataFrame
            Data to analyze.
            
        Returns
        -------
        tuple
            (min_value, max_value) with 6% padding on each side.
        """
        values = df.values
        
        # Sum positive and negative contributions separately for each row
        pos_sums = np.sum(np.where(values > 0, values, 0), axis=1)
        neg_sums = np.sum(np.where(values < 0, values, 0), axis=1)
        
        # Get the most extreme values
        max_pos = np.max(pos_sums) if pos_sums.size > 0 else 0
        min_neg = np.min(neg_sums) if neg_sums.size > 0 else 0
        
        # Calculate range and add padding
        range_length = max_pos - min_neg
        
        # Handle edge case of all zeros
        if range_length == 0:
            return -1, 1
        
        padding = 0.06 * range_length
        return min_neg - padding, max_pos + padding

    def _add_totals(self, ax, df, orientation, total_marker_size):
        """
        Add scatter markers showing row totals.
        
        Parameters
        ----------
        ax : matplotlib.axes.Axes
            Axes to draw on.
        df : pandas.DataFrame
            Data to sum.
        orientation : str
            'vertical' or 'horizontal'.
        """

        total = df.sum(axis=1)
        positions = np.arange(len(df))
        
        if orientation == "vertical":
            ax.scatter(positions, total, color="k", marker="D", 
                      s=total_marker_size, zorder=10, label="Total")
        else:
            ax.scatter(total, positions, color="k", marker="D", 
                      s=total_marker_size, zorder=10, label="Total")
        
        # Add to legend
        self._legend_labels["Total"] = mlines.Line2D(
            [], [], color="k", marker="D", linestyle="None", 
            markersize=6, label="Total"
        )

class ContributionComparisonPlotter(BasePlotter):
    """
    Plot multiple stacked bar charts side-by-side for comparison.
    
    Each DataFrame in the input list gets its own stacked bar chart,
    positioned next to each other for easy comparison.
    """

    def _draw(self, ax, data, **kwargs):
        """
        Draw comparison stacked bars.
        
        Parameters
        ----------
        ax : matplotlib.axes.Axes
            Axes to draw on.
        data : list of pandas.DataFrame
            List of DataFrames to compare. Each DataFrame should have the
            same index, but can have different columns.
        **kwargs : dict
            orientation : str, default='vertical'
                'vertical' or 'horizontal' bars.
            show_total : bool, default=False
                Whether to show total markers.
            group_labels : list of str, optional
                Labels for each DataFrame. If not provided, uses "Group 1", "Group 2", etc.
            bar_width : float, default=0.8
                Width of each bar (will be divided among DataFrames).
            gap_fraction : float, default=0.05
                Fraction of bar_width to use as gap between groups (0.0 to 1.0).
                E.g., 0.05 = 5% gap, 0.10 = 10% gap.
        """
        orientation = kwargs.get("orientation", "vertical")
        show_total = kwargs.get("show_total", False)
        total_marker_size = kwargs.get("total_marker_size", 20)
        group_labels = kwargs.get("group_labels", None)
        bar_width = kwargs.get("bar_width", 0.8)
        gap_fraction = kwargs.get("gap_fraction", 0.05)
        
        if data is None or len(data) == 0:
            raise ValueError("Data must be a non-empty list of DataFrames")
        
        df_list = data
        n_groups = len(df_list)
        
        # Validate that all DataFrames have the same index
        base_index = df_list[0].index
        for i, df in enumerate(df_list[1:], 1):
            if not df.index.equals(base_index):
                raise ValueError(f"DataFrame {i} has different index than DataFrame 0")
        
        # Create group labels if not provided
        if group_labels is None:
            group_labels = [f"Group {i+1}" for i in range(n_groups)]
        elif len(group_labels) != n_groups:
            raise ValueError(f"group_labels length ({len(group_labels)}) must match number of DataFrames ({n_groups})")
        
        # Collect all unique columns across all DataFrames for consistent coloring
        all_columns = []
        for df in df_list:
            all_columns.extend([col for col in df.columns if col not in all_columns])
        
        color_map = self.get_color_map(all_columns)
        self._axis_range = kwargs.get("axis_range", self._compute_axis_range(df_list))
        
        # Set up positions
        axis_labels = [str(idx) for idx in base_index]
        n_positions = len(base_index)
        positions = np.arange(n_positions)
        
        # Calculate bar width for each group with small gap between groups
        total_bar_width = bar_width
        single_bar_width = total_bar_width * (1 - gap_fraction) / n_groups
        
        # Calculate offsets
        offsets = np.linspace(-total_bar_width/2 + single_bar_width/2, 
                             total_bar_width/2 - single_bar_width/2, 
                             n_groups)
        
        # Plot each DataFrame
        for group_idx, (df, offset, label) in enumerate(zip(df_list, offsets, group_labels)):
            n = len(df)
            bottom_pos = np.zeros(n)
            bottom_neg = np.zeros(n)
            
            # Calculate positions for this group
            bar_positions = positions + offset
            
            # Stack bars for each column
            for col in df.columns:
                vals = df[col].values
                color = color_map[col]
                
                pos_vals = np.where(vals > 0, vals, 0)
                neg_vals = np.where(vals < 0, vals, 0)
                
                if orientation == "vertical":
                    ax.bar(bar_positions, pos_vals, width=single_bar_width,
                          bottom=bottom_pos, color=color, zorder=0)
                    ax.bar(bar_positions, neg_vals, width=single_bar_width,
                          bottom=bottom_neg, color=color, zorder=0)
                else:
                    ax.barh(bar_positions, pos_vals, height=single_bar_width,
                           left=bottom_pos, color=color, zorder=0)
                    ax.barh(bar_positions, neg_vals, height=single_bar_width,
                           left=bottom_neg, color=color, zorder=0)
                
                bottom_pos += pos_vals
                bottom_neg += neg_vals
                
                # Add to legend (only once per column)
                if col not in self._legend_labels:
                    self._legend_labels[col] = mpatches.Patch(color=color, label=col)
        
            # Add totals if requested
            if show_total:
                self._add_totals(ax, df, bar_positions, orientation, label, group_idx, total_marker_size)

        # Flip y-axis in case of horizontal orientation
        if orientation == "horizontal" and not ax.yaxis_inverted(): ax.invert_yaxis()

        # Set tick labels at center positions
        if orientation == "vertical":
            ax.set_xticks(positions)
            ax.set_xticklabels(axis_labels)
        else:
            ax.set_yticks(positions)
            ax.set_yticklabels(axis_labels)
    
    def _compute_axis_range(self, df_list):
        """
        Calculate appropriate axis range across all DataFrames.
        
        Parameters
        ----------
        df_list : list of pandas.DataFrame
            DataFrames to analyze.
            
        Returns
        -------
        tuple
            (min_value, max_value) with 6% padding on each side.
        """
        max_pos = 0
        min_neg = 0
        
        for df in df_list:
            values = df.values
            
            # Sum positive and negative contributions separately for each row
            pos_sums = np.sum(np.where(values > 0, values, 0), axis=1)
            neg_sums = np.sum(np.where(values < 0, values, 0), axis=1)
            
            # Update extremes
            if pos_sums.size > 0:
                max_pos = max(max_pos, np.max(pos_sums))
            if neg_sums.size > 0:
                min_neg = min(min_neg, np.min(neg_sums))
        
        # Calculate range and add padding
        range_length = max_pos - min_neg
        
        # Handle edge case of all zeros
        if range_length == 0:
            return -1, 1
        
        padding = 0.06 * range_length
        return min_neg - padding, max_pos + padding
    
    def _add_totals(self, ax, df, positions, orientation, group_label, group_idx, total_marker_size):
        """
        Add scatter markers showing row totals for this group.
        
        Parameters
        ----------
        ax : matplotlib.axes.Axes
            Axes to draw on.
        df : pandas.DataFrame
            Data to sum.
        positions : numpy.ndarray
            X or Y positions for the markers.
        orientation : str
            'vertical' or 'horizontal'.
        group_label : str
            Label for this group.
        group_idx : int
            Index of this group (for marker style variation).
        """
        total = df.sum(axis=1)
        
        # Vary marker style for different groups
        markers = ["D", "o", "s", "^", "v", "*", "P"]
        marker = markers[group_idx % len(markers)]
        
        if orientation == "vertical":
            ax.scatter(positions, total, color="k", marker=marker, 
                      s=total_marker_size, zorder=10, label=f"Total - {group_label}")
        else:
            ax.scatter(total, positions, color="k", marker=marker, 
                      s=total_marker_size, zorder=10, label=f"total - {group_label}")
        
        # Add to legend if not already present
        legend_key = f"total - {group_label}"
        if legend_key not in self._legend_labels:
            self._legend_labels[legend_key] = mlines.Line2D(
                [], [], color="k", marker=marker, linestyle="None", 
                markersize=6, label=legend_key
            )

class ScatterPlotter(BasePlotter):
    """
    Plot scatter plots with optional line connections.
    
    Automatically handles:
    - Multiple series from DataFrame columns
    - Color mapping for each series
    - Customizable markers and line styles
    - Index as x-axis values
    """
    
    def _draw(self, ax, data, **kwargs):
        """
        Draw scatter plot with optional lines.
        
        Parameters
        ----------
        ax : matplotlib.axes.Axes
            Axes to draw on.
        data : pandas.DataFrame
            DataFrame where index contains x-values and columns contain y-values.
        **kwargs : dict
            marker : str or list, default='o'
                Marker style(s). Single value or list matching number of columns.
            linestyle : str or list, default='-'
                Line style(s). Single value or list matching number of columns.
            markersize : int or float, default=6
                Size of markers.
            linewidth : int or float, default=1.5
                Width of lines.
            show_lines : bool, default=True
                Whether to connect points with lines.
            alpha : float, default=1.0
                Transparency of markers and lines.
        """
        if data is None or data.empty:
            raise ValueError("Data cannot be None or empty")
        
        df = data
        color_map = self.get_color_map(df.columns)

        # Get styling parameters
        marker = kwargs.get("marker", "o")
        linestyle = kwargs.get("linestyle", "-")
        markersize = kwargs.get("markersize", 6)
        linewidth = kwargs.get("linewidth", 1.5)
        show_lines = kwargs.get("show_lines", True)
        show_stem = kwargs.get("show_stem", False)
        alpha = kwargs.get("alpha", 1.0)
        skip_zeroes = kwargs.get("skip_zeroes", False)
        
        # Convert marker and linestyle to lists if single values provided
        if isinstance(marker, str):
            markers = [marker] * len(df.columns)
        else:
            markers = marker
            
        if isinstance(linestyle, str):
            linestyles = [linestyle] * len(df.columns)
        else:
            linestyles = linestyle
        
        # Ensure we have enough markers and linestyles
        if len(markers) < len(df.columns):
            markers = markers * (len(df.columns) // len(markers) + 1)
        if len(linestyles) < len(df.columns):
            linestyles = linestyles * (len(df.columns) // len(linestyles) + 1)
        
        # Get x-values from index
        x_values = df.index.values
        
        self._x_axis_range = kwargs.get("x_axis_range", (min(x_values), max(x_values)))

        # Get y-axis range if provided
        if "y_axis_range" in kwargs:
            self._y_axis_range = kwargs.get("y_axis_range")

        # Plot each column as a series
        for idx, col in enumerate(df.columns):
            x_values_here = x_values
            y_values_here = df[col].values
            color = color_map[col]
            m = markers[idx]
            ls = linestyles[idx]

            # If requested, only plot non-zero values
            if skip_zeroes:
                non_zero_mask = y_values_here != 0
                x_values_here = x_values_here[non_zero_mask]
                y_values_here = y_values_here[non_zero_mask]
            
            # Plot with or without lines
            if show_lines:
                ax.plot(x_values_here, y_values_here, marker=m, linestyle=ls,
                       color=color, markersize=markersize, linewidth=linewidth,
                       alpha=alpha, label=col, zorder=3)
            else:
                ax.scatter(x_values_here, y_values_here, marker=m, color=color,
                          s=markersize**2, alpha=alpha, label=col,zorder=3)
            if show_stem:
                ax.vlines(x_values_here, 0, y_values_here, color=color,
                          alpha=alpha*0.5, linewidth=linewidth, zorder=1)

            # Add to legend
            if col not in self._legend_labels:
                self._legend_labels[col] = mlines.Line2D(
                    [], [], color=color, marker=m, linestyle=ls if show_lines else "None",
                    markersize=markersize, linewidth=linewidth, label=col
                )

class WaterfallPlotter(BasePlotter):
    """
    Plot stacked waterfall charts showing cumulative changes over time. Concept based on bw_timex/utils function `plot_characterized_inventory_as_waterfall`.
    
    Automatically handles:
    - Stacked bars with waterfall offsets
    - Optional static (baseline) and prospective (future) periods
    - Step connectors between periods
    - Color mapping for each activity/column
    - Custom activity ordering
    """
    
    def _draw(self, ax, data, **kwargs):
        """
        Draw the waterfall plot on the given axis.
        
        Parameters
        ----------
        ax : matplotlib.axes.Axes
            Axes to draw on.
        data : pandas.DataFrame
            Main time-series data where columns are activities/categories.
        **kwargs : dict
            static_scores : pandas.Series or DataFrame, optional
                Static baseline period (single row).
            prospective_scores : pandas.Series or DataFrame, optional
                Prospective future period (single row).
            order_stacked_activities : list, optional
                Column order for stacking. If None, uses data column order.
            orientation : str, default='vertical'
                'vertical' or 'horizontal' bars (currently only vertical supported).
            show_zero_line : bool, default=True
                Whether to draw a solid black line at y=0.
        """
        import pandas as pd
        
        if data is None or data.empty:
            raise ValueError("Data cannot be None or empty")
        
        # Extract optional parameters from kwargs
        static_scores = kwargs.get("static_scores", None)
        prospective_scores = kwargs.get("prospective_scores", None)
        order_stacked_activities = kwargs.get("order_stacked_activities", None)
        orientation = kwargs.get("orientation", "vertical")
        
        if orientation != "vertical":
            raise NotImplementedError("WaterfallPlotter currently only supports vertical orientation")
        
        # Combine static --> time-explicit --> prospective
        combined_parts = []

        if static_scores is not None:
            combined_parts.append(self._ensure_df(static_scores, label='near-present static'))

        combined_parts.append(self._ensure_df(data))

        if prospective_scores is not None:
            combined_parts.append(self._ensure_df(prospective_scores, label='prospective static'))

        combined_df = pd.concat(combined_parts, axis=0)

        # Activity order
        if order_stacked_activities:
            combined_df = combined_df[order_stacked_activities]
        
        # Get color mapping
        color_map = self.get_color_map(combined_df.columns)
        colors = [color_map[col] for col in combined_df.columns]

        # Compute waterfall offsets ("bottom")
        dynamic_bottom = data.sum(axis=1).cumsum().shift(1).fillna(0)

        if static_scores is not None and prospective_scores is not None:
            bottom = pd.concat([pd.Series([0]), dynamic_bottom, pd.Series([0])])
        elif static_scores is not None:
            bottom = pd.concat([pd.Series([0]), dynamic_bottom])
        elif prospective_scores is not None:
            bottom = pd.concat([dynamic_bottom, pd.Series([0])])
        else:
            bottom = dynamic_bottom

        # Reset index to ensure alignment
        bottom = bottom.reset_index(drop=True)
        combined_df_reset = combined_df.reset_index(drop=True)
        
        # Plot stacked bars manually to maintain control over styling
        x_positions = np.arange(len(combined_df_reset))
        
        # Track cumulative bottoms separately for positive and negative values
        cumulative_pos = bottom.copy()
        cumulative_neg = bottom.copy()
        
        for col in combined_df_reset.columns:
            vals = combined_df_reset[col].values
            color = color_map[col]
            
            # Separate positive and negative values for proper stacking
            pos_vals = np.where(vals > 0, vals, 0)
            neg_vals = np.where(vals < 0, vals, 0)
            
            # Plot positive values
            if np.any(pos_vals > 0):
                ax.bar(
                    x_positions,
                    pos_vals,
                    bottom=cumulative_pos,
                    color=color,
                    edgecolor="black",
                    linewidth=0.5,
                    width=0.8,
                    zorder=1
                )
                cumulative_pos += pos_vals
            
            # Plot negative values
            if np.any(neg_vals < 0):
                ax.bar(
                    x_positions,
                    neg_vals,
                    bottom=cumulative_neg,
                    color=color,
                    edgecolor="black",
                    linewidth=0.5,
                    width=0.8,
                    zorder=1
                )
                cumulative_neg += neg_vals
            
            # Add to legend (only once per column)
            if col not in self._legend_labels:
                self._legend_labels[col] = mpatches.Patch(color=color, label=col)
        
        # Calculate true cumulative totals (bottom + all contributions, positive and negative)
        cumulative = bottom + combined_df_reset.sum(axis=1).values

        # Draw step connectors
        step = bottom.repeat(3).shift(-1)
        step[1::3] = np.nan

        if static_scores is not None:
            step[:4] = np.nan
        if prospective_scores is not None:
            step[-4:] = np.nan

        ax.plot(step.index, step.values, "k", lw=0.5, zorder=0)

        # Add total markers if requested
        show_total = kwargs.get("show_total", False)
        if show_total:
            self._add_totals(ax, cumulative, x_positions, static_scores, prospective_scores, len(data))

        # Set x-axis labels from combined dataframe index
        ax.set_xticks(x_positions)
        # Format labels: convert floats to integers if they're whole numbers
        formatted_labels = []
        for idx in combined_df.index:
            if isinstance(idx, (int, float)):
                # Check if it's a whole number
                if float(idx) == int(idx):
                    formatted_labels.append(str(int(idx)))
                else:
                    formatted_labels.append(str(idx))
            else:
                formatted_labels.append(str(idx))
        ax.set_xticklabels(formatted_labels)
        ax.set_xlabel("")

        # Compute and store axis range if not explicitly provided
        if "axis_range" not in kwargs:
            self._axis_range = self._compute_axis_range(combined_df_reset, bottom)
        else:
            self._axis_range = kwargs.get("axis_range")

        # Vertical separators
        if static_scores is not None:
            ax.axvline(x=0.5, color="black", linestyle="-", lw=1, zorder=2)
        if prospective_scores is not None:
            ax.axvline(x=len(combined_df) - 1.5, color="black", linestyle="-", lw=1, zorder=2)
    
    def _ensure_df(self, obj, label=None):
        """Convert Series to single-row DataFrame if needed."""
        import pandas as pd
        
        if isinstance(obj, pd.DataFrame):
            df = obj.copy()
        else:
            df = obj.to_frame().T  # Series → 1-row DF

        if label is not None:
            df.index = [label]

        return df
    
    def _compute_axis_range(self, df, bottom):
        """
        Calculate appropriate y-axis range with padding.
        
        Parameters
        ----------
        df : pandas.DataFrame
            Combined data (static + dynamic + prospective).
        bottom : pandas.Series
            Bottom values for each bar (waterfall offsets).
            
        Returns
        -------
        tuple
            (min_value, max_value) with 6% padding on each side.
        """
        # Calculate tops separately for positive and negative contributions
        pos_contributions = np.where(df.values > 0, df.values, 0).sum(axis=1)
        neg_contributions = np.where(df.values < 0, df.values, 0).sum(axis=1)
        
        tops_pos = bottom + pos_contributions
        tops_neg = bottom + neg_contributions
        
        # Get the overall range
        min_val = min(bottom.min(), tops_pos.min(), tops_neg.min(), 0)
        max_val = max(bottom.max(), tops_pos.max(), tops_neg.max(), 0)
        
        # Calculate range and add padding
        range_length = max_val - min_val
        
        # Handle edge case of all zeros
        if range_length == 0:
            return -1, 1
        
        padding = 0.06 * range_length
        min_ax = 0 if min_val == 0 else min_val - padding
        max_ax = 0 if max_val == 0 else max_val + padding
        return min_ax, max_ax
    
    def _add_totals(self, ax, totals, x_positions, static_scores, prospective_scores, n_dynamic):
        """
        Add scatter markers showing totals at the top of each stacked bar.
        
        For the time-explicit (dynamic) section, only shows the total at the last position.
        Static and prospective sections always show their totals.
        
        Parameters
        ----------
        ax : matplotlib.axes.Axes
            Axes to draw on.
        totals : numpy.ndarray or pandas.Series
            Total values (top of each bar).
        x_positions : numpy.ndarray
            X-axis positions for each bar.
        static_scores : pandas.Series or DataFrame or None
            Static baseline period.
        prospective_scores : pandas.Series or DataFrame or None
            Prospective future period.
        n_dynamic : int
            Number of dynamic (time-explicit) periods.
        """
        # Determine which positions to show totals for
        show_positions = []
        
        # Static period (if present): show total
        if static_scores is not None:
            show_positions.append(0)
        
        # Dynamic period: only show total at the LAST position
        dynamic_start = 1 if static_scores is not None else 0
        dynamic_end = dynamic_start + n_dynamic
        show_positions.append(dynamic_end - 1)  # Last dynamic position
        
        # Prospective period (if present): show total
        if prospective_scores is not None:
            show_positions.append(len(x_positions) - 1)
        
        # Plot markers only at selected positions
        selected_x = x_positions[show_positions]
        selected_totals = totals[show_positions]
        
        ax.scatter(selected_x, selected_totals, color="k", marker="D", 
                  s=50, zorder=10, label="total")
        
        # Add to legend if not already present
        if "total" not in self._legend_labels:
            self._legend_labels["total"] = mlines.Line2D(
                [], [], color="k", marker="D", linestyle="None", 
                markersize=7, label="total"
            )

class HeatmapPlotter(BasePlotter):
    """
    Plot heatmaps from DataFrame rows and columns.
    
    Automatically handles:
    - Row and column labels from DataFrame index and columns
    - Color mapping via colormap (distinct from BasePlotter's color_func)
    - Optional cell value annotations
    - Colorbar for value scale reference
    """
    
    def _draw(self, ax, data, **kwargs):
        """
        Draw heatmap.
        
        Parameters
        ----------
        ax : matplotlib.axes.Axes
            Axes to draw on.
        data : pandas.DataFrame
            DataFrame where index = row labels, columns = column labels,
            values = heatmap cell values.
        **kwargs : dict
            cmap : str, default='viridis'
                Matplotlib colormap name.
            show_values : bool, default=False
                Whether to annotate each cell with its value.
            value_fmt : str, default='.2f'
                Format string for cell values (e.g. '.0f', '.2f', '.2%').
            value_fontsize : int or float, default=9
                Font size for cell value annotations.
            value_color : str or 'auto', default='auto'
                Color of annotation text. 'auto' picks black or white
                based on colormap luminance at that value.
            vmin : float, default=None
                Minimum value for colormap scaling.
            vmax : float, default=None
                Maximum value for colormap scaling.
            colorbar : bool, default=True
                Whether to show the colorbar.
            colorbar_label : str, default=''
                Label for the colorbar axis.
        """
        if data is None or data.empty:
            raise ValueError("Data cannot be None or empty")

        df = data

        # Kwargs
        cmap            = kwargs.get("cmap", "viridis")
        show_values     = kwargs.get("show_values", False)
        value_fmt       = kwargs.get("value_fmt", ".2f")
        value_fontsize  = kwargs.get("value_fontsize", 9)
        value_color     = kwargs.get("value_color", "auto")
        vmin            = kwargs.get("vmin", None)
        vmax            = kwargs.get("vmax", None)
        show_colorbar   = kwargs.get("colorbar", True)
        colorbar_label  = kwargs.get("colorbar_label", "")
        aspect          = kwargs.get("aspect", "auto")

        values = df.values
        self._im = ax.imshow(values, cmap=cmap, aspect=aspect, vmin=vmin, vmax=vmax)

        # Cell value annotations
        if show_values:
            norm_min = values.min() if vmin is None else vmin
            norm_max = values.max() if vmax is None else vmax
            norm_range = norm_max - norm_min if norm_max != norm_min else 1
            
            # Get the colormap object
            colormap = plt.get_cmap(cmap)

            for row_idx in range(values.shape[0]):
                for col_idx in range(values.shape[1]):
                    cell_val = values[row_idx, col_idx]
                    text = format(cell_val, value_fmt)

                    if value_color == "auto":
                        # Normalize the value to [0, 1] range
                        normalized_val = (cell_val - norm_min) / norm_range
                        
                        # Get the actual RGB color from the colormap
                        rgb = colormap(normalized_val)[:3]
                        
                        # Calculate luminance using standard formula
                        luminance = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
                        
                        # Use white text on dark backgrounds, black on light
                        txt_color = "white" if luminance < 0.5 else "black"
                    else:
                        txt_color = value_color

                    ax.text(
                        col_idx, row_idx, text,
                        ha="center", va="center",
                        fontsize=value_fontsize,
                        color=txt_color,
                    )

        # Colorbar
        if show_colorbar:
            cbar = ax.get_figure().colorbar(self._im, ax=ax)
            if colorbar_label:
                cbar.set_label(colorbar_label)

        # Register columns so BasePlotter doesn't error on legend logic
        for col in df.columns:
            if col not in self._legend_labels:
                self._legend_labels[col] = None

    def _post_draw(self, ax, data, **kwargs):
        """Post-draw formatting, applying heatmap labels without interference from base class."""
        kwargs.setdefault("turn_x_label", False)
        kwargs.setdefault("sci_notation", False)
        super()._post_draw(ax=ax, data=data, **kwargs)

        # Apply tick labels after base class formatting
        ax.set_xticks(range(len(data.columns)))
        ax.set_xticklabels(data.columns, rotation=45, ha="right")
        ax.set_yticks(range(len(data.index)))
        ax.set_yticklabels(data.index)