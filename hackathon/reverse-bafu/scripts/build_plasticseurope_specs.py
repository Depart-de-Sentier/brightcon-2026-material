"""Write the S2/S3 specs for the PlasticsEurope family of BAFU-2026 (their starting amounts).

Run:  uv run python scripts/build_plasticseurope_specs.py [--force]

The committed specs were written by this script and then resolved and calibrated by
``reverse-bafu run-all --apply``, which wrote codes and fitted amounts into them. Re-running the
script therefore skips every spec that already exists; ``--force`` overwrites them with the
starting values (run ``run-all --apply`` again afterwards).

Why a script and not 11 JSON files typed out: every amount in these specs is derived from one of a
small number of quoted lines (a stoichiometric equation, a yield range, an allocation factor, the
ecoinvent standard transport distances), and the derivation has to stay visible next to the number.
The script is the derivation; the JSON it writes carries the quote in every ``note``.

Nothing here reads the target's own flow vector. What the specs take from BAFU-2026 itself is
structure from *other* datasets used as named templates (Diethylene glycol, PET amorphous,
Emulsion polymerisation) - never the target.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

OUT = Path("specs")

# ecoinvent v2 standard transport, per kg of *precursor material*, as used by every chemicals
# dataset BAFU carries that was built this way (Ethylene dichloride 0.6/0.1 per 1.03 kg of
# precursor, Ethylene oxide 0.541/0.105 per 0.825 kg, Ethyl benzene 0.619/0.103 per 1.03 kg,
# PET granulate amorphous 0.743/0.124 per 1.209 kg). Source of the convention: Althaus 2007
# sec. 34.6.7 / 35.6.7, "standard distances and means according to Frischknecht et al. (2007)".
RAIL, LORRY = 0.6, 0.1
TRANSPORT_NOTE = ("The dataset's own text names 'transportation of feedstock' but no report in the bundle gives a "
                  "distance for it, so the amount is calibrated. The starting value is the ecoinvent v2 standard "
                  "distance for precursor materials (Althaus 2007 sec. 34.6.7: 'As there is no information about the "
                  "transport amounts, standard distances and means according to Frischknecht et al. (2007) are used "
                  "for the different raw materials') = {rail} tkm rail + {lorry} tkm lorry per kg of precursor, the "
                  "ratio BAFU's Ethylene dichloride, Ethylene oxide, Ethyl benzene and PET-amorphous unit processes "
                  "all carry; precursor mass here {mass:.4g} kg. It is left free rather than fixed because the "
                  "PlasticsEurope eco-profile accounts for its feedstock transport as elementary flows only - it "
                  "carries no vehicle or track infrastructure - so an ecoinvent transport dataset adds a background "
                  "the target cannot have, and the fit is the right place to decide how much of it belongs.")

CHEM_PLANT_NOTE = (
    "Rajabihamedani 2025 sec. 3.6: 'For the implementation, the dataset \"Chemical plant, organics {RER}U\" is used. "
    "The quantity is the standard amount for production of chemicals of 4.0E-10 p.' The target carries exactly that, "
    "which is why 4.0E-10 is the upper bound here. It is the upper bound and not the amount because ESU added one "
    "chemical plant per *dataset*, i.e. one for a whole cradle-to-gate chain, while this model links to a precursor "
    "dataset that already carries its own 4.0E-10 - so a second one is a double count against the target's own "
    "convention. That matters more than its size suggests: of the 1790 flows in the cumulative vector of every one "
    "of these 14 datasets, 1316 get more than 90 % of their value from this single exchange (see "
    "scripts/plasticseurope_infrastructure_diagnostic.py), so doubling it doubles three quarters of the vector. "
    "The amount is therefore fitted between 0 and the report's 4.0E-10.")

NO_WASTE_NOTE = (
    "The waste-treatment services that the BAFU dataset already carries as explicit exchanges (Tab. 3.1 of "
    "Rajabihamedani 2025 documents how they were re-linked, but prints no amounts) are deliberately NOT part "
    "of this model: they were never collapsed away, so reconstructing them adds nothing, and copying their "
    "amounts out of the target would be reading the answer. Adding the whole Tab. 3.1 candidate list as free "
    "inputs was tested on Ethylene glycol - the fit drove all eleven to ~1e-12 and the agreement did not move "
    "by a single flow - so they are left out. Consequence for the harness number: the target's cumulative "
    "vector gets its long tail of trace flows from those disposal chains, while this model gets a different "
    "tail from the ecoinvent-v2 chains of its own inputs; the two tails cannot agree, which caps the "
    "'share of all flows within 10 %' far below what the main flows achieve.")

AGG_DEP_NOTE = (
    "This model terminates on {dep}, which is itself an ecoSpold type=2 dataset - the harness flags that, "
    "correctly. It is linked to the BAFU dataset rather than to the sibling rebuild so that this spec's "
    "check measures only this spec's evidence; re-point it with the input's `sandbox` field to chain the "
    "rebuilds together.")


def chem_plant():
    return {"name": "Chemical plant, organics", "amount": 4.0e-10, "unit": "unit", "location": "RER",
            "free": True, "bounds": [0.0, 4.0e-10], "note": CHEM_PLANT_NOTE}


def transports(mass: float):
    n = TRANSPORT_NOTE.format(rail=RAIL, lorry=LORRY, mass=mass)
    return [
        {"name": "Transport, freight, rail", "amount": RAIL * mass, "unit": "ton kilometer",
         "location": "RER", "free": True, "note": n},
        {"name": "Transport, freight, lorry, fleet average", "amount": LORRY * mass,
         "unit": "ton kilometer", "location": "RER", "free": True, "note": n},
    ]


def free(name, unit, location, note, start=0.1, bounds=None):
    d = {"name": name, "amount": start, "unit": unit, "location": location, "free": True, "note": note}
    if bounds:
        d["bounds"] = list(bounds)
    return d


def write(code, slug, spec):
    p = OUT / f"{code[:8]}-{slug}.json"
    if p.exists() and "--force" not in sys.argv:
        print("exists, kept", p)
        return
    p.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n")
    print("wrote", p)


# --- molar masses (IUPAC standard atomic weights; physical constants, not modelling choices) ----
M = {"C2H4": 28.054, "Cl2": 70.906, "C2H3Cl": 62.498, "C8H10": 106.165, "C8H6O4": 166.131}

EVID_LOCATE = {
    "source": "2025 - LCI plastics - Rajabihamedani.pdf (the dataset's own cited report)",
    "where": "sec. 3.2, Tab. 1.1, sec. 6",
    "note": ("Prints no unit-process inventory for any of its 14 datasets: 'All datasets addressed for the "
             "updates are nowadays only available as system processes and therefore are modelled accordingly "
             "in this study' (sec. 3.2); Foreground data = 'Cumulative inventories of Plastics as provided by "
             "PlasticsEurope' (Tab. 1.1). Verified page by page, including every table that is embedded as an "
             "image. The full finding is in specs/evidence/<code>/response-0-locate.json. What the report does "
             "give and is used here: sec. 3.6 (infrastructure, 4.0E-10 p of Chemical plant, organics).")}


def eco_spold(text, field="technology"):
    return {"source": f"bafu-2026 ecoSpold metadata of the target ({field})", "where": field, "note": text}


# =====================================================================================
# Vinyl chloride, at plant  (S3: balanced VCM stoichiometry + the target's own process text)
# =====================================================================================
eth_vcm = M["C2H4"] / M["C2H3Cl"] / 0.97          # 0.97 = midpoint of the 96-98 % yield on ethylene
cl_vcm = (M["Cl2"] / 2) / M["C2H3Cl"] / 0.98      # 0.98 = yield on chlorine
prec_vcm = eth_vcm + cl_vcm
write("99a93e93-a8a8-34f3-88f3-6af0c21c4762", "vinyl-chloride-at-plant", {
 "target": {"code": "99a93e93-a8a8-34f3-88f3-6af0c21c4762", "name": "Vinyl chloride, at plant", "location": "RER"},
 "strategy": {"code": "S3",
   "label": "top-down model: the balanced VCM process, input list from the dataset's own process description, amounts from the reaction stoichiometry, energy calibrated",
   "note": ("NOT S1. The cited report prints no inventory (see the evidence block). The input list is the one the "
            "BAFU dataset itself states - 'The VCM production process, upstream processes like ethylene and chlorine "
            "production, electricity, and steam production as well as transportation of feedstock and waste treatment' "
            "- and the two material amounts follow from the balanced-process equations printed in Althaus 2007 sec. "
            "34.5.3 with the yields of sec. 34.5.1. Electricity and steam are named by the dataset and quantified "
            "nowhere in the bundle, so they are fitted, unbounded. No direct process emissions are modelled: the only "
            "VCM emission factors in the bundle (Althaus Tab. 34.1) are for EDC, not for the cracking step.")},
 "evidence": [
   EVID_LOCATE,
   eco_spold("'The VCM production process, upstream processes like ethylene and chlorine production, electricity, "
             "and steam production as well as transportation of feedstock and waste treatment.' - this is the whole "
             "input list the dataset declares, and it is what the model contains.", "includedProcesses / technology"),
   {"source": "2007 - LCI chemicals - Althaus.pdf", "where": "sec. 34.5.3 Thermal cracking of EDC",
    "note": ("'C2H4 + Cl2 -> C2H4Cl2 (Chlorination of ethylene to EDC) / C2H4Cl -> CH2CHCl + HCl (Cracking of EDC to "
             "form VCM) / C2H4 + 1/2 O2 + 2HCl -> C2H4Cl2 + H2O (Oxychlorination route to EDC)'. 'Often all the HCl "
             "generated in the cracking section is reused in producing EDC by oxychlorination. Plants that exhibit "
             "this characteristic and also do not export EDC are called “balanced”. The balanced process is the "
             "common process used as a Best Available Technology benchmark.' Summing the three gives the balanced "
             "overall reaction 2 C2H4 + Cl2 + 1/2 O2 -> 2 C2H3Cl + H2O, in which the HCl cancels - which is why VCM "
             "is modelled here from ethylene and chlorine directly and not from 1.583 kg of EDC (that route would "
             "double-count the chlorine, because half of it comes back as HCl).")},
   {"source": "2007 - LCI chemicals - Althaus.pdf", "where": "sec. 34.5.1 EDC by direct chlorination of ethylene",
    "note": "'Yield on ethylene 96-98% / on chlorine 98%' - the midpoint 97 % and the 98 % are applied to the stoichiometric amounts."},
   {"source": "bafu-2026: Ethylene dichloride, at plant [RER]", "where": "cross-check of the transport convention",
    "note": ("The one BAFU unit process for the same chemistry carries 0.6 tkm rail + 0.1 tkm lorry per kg, "
             "chlorine, liquid, production mix 0.735 kg and ethylene 0.295 kg - it reproduces Althaus Tab. 34.3 "
             "exactly, which is the check that this way of reading the report gives back the dataset it built.")}],
 "node": {
  "name": "Vinyl chloride, at plant, disaggregated", "unit": "kilogram", "location": "RER",
  "comment": ("Balanced EDC/VCM process, per kg of vinyl chloride monomer. " + NO_WASTE_NOTE + " " +
              AGG_DEP_NOTE.format(dep="Ethylene, average, at plant [RER]")),
  "inputs": [
   {"name": "Ethylene, average, at plant", "amount": eth_vcm, "unit": "kilogram", "location": "RER",
    "note": f"balanced reaction 2 C2H4 + Cl2 + 1/2 O2 -> 2 C2H3Cl + H2O: M(C2H4)/M(C2H3Cl) = {M['C2H4']}/{M['C2H3Cl']} = 0.4489 kg, / 0.97 yield on ethylene (Althaus sec. 34.5.1) = {eth_vcm:.4f} kg"},
   {"name": "Chlorine, liquid, production mix, at plant", "amount": cl_vcm, "unit": "kilogram", "location": "RER",
    "note": f"same reaction: 0.5*M(Cl2)/M(C2H3Cl) = {M['Cl2']/2}/{M['C2H3Cl']} = 0.5672 kg, / 0.98 yield on chlorine (Althaus sec. 34.5.1) = {cl_vcm:.4f} kg; the dataset BAFU's own Ethylene dichloride unit process uses"},
   free("Electricity, medium voltage, production ENTSO-E, at grid", "kilowatt hour", "ENTSO-E",
        "named by the dataset ('electricity ... production'), quantified nowhere in the bundle -> calibrated, unbounded"),
   free("Steam, for chemical processes, at plant", "kilogram", "RER",
        "named by the dataset ('steam production'), quantified nowhere in the bundle -> calibrated, unbounded; EDC cracking to VCM is strongly endothermic"),
   chem_plant(), *transports(prec_vcm)],
  "emissions": [], "resources": []}})


# =====================================================================================
# The addition polymers: HDPE, LDPE, LLDPE, PP, S-PVC   (S3, one shared shape)
# =====================================================================================
POLY_NOTE = ("NOT S1. The cited report prints no inventory. The input list is the one the BAFU dataset itself "
             "declares in its ecoSpold technology/includedProcesses field, and the monomer amount is a mass balance, "
             "not a measurement: addition (chain-growth) polymerisation adds the monomer to the chain unchanged, so "
             "the repeat unit and the monomer have the same empirical formula and 1 kg of polymer needs 1 kg of "
             "monomer plus whatever is lost. No loss figure exists anywhere in the bundle, so 1.000 kg is used and "
             "the real value can only be higher - this is the one place where the model is knowingly at a bound. "
             "Electricity and steam are named by the dataset and quantified nowhere, so they are fitted, unbounded; "
             "they are the whole gate-to-gate difference between the polymer and its monomer.")


def addition_polymer(code, slug, name, monomer, monomer_loc, tech_quote, dep_flag, ced_note,
                     extra_inputs=(), extra_note=""):
    write(code, slug, {
     "target": {"code": code, "name": name, "location": "RER"},
     "strategy": {"code": "S3",
       "label": "top-down model: monomer by mass balance, input list from the dataset's own process description, energy calibrated",
       "note": POLY_NOTE + (" " + extra_note if extra_note else "")},
     "evidence": [EVID_LOCATE,
       eco_spold(tech_quote, "includedProcesses / technology"),
       {"source": "2025 - LCI plastics - Rajabihamedani.pdf", "where": "Tab. 5.3 (cross-check only, not used for any amount)",
        "note": ced_note + " Quoted as a sanity check on the fitted electricity and steam, and deliberately not used "
                "to set or bound them: it is an impact result, and no impact assessment enters this pipeline."}],
     "node": {
      "name": f"{name}, disaggregated", "unit": "kilogram", "location": "RER",
      "comment": (f"Polymerisation step, per kg of granulate. " + NO_WASTE_NOTE +
                  (" " + AGG_DEP_NOTE.format(dep=dep_flag) if dep_flag else "")),
      "inputs": [
       {"name": monomer, "amount": 1.0, "unit": "kilogram", "location": monomer_loc,
        "note": ("mass balance of chain-growth polymerisation: the repeat unit is the monomer, so 1 kg of polymer "
                 "carries 1 kg of monomer; no conversion-loss figure is printed in any report of the bundle, so "
                 "this is a lower bound, fixed (not fitted)")},
       free("Electricity, medium voltage, production ENTSO-E, at grid", "kilowatt hour", "ENTSO-E",
            "named by the dataset ('electricity ... production'), quantified nowhere in the bundle -> calibrated, unbounded"),
       free("Steam, for chemical processes, at plant", "kilogram", "RER",
            "named by the dataset ('steam production'), quantified nowhere in the bundle -> calibrated, unbounded"),
       *extra_inputs, chem_plant(), *transports(1.0)],
      "emissions": [], "resources": []}})


CED = {'hdpe': 'Cumulative energy demand, this study: HDPE 77.38 MJ/kg against Ethylene, average 70.73 MJ/kg, so the whole gate-to-gate step the fit has to find is worth about 6.7 MJ/kg, under 9 % of the total.', 'ldpe': 'Cumulative energy demand, this study: LDPE 79.41 MJ/kg against Ethylene, average 70.73 MJ/kg - about 8.7 MJ/kg for the high-pressure polymerisation step, 11 % of the total.', 'lldpe': 'Cumulative energy demand, this study: LLDPE 76.95 MJ/kg against Ethylene, average 70.73 MJ/kg - about 6.2 MJ/kg, 8 % of the total.', 'pp': 'Cumulative energy demand, this study: Polypropylene 75.62 MJ/kg. Propylene is not one of the 14 datasets of the report, so Tab. 5.3 gives no monomer figure to subtract and there is no cross-check on the fitted process energy for this one.', 'spvc': 'Cumulative energy demand, this study: S-PVC 54.49 MJ/kg against Vinyl chloride 49.71 MJ/kg - about 4.8 MJ/kg for the suspension polymerisation step, 9 % of the total.'}

PE_QUOTE = ("'The polymer process, upstream processes like ethylene production, electricity, and steam production as "
            "well as transportation of feedstock and waste treatment.' - the whole input list the dataset declares.")
addition_polymer("6738f024-eb64-3ef8-837e-05b84c6e43da", "polyethylene-hdpe-granulate-at-plant",
                 "Polyethylene, HDPE, granulate, at plant", "Ethylene, average, at plant", "RER", PE_QUOTE,
                 "Ethylene, average, at plant [RER]", CED["hdpe"],
                 extra_note=("HDPE is made by low-pressure catalytic polymerisation, LDPE by the high-pressure radical "
                             "route and LLDPE by low-pressure copolymerisation with an alpha-olefin. The bundle "
                             "documents none of that quantitatively, so the three specs differ only in what the fit "
                             "puts into electricity and steam. The alpha-olefin comonomer of LLDPE (a few per cent of "
                             "1-butene/1-hexene) is a known gap: no dataset for it is named anywhere and folding it "
                             "into the ethylene is the standard simplification."))
addition_polymer("c4dbbb99-22d0-37c1-8cc7-fc5a8c64329b", "polyethylene-ldpe-granulate-at-plant",
                 "Polyethylene, LDPE, granulate, at plant", "Ethylene, average, at plant", "RER", PE_QUOTE,
                 "Ethylene, average, at plant [RER]", CED["ldpe"])
addition_polymer("df878822-0deb-3a59-a6b4-396d94a3b654", "polyethylene-lldpe-granulate-at-plant",
                 "Polyethylene, LLDPE, granulate, at plant", "Ethylene, average, at plant", "RER", PE_QUOTE,
                 "Ethylene, average, at plant [RER]", CED["lldpe"],
                 extra_note="The alpha-olefin comonomer (typically a few per cent of 1-butene or 1-hexene) is a gap: no comonomer is named in the dataset's own text and no dataset for one is identified, so it is carried inside the ethylene.")
addition_polymer("09cda8b1-b652-39b2-8761-c93aecc29f70", "polypropylene-granulate-at-plant",
                 "Polypropylene, granulate, at plant", "Propylene, at plant", "RER",
                 "'The polymer process, upstream processes like propylene production, electricity, and steam "
                 "production as well as transportation of feedstock and waste treatment.'", "", CED["pp"],
                 extra_note=("'Propylene, at plant [RER]' is not one of the 101, so the harness does not flag it, but "
                             "it is not a transparent unit process either: it carries 8 technosphere exchanges, all "
                             "of them waste-treatment services, and 143 elementary flows - the same APME/PlasticsEurope "
                             "shape as the datasets being rebuilt here. The chain therefore still terminates on "
                             "aggregated data one level down, and saying so is part of the result."))
addition_polymer("48985f3e-97b4-3128-a1a8-a5ba91a1cb88", "polyvinylchloride-suspension-polymerised-at-plant",
                 "Polyvinylchloride, suspension polymerised, at plant", "Vinyl chloride, at plant", "RER",
                 "'The polymerisation process, upstream processes like ethylene, chlorine, and VCM production, "
                 "electricity, and steam production as well as transportation of feedstock and waste treatment.'",
                 "Vinyl chloride, at plant [RER]", CED["spvc"],
                 extra_note=("Suspension polymerisation is carried out in an aqueous phase with a suspension "
                             "stabiliser, and both the water and the stabiliser are gaps here: the dataset's own text "
                             "names neither, and nothing in the bundle quantifies them. Only the monomer, the energy "
                             "and the transport are modelled. Re-point the monomer to 99a93e93-...-disagg with the "
                             "input's `sandbox` field to chain this onto the VCM rebuild."))


# =====================================================================================
# PVC, emulsion polymerised  (S3 + a named BAFU template for the utility side)
# =====================================================================================
EMUL = {  # BAFU-2026 'Emulsion polymerisation, polyvinylchlorid' [RER], per kg
 "Nitrogen, liquid, at plant": (0.00125, "kilogram", "RER"),
 "Compressed air, average installation, >30kW, 8 bar gauge, at supply network": (1.732, "cubic meter", "RER"),
 "Tap water, at user": (2.475, "kilogram", "RER"),
 "Natural gas, burned in industrial furnace 1MWth": (0.885, "megajoule", "CH"),
 "Steam, for chemical processes, at plant": (1.395, "kilogram", "RER"),
 "Electricity, medium voltage, production ENTSO-E, at grid": (0.3764, "kilowatt hour", "ENTSO-E"),
 "Chemicals organic, at plant": (0.025, "kilogram", "GLO"),
 "Treatment, sewage, unpolluted, to wastewater treatment, class 3": (0.002475, "cubic meter", "CH"),
}
write("015cd7db-8a64-3f0b-ba15-6ff81e3d1eb4", "polyvinylchloride-emulsion-polymerised-at-plant", {
 "target": {"code": "015cd7db-8a64-3f0b-ba15-6ff81e3d1eb4", "name": "Polyvinylchloride, emulsion polymerised, at plant", "location": "RER"},
 "strategy": {"code": "S3",
   "label": "top-down model: monomer by mass balance, utility side from BAFU's own emulsion-polymerisation module, amounts calibrated within 0.5-2x of it",
   "note": ("NOT S1. The cited report prints no inventory. The monomer is a mass balance (1 kg of PVC carries 1 kg of "
            "vinyl chloride; chain-growth polymerisation adds the monomer unchanged). The utility side - nitrogen "
            "blanketing, compressed air, process water, furnace gas, steam, electricity, auxiliary organics and the "
            "treatment of the unpolluted process water - is the input list of BAFU's own unit process 'Emulsion "
            "polymerisation, polyvinylchlorid' [RER], with its amounts as the centre of 0.5-2x bounds. Caveat, stated "
            "rather than hidden: that module is generic. Its one consumer in BAFU-2026 is 'Polyvinylalcohol, at "
            "plant' (1.94 kg of it), and its monomer slot is filled with 1.355 kg of dichloromethane, which is not a "
            "PVC reagent. Only its utility rows are used here; the monomer slot is replaced by vinyl chloride. That "
            "is why this is S3 with a template for the utilities, not S2.")},
 "evidence": [EVID_LOCATE,
   eco_spold("'The polymerisation process, upstream processes like ethylene, chlorine, and VCM production, "
             "electricity, and steam production as well as transportation of feedstock and waste treatment.'",
             "includedProcesses / technology"),
   {"source": "bafu-2026: Emulsion polymerisation, polyvinylchlorid [RER] (unit process, 9 inputs)",
    "where": "template for the utility side only",
    "note": ("Per kg: nitrogen, liquid 0.00125 kg; compressed air >30kW 8 bar 1.732 m3; tap water 2.475 kg; natural "
             "gas burned in industrial furnace 1MWth 0.885 MJ; steam for chemical processes 1.395 kg; electricity "
             "medium voltage 0.3764 kWh; chemicals organic 0.025 kg; treatment, sewage, unpolluted class 3 0.002475 "
             "m3; dichloromethane 1.355 kg (the monomer slot, not used); direct flows Water To Cooling 0.03139 m3 and "
             "Water to water 0.02982 m3.")}],
 "node": {
  "name": "Polyvinylchloride, emulsion polymerised, at plant, disaggregated", "unit": "kilogram", "location": "RER",
  "comment": ("Emulsion polymerisation of VCM, per kg of E-PVC. " + NO_WASTE_NOTE + " " +
              AGG_DEP_NOTE.format(dep="Vinyl chloride, at plant [RER]")),
  "inputs": [
   {"name": "Vinyl chloride, at plant", "amount": 1.0, "unit": "kilogram", "location": "RER",
    "note": "mass balance of chain-growth polymerisation, as for the other polymers; replaces the template's 1.355 kg dichloromethane monomer slot"},
   *[free(n, u, loc, f"BAFU 'Emulsion polymerisation, polyvinylchlorid' = {a:g} {u}; calibrated within 0.5-2x of the template (the same bound convention as the committed gypsum-fibre-board S2 spec)",
          start=a, bounds=(0.5 * a, 2.0 * a)) for n, (a, u, loc) in EMUL.items()],
   chem_plant(), *transports(1.0)],
  "emissions": [
   {"name": "Water", "category": "water", "amount": 0.02982, "unit": "cubic meter",
    "note": "template direct flow: 0.02982 m3 to water"}],
  "resources": [
   {"name": "Water To Cooling", "category": "resources", "amount": 0.03139, "unit": "cubic meter",
    "note": "template direct flow: 0.03139 m3 cooling water"}]}})


# =====================================================================================
# Polystyrene, expandable  (S3 from the dataset's own, unusually detailed process text)
# =====================================================================================
write("05a10e4b-a919-33b6-b017-7c0bf7f7a7f9", "polystyrene-expandable-at-plant", {
 "target": {"code": "05a10e4b-a919-33b6-b017-7c0bf7f7a7f9", "name": "Polystyrene, expandable, at plant", "location": "RER"},
 "strategy": {"code": "S3",
   "label": "top-down model from the dataset's own process description: styrene by mass balance, blowing agent and utilities calibrated",
   "note": ("NOT S1. The cited report prints no inventory; what it says about EPS is an error correction (sec. 3.8, "
            "the rejected 28.5 kg of natural gas per kg). The input list here comes from the dataset's own ecoSpold "
            "technology field, which for EPS is unusually explicit and names, in order: styrene monomer, organic "
            "peroxide initiators, an aqueous phase, flame retardant and elemental carbon, suspension stabilisers, "
            "chain transfer agents, expanding aids, nucleating agents, plasticisers, pentane as the blowing agent, "
            "heating to 80-150 C, a centrifuge, drying and sieving, and a coating step. Amounts for none of them are "
            "printed anywhere in the bundle, so styrene is fixed by mass balance and everything else is fitted. The "
            "flame retardant and the elemental carbon of grey EPS are left out on purpose: no dataset is named for "
            "either and proposing one would be guessing - see gaps in the comment.")},
 "evidence": [EVID_LOCATE,
   eco_spold("'Expandable Polystyrene (EPS) is produced by polymerisation of styrene monomer, a chain-growth reaction "
             "which is mostly initiated by free radical organic initiators. ... Styrene charged with organic peroxide "
             "initiators is added to an aqueous phase and forms a suspension upon stirring. Flame retardant and "
             "elemental carbon, as well as auxiliaries such as suspension stabilisers, chain transfer agents, "
             "expanding aids, nucleating agents and plasticisers can also be added. The styrene droplets polymerise "
             "to polystyrene during heating of the reactor between 80 and 150 C. Blowing agent, typically pentane, is "
             "added to the reactor during polymerisation and dissolves in the polymer, producing the Expandable "
             "Polystyrene bead. After the reactor is cooled, the polymer is separated from the water phase using a "
             "centrifuge. The EPS beads are dried and sieved into the required size fractions before being coated "
             "with additive'", "technology"),
   {"source": "2025 - LCI plastics - Rajabihamedani.pdf", "where": "sec. 3.8 Obvious errors corrected in PE data",
    "note": ("'According to the latest PlasticsEurope data, methane emissions were first estimated for Polystyrene "
             "expandable seven times higher (0.226 kg vs. 0.031 kg) than previously estimated in UVEK 2025. This "
             "discrepancy is largely due to the significant consumption of natural gas - 28.5 kg - required to "
             "produce just 1 kg of polystyrene. Since such a high input is unrealistic a correction has been made.' "
             "A rejected figure, so it cannot be used as an amount; it is recorded because it is the only "
             "process-energy number the report ever prints for this dataset, and because it means the published "
             "vector for EPS carries a hand-made correction of unstated size.")}],
 "node": {
  "name": "Polystyrene, expandable, at plant, disaggregated", "unit": "kilogram", "location": "RER",
  "comment": ("Suspension polymerisation of styrene with a pentane blowing agent, per kg of EPS beads. "
              "Gaps: the flame retardant, the elemental carbon of grey EPS (4 of the 14 plants behind the eco-profile), "
              "the peroxide initiator and the bead coating are named by the dataset and modelled only through the "
              "generic 'Chemicals organic, at plant'. Note also that the target carries 1.435 kg of 'Disposal, salt tailings potash mining, 0% water, to "
              "residual material landfill {CH}' per kg of EPS. Tab. 3.1 of the cited report (p. 11 of the PDF, the "
              "continuation page that pdftotext returns empty because the table is an image) shows where that comes "
              "from: 'tailings (deposited)', 'Overburden (deposited)' and 'Waste salt from KCl-production (wfr)' are "
              "all mapped to that one potash-tailings *treatment* dataset. Mining overburden routed through a "
              "waste-treatment chain is what gives the EPS target its three largest kilogram flows - 30.6 kg of waste "
              "water to river, 18.3 kg of air and 1.44 kg of basalt per kg of polystyrene - and it is why this "
              "dataset's kg-mass and top-50 scores cannot be met by any model of the polymerisation. Nothing in this "
              "model reproduces it, and nothing should. " + NO_WASTE_NOTE),
  "inputs": [
   {"name": "Styrene, at plant", "amount": 1.0, "unit": "kilogram", "location": "RER",
    "note": ("mass balance of chain-growth polymerisation. EPS also contains the dissolved pentane, so the true "
             "styrene content is a few per cent below 1 kg; no percentage is printed anywhere in the bundle, so "
             "1.000 kg is kept and the model is knowingly a little heavy on styrene")},
   free("Pentane, at plant", "kilogram", "RER",
        "'Blowing agent, typically pentane, is added to the reactor during polymerisation and dissolves in the polymer' - named, never quantified -> calibrated, unbounded",
        start=0.05),
   free("Tap water, at user", "kilogram", "RER", "'added to an aqueous phase and forms a suspension upon stirring' - named, never quantified -> calibrated, unbounded", start=2.0),
   free("Chemicals organic, at plant", "kilogram", "GLO",
        "stands for the named auxiliaries as a group (peroxide initiators, suspension stabilisers, chain transfer agents, expanding aids, nucleating agents, plasticisers, bead coating); none is quantified -> calibrated, unbounded", start=0.02),
   free("Electricity, medium voltage, production ENTSO-E, at grid", "kilowatt hour", "ENTSO-E", "stirring, centrifuge, sieving, conveying; never quantified -> calibrated, unbounded"),
   free("Steam, for chemical processes, at plant", "kilogram", "RER", "'heating of the reactor between 80 and 150 C' and the drying step; never quantified -> calibrated, unbounded", start=1.0),
   chem_plant(), *transports(1.0)],
  "emissions": [], "resources": []}})


# =====================================================================================
# PET, granulate, bottle grade  (S2 from BAFU's own PET-amorphous unit process)
# =====================================================================================
PETT_FIXED = [  # (name, amount, unit, location, note-tail)
 ("Purified terephthalic acid, at plant", 0.875, "kilogram", "RER",
  "template; cross-check against the esterification stoichiometry 2 PTA + 2 MEG -> PET repeat unit + 2 H2O: "
  "M(C8H6O4)/M(C10H8O4) = 166.131/192.17 = 0.8645 kg is the theoretical minimum, so the template's 0.875 kg is 1.2 % above it"),
 ("Ethylene glycol, at plant", 0.334, "kilogram", "RER",
  "template; the same stoichiometry gives M(C2H6O2)/M(C10H8O4) = 62.068/192.17 = 0.3230 kg as the minimum, "
  "so the template's 0.334 kg is 3.4 % above it"),
 ("Nitrogen, liquid, at plant", 0.0298, "kilogram", "RER", "template (inert blanketing of the melt)"),
]
PETT_FREE = [
 ("Steam, for chemical processes, at plant", 0.94, "kilogram", "RER"),
 ("Electricity, medium voltage, production ENTSO-E, at grid", 0.194, "kilowatt hour", "ENTSO-E"),
 ("Heat, natural gas, at industrial furnace 1MW", 0.665, "megajoule", "CH"),
 ("Heat, heavy fuel oil, at industrial furnace 1MW", 0.494, "megajoule", "RER"),
 ("Heat, at hard coal industrial furnace 1-10MW", 0.306, "megajoule", "RER"),
 ("Heat, light fuel oil, at industrial furnace 1MW", 0.165, "megajoule", "RER"),
]
PETT_BIO = [
 ("Non-methane Volatile Organic Compounds", 9e-05, "kilogram", "air"),
 ("Particles (> PM10)", 3.2e-07, "kilogram", "air"),
 ("Particles (PM2.5)", 2.5e-07, "kilogram", "air"),
 ("Particles (PM10)", 4.3e-07, "kilogram", "air"),
 ("Waste Heat", 0.7, "megajoule", "air"),
 ("Suspended Solids, Unspecified", 1e-06, "kilogram", "water"),
 ("Biological Oxygen Demand", 0.00016, "kilogram", "water"),
 ("Chemical Oxygen Demand", 0.00102, "kilogram", "water"),
 ("Total Organic Carbon", 0.000262, "kilogram", "water"),
 ("DOC, Dissolved Organic Carbon", 0.000262, "kilogram", "water"),
 ("Oils, Unspecified", 0.000499, "kilogram", "water"),
 ("Water", 0.0062348, "cubic meter", "water"),
]
write("c7af8832-9551-38fd-a628-363e6fc17c8e", "polyethylene-terephthalate-granulate-bottle-grade-at-plant", {
 "target": {"code": "c7af8832-9551-38fd-a628-363e6fc17c8e", "name": "Polyethylene terephthalate, granulate, bottle grade, at plant", "location": "RER"},
 "strategy": {"code": "S2",
   "label": "template transfer from BAFU's own PET-granulate-amorphous unit process, the six energy inputs calibrated within 0.5-2x",
   "note": ("The cited report prints no inventory. BAFU-2026 does carry a 16-input unit process for the same polymer "
            "in its other grade - 'Polyethylene terephthalate, granulate, amorphous, at plant' [RER] - and the target "
            "declares exactly that structure: 'The polymer process, upstream processes like pX, PTA, and MEG "
            "production, electricity, and steam production as well as transportation of feedstock and waste "
            "treatment.' Bottle grade differs from amorphous by a solid-state polycondensation step, which is extra "
            "heat and residence time and no extra material; the six energy inputs are therefore free within 0.5-2x of "
            "the template (the bound convention of the committed gypsum-fibre-board S2 spec) and the three material "
            "inputs are fixed. This is the best-evidenced of the family after ethylene glycol, and it is the only one "
            "of the fourteen whose direct process emissions are known at all - they come with the template.")},
 "evidence": [EVID_LOCATE,
   eco_spold("'The polymer process, upstream processes like pX, PTA, and MEG production, electricity, and steam "
             "production as well as transportation of feedstock and waste treatment.'", "includedProcesses"),
   {"source": "bafu-2026: Polyethylene terephthalate, granulate, amorphous, at plant [RER] (unit process, 16 inputs, 15 direct flows)",
    "where": "template transfer (S2)",
    "note": ("Per kg: purified terephthalic acid 0.875 kg, ethylene glycol 0.334 kg, nitrogen liquid 0.0298 kg, "
             "steam 0.94 kg, electricity 0.194 kWh, heat natural gas 0.665 MJ, heat heavy fuel oil 0.494 MJ, heat "
             "hard coal 0.306 MJ, heat light fuel oil 0.165 MJ, chemical plant organics 4.0E-10 unit, transport rail "
             "0.743 tkm + lorry 0.124 tkm, four disposal services, and 15 direct elementary flows. The four disposal "
             "services are dropped here: the bottle-grade target declares no waste-treatment exchanges at all (its "
             "only technosphere exchange is the 4.0E-10 chemical plant), so copying them in would add a chain the "
             "dataset does not have.")},
   {"source": "stoichiometry of the PET esterification", "where": "cross-check of the two material amounts",
    "note": ("n HOOC-C6H4-COOH + n HO-C2H4-OH -> [-OC-C6H4-CO-O-C2H4-O-]n + 2n H2O. Per kg of repeat unit "
             "(M = 192.17): PTA 166.131/192.17 = 0.8645 kg, MEG 62.068/192.17 = 0.3230 kg. The template sits 1.2 % "
             "and 3.4 % above those minima, which is the expected order for process losses - the template is "
             "consistent with the chemistry, which is why both are kept fixed rather than fitted.")}],
 "node": {
  "name": "Polyethylene terephthalate, granulate, bottle grade, at plant, disaggregated", "unit": "kilogram", "location": "RER",
  "comment": ("Esterification/polycondensation of PTA and MEG plus the solid-state step, per kg of bottle-grade "
              "granulate. " + NO_WASTE_NOTE + " " +
              AGG_DEP_NOTE.format(dep="Purified terephthalic acid, at plant [RER] and Ethylene glycol, at plant [RER], both of them among the 101")),
  "inputs": [
   *[{"name": n, "amount": a, "unit": u, "location": loc, "note": note} for n, a, u, loc, note in PETT_FIXED],
   *[free(n, u, loc, f"template {a:g} {u}; bottle grade adds solid-state polycondensation, so the energy inputs are calibrated within 0.5-2x of the amorphous template",
          start=a, bounds=(0.5 * a, 2.0 * a)) for n, a, u, loc in PETT_FREE],
   chem_plant(),
   free("Transport, freight, rail", "ton kilometer", "RER", "template 0.743 tkm; left free for the same reason as in the rest of this family - the PlasticsEurope vector carries feedstock transport as elementary flows with no vehicle or track background", start=0.743),
   free("Transport, freight, lorry, fleet average", "ton kilometer", "RER", "template 0.124 tkm; left free, see the rail note", start=0.124)],
  "emissions": [{"name": n, "category": c, "amount": a, "unit": u, "note": "template direct flow"}
                for n, a, u, c in PETT_BIO],
  "resources": [{"name": "Water", "category": "resources", "amount": 0.000163, "unit": "cubic meter", "note": "template direct flow"},
                {"name": "Water To Cooling", "category": "resources", "amount": 0.0064, "unit": "cubic meter", "note": "template direct flow"}]}})


# =====================================================================================
# Purified terephthalic acid  (S3: p-xylene oxidation stoichiometry)
# =====================================================================================
px_pta = M["C8H10"] / M["C8H6O4"]
write("bfff239d-8ae3-3730-a048-dffb312515f3", "purified-terephthalic-acid-at-plant", {
 "target": {"code": "bfff239d-8ae3-3730-a048-dffb312515f3", "name": "Purified terephthalic acid, at plant", "location": "RER"},
 "strategy": {"code": "S3",
   "label": "top-down model: p-xylene by the oxidation stoichiometry from the dataset's own process description, energy calibrated",
   "note": ("NOT S1. The cited report prints no inventory and says of PTA only that a x1000 correction was applied to "
            "one land-occupation flow (sec. 3.8). The dataset's own includedProcesses field names the chemistry - "
            "'Crude terephthalic acid (CTA) is produced by oxidation of p-xylene. A subsequent purification step "
            "leads to purified terephthalic acid (PTA)' - and the feedstock amount follows from that reaction. Two "
            "honest weaknesses: (1) the amount is the theoretical minimum, because no yield is printed anywhere in "
            "the bundle, so the model is low on p-xylene by whatever the real loss is; (2) BAFU has only 'Xylene, at "
            "plant', the mixed-isomer dataset, not p-xylene, so the isomer separation - which Althaus 2007 sec. "
            "96.5.1 describes as crystallisation or molecular-sieve adsorption and does not quantify - is missing "
            "from the chain. The acetic acid solvent and the cobalt/manganese/bromide catalyst of the oxidation step "
            "are named by neither the dataset nor any report in the bundle and are left out rather than guessed.")},
 "evidence": [EVID_LOCATE,
   eco_spold("'Crude terephthalic acid (CTA) is produced by oxidation of p-xylene. A subsequent purification step "
             "leads to purified terephthalic acid (PTA). In addition to these foreground processes, the following "
             "processes in the supply chain are considered for this EPD: extraction and refinery of crude oil and "
             "natural gas, steam cracking of hydrocarbons (predominantly naphtha) into lower olefins and pygas, "
             "catalytic reforming of naphtha, and the extraction and production of p-xylene from both pygas and "
             "reformate (xylene loop).'", "includedProcesses"),
   {"source": "stoichiometry of the p-xylene oxidation", "where": "the one material amount",
    "note": (f"C8H10 + 3 O2 -> C8H6O4 + 2 H2O. Per kg of PTA: M(C8H10)/M(C8H6O4) = {M['C8H10']}/{M['C8H6O4']} = "
             f"{px_pta:.4f} kg of p-xylene. The oxygen is taken from air and is not an inventoried input, as in every "
             "air-oxidation process in BAFU (cf. Ethylene oxide, at plant, whose oxygen is a purchased pure-O2 input "
             "and is therefore listed there but not here).")},
   {"source": "2007 - LCI chemicals - Althaus.pdf", "where": "sec. 96.5.1 p-Xylene, o-Xylene",
    "note": ("Describes the isomer separation that this model cannot represent: 'Crystallization techniques take "
             "advantage of the spread of melting points ... p-Xylene can also be recovered using solid absorption of "
             "the molecular-sieve type.' No amounts are given for it anywhere.")}],
 "node": {
  "name": "Purified terephthalic acid, at plant, disaggregated", "unit": "kilogram", "location": "RER",
  "comment": ("Air oxidation of p-xylene to CTA plus purification to PTA, per kg. " + NO_WASTE_NOTE + " " +
              AGG_DEP_NOTE.format(dep="Xylene, at plant [RER]")),
  "inputs": [
   {"name": "Xylene, at plant", "amount": px_pta, "unit": "kilogram", "location": "RER",
    "note": f"C8H10 + 3 O2 -> C8H6O4 + 2 H2O: {M['C8H10']}/{M['C8H6O4']} = {px_pta:.4f} kg, the theoretical minimum (no yield printed in the bundle); mixed xylene stands in for p-xylene, see the strategy note"},
   free("Electricity, medium voltage, production ENTSO-E, at grid", "kilowatt hour", "ENTSO-E", "oxidation reactor agitation, air compression, crystallisation, centrifuges; never quantified -> calibrated, unbounded", start=0.3),
   free("Steam, for chemical processes, at plant", "kilogram", "RER", "the purification step is a high-pressure hydrogenation and recrystallisation; never quantified -> calibrated, unbounded", start=1.0),
   chem_plant(), *transports(px_pta)],
  "emissions": [], "resources": []}})


# =====================================================================================
# Xylene  (S3 from the BREF tables Althaus quotes, every bound printed in the report)
# =====================================================================================
# Tab. 96.1, per ton of feedstock: p-xylene 0.23-0.48 t and o-xylene 0-0.25 t
# -> 0.23-0.73 t of xylenes per t of feedstock -> 1.370-4.348 kg of feedstock per kg of xylene.
FS_LO, FS_HI = 1.0 / 0.73, 1.0 / 0.23
FS_MID = 2.0 / (0.23 + 0.73)          # the midpoint yield, used only as a starting value
PYGAS, REFORMATE = 0.14, 0.86         # the dataset's own EU27 route split
write("a29aa0d5-9e37-34d7-8868-8a4fff95350a", "xylene-at-plant", {
 "target": {"code": "a29aa0d5-9e37-34d7-8868-8a4fff95350a", "name": "Xylene, at plant", "location": "RER"},
 "strategy": {"code": "S3",
   "label": "top-down model: BREF ranges for a reformate xylene plant, feedstock split from the dataset's own text, every free amount bounded by a printed range",
   "note": ("NOT S1. The cited report prints no inventory. Althaus 2007 ch. 96 is about this very dataset name, but "
            "its inventory tables 96.5-96.7 are the *cumulative* vector of the PlasticsEurope module - the report "
            "says so: 'Due to the fact that this dataset is cumulated it was not possible to use the other processes "
            "modelled in ecoinvent to obtain a transparent process chain' - so they are the aggregate this project is "
            "trying to open, not a unit process. What ch. 96 does print, from the EU BREF (European Commission 2002), "
            "is a gate-to-gate picture of a reformate xylene plant as ranges: Tab. 96.1 consumptions and yields, Tab. "
            "96.2 air emissions, Tab. 96.3 wastewater, Tab. 96.4 solid wastes. That is what is modelled here. Every "
            "free amount carries bounds taken straight from those printed ranges - none of them was chosen to make "
            "the agreement look better, and the feedstock bounds in particular are very wide (1.37-4.35 kg per kg) "
            "because the printed yield range is. Same caveat as Althaus's own: 'Within the module assessed here there "
            "are only the resources and emissions considered which are given in the data source. Therefore no land "
            "use could be included and no direct soil emissions within the process chain are stated.'")},
 "evidence": [EVID_LOCATE,
   eco_spold("'Xylenes are commercially produced based on two different feedstocks: - Pyrolysis gasoline, a side "
             "product of thermal cracking (steam cracking) of hydrocarbons (e.g. naphtha, gas oil, ethane, propane, "
             "butanes, natural gas liquids) - Reformate, a product of catalytic reforming of naphtha. ... In Europe "
             "(EU27) xylenes are mainly produced via pyrolysis gasoline (14 %) and reformate (86 %).' The 14/86 split "
             "is the only quantitative statement about this dataset anywhere, and it fixes the feedstock mix.", "technology"),
   {"source": "2007 - LCI chemicals - Althaus.pdf", "where": "Tab. 96.1 (printed p. 854, PDF p. 935)",
    "note": ("'Energy usage for and precursor materials for xylene production (European Commission (2002))', column "
             "'Reformate plant', per ton of feedstock: Fuel gas 3 - 10 kg; Steam (tons) 0.5 - 1.5; Electricity (MWh) "
             "<0.07. Production (tons) per ton of feedstock: p-xylene 0.23 - 0.48; o-xylene 0 - 0.25. Summing the two "
             "product ranges gives 0.23 - 0.73 t of xylenes per t of feedstock, i.e. 1.370 - 4.348 kg of feedstock "
             "per kg of product, and every consumption range is multiplied by that to get a per-kg-of-product range.")},
   {"source": "2007 - LCI chemicals - Althaus.pdf", "where": "Tab. 96.2 and Tab. 96.3 (same page), row 'BTX from aromatic mixture (source: a single plant)'",
    "note": ("Air, kg/ton product: Methane 0.086; SO2 0.53; Particulates 0.008 kg/ton *feedstock*; VOC 0.03 toluene "
             "and 0.2 NMVOCtot. Water, kg/ton product: Benzene 0.003; Toluene 0.001; COD 0.087; N-Kjeldahl 0.0009. "
             "Two rows are not used: the particulates, because they are per ton of feedstock and the feedstock amount "
             "here is itself calibrated, and the second 'Methane' column (0.09), because the table has two columns "
             "with that same header and the report gives no way to tell what the second one is. The caption reads "
             "'Air emissions for toluene production' inside the xylenes chapter, which is a copy-paste slip in the "
             "report; the rows are the BTX plant the chapter is about.")},
   {"source": "2007 - LCI chemicals - Althaus.pdf", "where": "Tab. 96.4 and sec. 96.5 Solid wastes",
    "note": ("kg/ton product: Catalysts 0.05 'recycled via supplier'; Clay, desiccant material, inert balls 0.006 "
             "'reused after regeneration'; Activated carbon 0.01 'incinerated'; Filter cloth etc. 0.0009 "
             "'incinerated'. The first two leave the system as recovered material and are skipped; the two "
             "incinerated streams are modelled together, since 'The wastes are usually recycled, landfilled or "
             "incinerated in a hazardous waste incinerator.'")}],
 "node": {
  "name": "Xylene, at plant, disaggregated", "unit": "kilogram", "location": "RER",
  "comment": ("Separation of mixed xylenes from reformate (86 %) and pyrolysis gasoline (14 %), per kg. "
              "Gaps: no reformate dataset exists in BAFU, so naphtha - the feed of the catalytic reformer - stands in "
              "for it and the reforming step itself is missing from the chain; particulate emissions are per ton of "
              "feedstock and cannot be fixed while the feedstock is calibrated; the isomer separation described in "
              "sec. 96.5.1 is not quantified anywhere. " + NO_WASTE_NOTE + " " +
              AGG_DEP_NOTE.format(dep="Pyrolysis gasoline, production mix, at plant [RER], itself one of the 101 and the one dataset of this family that could not be rebuilt at all")),
  "inputs": [
   free("Naphtha, at refinery", "kilogram", "RER",
        f"reformate route, {REFORMATE:.0%} of EU27 xylene (dataset text) x the feedstock range of Tab. 96.1 "
        f"(1.370-4.348 kg feedstock per kg product) = {REFORMATE*FS_LO:.4f}-{REFORMATE*FS_HI:.4f} kg; naphtha stands in for reformate, which BAFU does not have",
        start=REFORMATE * FS_MID, bounds=(REFORMATE * FS_LO, REFORMATE * FS_HI)),
   free("Pyrolysis gasoline, production mix, at plant", "kilogram", "RER",
        f"pygas route, {PYGAS:.0%} of EU27 xylene (dataset text) x the same feedstock range = {PYGAS*FS_LO:.4f}-{PYGAS*FS_HI:.4f} kg",
        start=PYGAS * FS_MID, bounds=(PYGAS * FS_LO, PYGAS * FS_HI)),
   free("Steam, for chemical processes, at plant", "kilogram", "RER",
        f"Tab. 96.1 'Steam (tons) 0.5 - 1.5' per ton of feedstock x the feedstock range = {0.5*FS_LO:.4f}-{1.5*FS_HI:.4f} kg per kg of product",
        start=1.0 * FS_MID, bounds=(0.5 * FS_LO, 1.5 * FS_HI)),
   free("Electricity, medium voltage, production ENTSO-E, at grid", "kilowatt hour", "ENTSO-E",
        f"Tab. 96.1 'Electricity (MWh) <0.07' per ton of feedstock = <0.07 kWh/kg feedstock x the feedstock range = 0-{0.07*FS_HI:.4f} kWh per kg of product",
        start=0.07 * FS_MID, bounds=(0.0, 0.07 * FS_HI)),
   free("Refinery gas, burned in furnace", "megajoule", "RER",
        "Tab. 96.1 'Fuel gas 3 - 10 kg' per ton of feedstock = 0.0041-0.0435 kg per kg of product. No heating value "
        "for refinery fuel gas is printed in any report of the bundle, so the mass range cannot be converted to the "
        "megajoules this dataset is measured in; rather than invent a heating value the amount is calibrated, "
        "unbounded, and the printed mass range is recorded here instead", start=0.5),
   {"name": "Disposal, hazardous waste, 25% water, to hazardous waste incineration", "amount": 1.09e-5,
    "unit": "kilogram", "location": "CH",
    "note": "Tab. 96.4: activated carbon 0.01 kg/ton product + filter cloth etc. 0.0009 kg/ton product, both marked 'incinerated' = 1.09E-05 kg/kg; catalysts (0.05, recycled via supplier) and clay/desiccant (0.006, reused after regeneration) are not disposal and are skipped"},
   chem_plant()],
  "emissions": [
   {"name": "Methane (fossil)", "category": "air", "amount": 8.6e-5, "unit": "kilogram", "note": "Tab. 96.2 'Methane' 0.086 kg/ton product"},
   {"name": "Sulfur Dioxide", "category": "air", "amount": 5.3e-4, "unit": "kilogram", "note": "Tab. 96.2 'SO2' 0.53 kg/ton product"},
   {"name": "Toluene", "category": "air", "amount": 3.0e-5, "unit": "kilogram", "note": "Tab. 96.2 'VOC * 0.03 toluene' kg/ton product; * = 'tanks and various fugitive sources'"},
   {"name": "Non-methane Volatile Organic Compounds", "category": "air", "amount": 2.0e-4, "unit": "kilogram", "note": "Tab. 96.2 'VOC * 0.2 NMVOCtot*' kg/ton product"},
   {"name": "Benzene", "category": "water", "amount": 3.0e-6, "unit": "kilogram", "note": "Tab. 96.3 'Benzene' 0.003 kg/ton product"},
   {"name": "Toluene", "category": "water", "amount": 1.0e-6, "unit": "kilogram", "note": "Tab. 96.3 'Toluene' 0.001 kg/ton product"},
   {"name": "Chemical Oxygen Demand", "category": "water", "amount": 8.7e-5, "unit": "kilogram", "note": "Tab. 96.3 'COD' 0.087 kg/ton product"}],
  "resources": []}})
