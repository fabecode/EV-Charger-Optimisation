# EV-Charger-Optimisation
## Key Notebooks
Run in below order:
1. [convert_coord.ipynb](./convert_coord.ipynb) - Converts Coordinates
    - To run, OneMap API key is required. Update [config.json](./config.json) Refer to [OneMap API Coordinate Conversion Docs](https://www.onemap.gov.sg/apidocs/apidocs/#coordinateConverters) for more information.
    - Outputs: [HDBCarparkInformation_latlong.csv](./data/HDBCarparkInformation_latlong.csv), [HDBPropertyInformation_latlong.csv](./data/HDBPropertyInformation_latlong.csv)
2. [merge_data.ipynb](./merge_data.ipynb) - Merges datasets and cleans data. 
    - Outputs: [CombinedCarpark.csv](./data/CombinedCarpark.csv) and [CombinedPOI.csv](./data/CombinedPOI.csv)
3. [optimisation_bishan.ipynb](./optimisation_bishan.ipynb)
    - To run Gurobi optimisation on Bishan area. Includes sensitivity analysis.
    - If you do not want to reconstruct the distance matrix, you can load precomputed distance matrix at [bishan_dm.pkl](./data/pkl/bishan_dm.pkl).
4. [optimisation_for_testing.ipynb](./optimisation_for_testing.ipynb)
    - To run Gurobi optimisation on different areas for testing purposes. You can easily change the area by changing the `area_name` variable in the notebook.
    - In the last cell, you can easily extract the results of all areas. The output can be found in [EVChargerPlacementResults.csv](./data/EVChargerPlacementResults.csv).

## Datasets
- [HDBCarparkInformation.csv](./data/HDBCarparkInformation.csv) from [HDB Carpark Information (Data.gov)](https://beta.data.gov.sg/datasets/d_23f946fa557947f93a8043bbef41dd09/view)
- [HDBPropertyInformation](./data/HDBPropertyInformation.csv) from [HDB Property Information (Data.gov)](https://beta.data.gov.sg/datasets/d_17f5382f26140b1fdae0ba2ef6239d2f/view)
- [ShoppingMall.csv](./data/ShoppingMall.csv) from [Shopping Mall Coordinates (Kaggle)](https://www.kaggle.com/datasets/karthikgangula/shopping-mall-coordinates)