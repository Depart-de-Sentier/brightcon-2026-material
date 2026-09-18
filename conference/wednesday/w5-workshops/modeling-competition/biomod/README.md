# Readme
___

# biomod
___


This is a Python package designed to take the European Commission Joint Research Centre (JRC) biomass flows dataset, turn it into a life cycle inventory-like matrix, implement future scenarios based on forecast of supply and demand of biomass sources and biobased products to generate an updated future version of the matrix, and support the identification of the marginal mix for LCA studies of bio-based products.

This library is developed based on **[EU Biomass flows](https://data.europa.eu/doi/10.2905/JRC.GEJXSR8)** dataset.

## 📖 Background Knowledge
___

### EU Biomass flows
[EU Biomass flows](https://data.europa.eu/doi/10.2905/JRC.GEJXSR8) is a dataset that stores harmonised data on biomass supply, uses and flows in the EU. This dataset mirrors the diagrams displayed in the interactive [EU Biomass Flows tool](https://datam.jrc.ec.europa.eu/datam/mashup/BIOMASS_FLOWS/) that represent the flows of biomass for each sector of the bioeconomy, from supply to uses including trade and food waste. The tool enables deeper analysis and comparison of the different countries and sectors across a defined time series. The EU Biomass Flows tool is based on the energy Sankey tool developed by Eurostat

### Sankey diagram
A Sankey diagram is a flow diagram that visually represents the movement of quantities of varius type (e.g., energy, money, and material) from one set of values to another. It uses directed arrows or bands where the width of each flow is proportional to its magnitude, facilitating the identification of the most significant flows and the losses or bottlenecks within a system. Nodes represent the stages or categories, and the flows connect them, moving from sources on one side to destinations on the other. The underlaying data is therefore structured as a table with sources, destinations, size of the flow (with adequate and consistent unit), and potentially details on the specific flow. The latter can differentiate 2 flows of different type that link the same 2 notes.

### Life Cycle Inventory (LCI)
A life cycle inventory (LCI) matrix is essentially a structured table that shows everything that goes into and comes out of a product throughout its entire life, from raw material extraction to disposal. Each row represents a step in the process – like manufacturing, transportation, or use – while each column represents resources or outputs such as energy, water, raw materials, or emissions. The numbers in the table show how much of each resource is used or how much pollution is generated at each stage.

## ✨ Features
___

This library allows four main operations:
1. Conversion of Sankey-oriented into an LCI-like matrix:
- Selects the raw data of interest based on the desired year and resolution level.
- Disaggregates the nodes that are aggregated in the raw data by solving a distribution problem based on a set of predefined validity rules for linkages between nodes (e.g., cultivation residues are not allowed as food).
- Converts the Sankey-oriented dataset into an LCI-like matrix table but preseving the absolute values.

2. Maps the bioeconomy matrix
- The different sources and destinations in the matrix are classified as:
  - **Primary sources**
    - These are the nodes that indicate where biomass enters the bioeconomy(e.g., cultivation, forestry, and fisheries, or import).
  - **Final outputs**
    - These are the nodes that indicate biobased products that leave the matrix as final products or that can be taken up by other industries outside the bioeconomy, including waste treatment.
  - **Intermediates**
    - These are the nodes that are not primary sources nor outputs and represent flows of material/energy that require further processing in other nodes within the bioeconomy.

- Imposes a set of rules to safeguard specific relationships between nodes such as technical coefficients that describe co-production, i.e., processes that generates multiple products of different types and values (e.g., ceral cultivation generating cereal grains and straw), or a specific bill of materials. This default set of rules can be adjusted.

3. Assesses how the increased demand of a new biobased product could compete with the other products for the same pool of limited biomass feedstock:
    - The matrix is expanded to accomodate a new product.
    - The product is linked to the appropriate sources (primary/intermediate) and the rules ar re-mapped accordingly and/or updated .
    - An optimization process adjust the matrix to accomodate the user-defined final output for the newly introduced biobased product.
      - The optimization process can be adjusted based on user preferences.
      - It prioritizes meeting this demand tapping first into any available and suitable surplus.
      - If surpluses are unavailable or insufficient, it taps into the pool of feedstock currently utilized for the production of other biobased products (outputs).
      - The affected (preexisting) biobased product(s) will incur a deficit as their demand will not be met because of this new competition
    - The deficit of biobased products are quantify the net deficit that the specified demand of new biobased product will generate as unintended consequence

  **NOTICE:**
    - The model can accommodate demands for multiple newly introduced biobased products, for existing products, or for a mix of the two.


## 👩‍💻 Getting Started
___
### Requirements
- This library was developed using **Python 3.13.5**.

### Dependencies
- You need to have a few packages installed:
    - **pandas**
    - **pulp**
    - **logging**
    - **gurobipy**
    - **numpy**
    - **scipy**

### Prepare the directory
1. Unzip the notebooks folder.


2. Ensure the directory structure is the following.
```
your_project_folder/
│
├── __init__.py
├── competition.py
├── disaggregation.py
├── matrix_assembling.py
├── README.md
├── Detailed_guide.md
├── requirements.txt
└── notebooks/
    ├── 1-Raw_to_disaggregated.ipynb
    └── 2-Disaggregated_to_matrix.ipynb
    └── 3-Demand_competition_examples.ipynb
```
### Required files

**External database file**
This library was developed on the raw JRC data [EU Biomass flows] as a starting point. The raw data can be downloaded at **[EU Biomass flows](https://data.europa.eu/doi/10.2905/JRC.GEJXSR8)**. Note: the raw data is not provided in the library, so it must be downloaded separately.

### Notebooks
- [1-Raw_to_disaggregated.ipynb](notebooks/1-Raw_to_disaggregated.ipynb)
- [2-Disaggregated_to_matrix.ipynb](notebooks/2-Disaggregated_to_matrix.ipynb)
- [3-Demand_competition_examples.ipynb](notebooks/3-Demand_competition_examples.ipynb)

## 💬 Contacts
___
If you encounter any issues or would like to contribute to the library, please contact:
  - Fabio Sporchia (fabios@plan.aau.dk)
  - Kíra Lancz (kiral@plan.aau.dk)
  - Massimo Pizzol (massimo@plan.aau.dk)

## Funding
___
This contribution is funded by the [LCA4BIO project](https://lca4bioproject.eu/) (Horizon Europe, grant number 101135371)[^note].

## License
This project is licensed under the MIT License — see the LICENSE file for details.
This package depends on Gurobi (gurobipy), which requires a separate commercial or academic license.
See https://www.gurobi.com for details.

___
[^note]: Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Executive Agency. Neither the European Union nor the granting authority can be held responsible for them