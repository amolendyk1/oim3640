from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        place = request.form.get("place")

        try:
            lat, lng, stops = find_stop_near(place)

            if not stops:
                return render_template("result.html",
                                       place=place,
                                       error="No MBTA stops found nearby.")

            nearest = stops[0]

            return render_template("result.html",
                                   place=place,
                                   stop_name=nearest["name"],
                                   wheelchair=nearest["wheelchair"])
        except Exception as e:
            return render_template("result.html",
                                   place=place,
                                   error=str(e))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)