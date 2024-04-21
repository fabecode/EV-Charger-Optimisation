# EV-Charger-Optimisation
## Project Overview
The placement of EV charging stations and number of EV charging points at each station is a complicated but important part of the wider acceptance of electric vehicles (EVs). The problem lies mainly in 4 broad categories - charging demand prediction, charging station placement, EV station utilisation, and charging scheduling and pricing. However, due to the Singapore government’s initiative to shift towards zero internal combustion engines by 2040, this project mainly focuses on the issue of charging station placement and optimal number of charging stations. This requires finding the optimal number of EV charging points to be installed at each charging point to facilitate the usage of EVs and be able to meet the current charging demand. 

The project aims to determine the optimal number of EV charging points to be installed at each charging location by maximising coverage, specifically, Point-of-Interest (POI) coverage in Singapore. POI coverage assesses the accessibility of charging infrastructure to key destinations such as shopping centres and HDBs. By prioritising POI coverage, the optimization model ensures that EV charging stations are strategically located near areas of high human activity, where EV users are likely to visit frequently. This approach enhances the convenience and usability of the charging network, encouraging EV adoption and facilitating seamless integration into daily routines.

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
- [HDBPropertyInformation.csv](./data/HDBPropertyInformation.csv) from [HDB Property Information (Data.gov)](https://beta.data.gov.sg/datasets/d_17f5382f26140b1fdae0ba2ef6239d2f/view)
- [ShoppingMall.csv](./data/ShoppingMall.csv) from [Shopping Mall Coordinates (Kaggle)](https://www.kaggle.com/datasets/karthikgangula/shopping-mall-coordinates)