import os
import requests
from dotenv import load_dotenv

load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

# ---------------------------------------------------------
# Get latitude and longitude from Mapbox
# ---------------------------------------------------------
def get_lat_lng(place_name):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json"
    params = {"access_token": MAPBOX_TOKEN}

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    coords = data["features"][0]["geometry"]["coordinates"]
    lng, lat = coords[0], coords[1]
    return lat, lng

# ---------------------------------------------------------
# Convert MBTA wheelchair code to text
# ---------------------------------------------------------
def get_wheelchair_accessibility(code):
    if code == 0:
        return "No accessibility information"
    elif code == 1:
        return "Wheelchair accessible"
    elif code == 2:
        return "Not wheelchair accessible"
    else:
        return "Unknown accessibility status"

# ---------------------------------------------------------
# Get all stops within a radius
# ---------------------------------------------------------
def get_stops_within_radius(lat, lng, radius=800):
    url = "https://api-v3.mbta.com/stops"
    params = {
        "api_key": MBTA_API_KEY,
        "filter[latitude]": lat,
        "filter[longitude]": lng,
        "filter[radius]": radius,
        "sort": "distance"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    stops = []
    for stop in data["data"]:
        attrs = stop["attributes"]
        stops.append({
            "name": attrs["name"],
            "lat": attrs["latitude"],
            "lng": attrs["longitude"],
            "distance": attrs.get("distance"),
            "wheelchair": get_wheelchair_accessibility(attrs["wheelchair_boarding"])
        })

    return stops

# ---------------------------------------------------------
# Main function combining everything
# ---------------------------------------------------------
def find_stop_near(place_name, radius=800):
    lat, lng = get_lat_lng(place_name)
    stops = get_stops_within_radius(lat, lng, radius)
    return lat, lng, stops