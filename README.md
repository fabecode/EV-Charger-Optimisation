# EV-Charger-Optimisation
## Key Notebooks
Run in below order:
1. [merge_data.ipynb](./merge_data.ipynb)
2. [convert_coord.ipynb](./convert_coord.ipynb)
    - To run, OneMap API key is required. Update [config.json](./config.json) Refer to [OneMap API Coordinate Conversion Docs](https://www.onemap.gov.sg/apidocs/apidocs/#coordinateConverters) for more information.
3. [optimisation_bishan.ipynb](./optimisation_bishan.ipynb)
    - To run Gurobi optimisation on Bishan area

## Datasets
- [HDB Carpark Information (Data.gov)](https://beta.data.gov.sg/datasets/d_23f946fa557947f93a8043bbef41dd09/view)
- [HDB Property Information (Data.gov)](https://beta.data.gov.sg/datasets/d_17f5382f26140b1fdae0ba2ef6239d2f/view)
- [Shopping Mall Coordinates (Kaggle)](https://www.kaggle.com/datasets/karthikgangula/shopping-mall-coordinates)