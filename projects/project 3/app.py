import os
import requests

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

def get_lat_lng(place_name):
    url = 
    params = {"access_token": MAPBOX_TOKEN}

    response = request.get(url, params=params)
    response.raise_for_status()
    data = response.json ()

    coords = data


def get_nearest_mbta_stop(lat, lng):
    url = "https://api-v3.mbta.com/stops"
    params = {"api_key": MBTA_API_KEY, "filter[latitude]": lat, "filter[longitude]": lng}
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    stops = data["data"]
    if not stops:
        return None
    nearest_stop = stops[0]

    wheelchair_accessible = nearest_stop["attributes"]["wheelchair_accessible"]
    if wheelchair_accessible == 1:
        accessibility = "Wheelchair accessible"
    elif wheelchair_accessible == 2:
        accessibility = "Not wheelchair accessible"
    else:
        accessibility = "Unknown accessibility"
    return nearest_stop["attributes"]["name"], accessibility

def find_stop_near(place_name):
    lat, lng = get_lat_lng(place_name)
    stop_info = get_nearest_mbta_stop(lat, lng)
    if stop_info:
        stop_name, accessibility = stop_info
        print(f"The nearest MBTA stop to {place_name} is {stop_name}. Accessibility: {accessibility}")
    else:
        print(f"No MBTA stops found near {place_name}.")

def main():
    place_name = input("Enter a location: ")
    find_stop_near(place_name)
    print("Thank you for using the MBTA stop finder!")
    print("Input a location to find the nearest MBTA stop and its accessibility.")

if __name__ == "__main__":)
