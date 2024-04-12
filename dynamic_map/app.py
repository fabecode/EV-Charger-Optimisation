from flask import Flask, render_template
import folium
import codecs
import pandas as pd


app = Flask(__name__)

@app.route("/")
def index():
    # Create a map centered around Singapore
    map_sg = folium.Map(location=[1.3521, 103.8198], zoom_start=12)

    # Add HDB carpark plots to the map
    # df = pd.read_csv("../data/HDBCarparkInformation_latlong.csv")
    # # extract only the columns "car_park_no", "latitude", "longitude" and save it as dictionary similar to amenities data
    # hdb_carpark_data = [
    #     {"name": row["car_park_no"], "location": [row["latitude"], row["longitude"]]}
    #     for _, row in df.iterrows()
    # ]
    
    hdb_carpark_data = [
        {"name": "HDB Carpark A", "location": [1.3503, 103.8734]},
        {"name": "HDB Carpark B", "location": [1.3352, 103.8504]},
        {"name": "HDB Carpark C", "location": [1.3010, 103.8387]},
        # Add more HDB carpark data as needed
    ]

    amenities_data = [
        {"name": "Restaurant A", "location": [1.3503, 103.8734]},
        {"name": "Park B", "location": [1.3352, 103.8504]},
        {"name": "Shopping Mall C", "location": [1.3010, 103.8387]},
        # Add more amenities data as needed
    ]

    # Add HDB carpark markers to the map
    for carpark in hdb_carpark_data:
        folium.Marker(
            location=carpark["location"],
            popup=carpark["name"],
            icon=folium.Icon(color="blue"),
        ).add_to(map_sg)

    # Add amenities markers to the map
    for amenity in amenities_data:
        folium.Marker(
            location=amenity["location"],
            popup=amenity["name"],
            icon=folium.Icon(color="green"),
        ).add_to(map_sg)

    # Save the map HTML to a string
    hdb_carparks_amenities_sg_map_html = map_sg.get_root().render()

    return render_template(
        "index.html",
        hdb_carparks_amenities_sg_map_html=hdb_carparks_amenities_sg_map_html,
    )


if __name__ == "__main__":
    app.run(debug=True)
