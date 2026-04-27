from flask import Flask, render_template, request
from mbta import find_stop_near
import json
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        place = request.form.get("place")
        radius = int(request.form.get("radius"))

        try:
            lat, lng, stops = find_stop_near(place, radius)

            if not stops:
                return render_template("stop.html",
                                       place=place,
                                       error="No MBTA stops found nearby.")

            nearest = stops[0]

            # Prepare stop data for map
            stops_json = json.dumps([
                {
                    "name": s["name"],
                    "lat": s["lat"],
                    "lng": s["lng"],
                    "color": "green" if s["wheelchair"] == "Wheelchair accessible" else "red"
                }
                for s in stops
            ])

            return render_template(
                "stop.html",
                place=place,
                lat=lat,
                lng=lng,
                nearest_name=nearest["name"],
                nearest_wheelchair=nearest["wheelchair"],
                stops_json=stops_json,
                mapbox_token=os.getenv("MAPBOX_TOKEN")
            )

        except Exception as e:
            return render_template("stop.html",
                                   place=place,
                                   error=str(e))

    # First page load → show form only
    return render_template("stop.html")


if __name__ == "__main__":
    app.run(debug=True)