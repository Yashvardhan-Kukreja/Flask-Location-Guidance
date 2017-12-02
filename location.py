import requests
from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route('/api/location', methods=['POST'])
def test():
    api_key = "AIzaSyCb21lFiDWAH9mCc48qBvsLXSaRMN-BvME"
    mode = "walking"
    origin = "VIT+Vellore"
    destination = request.form["data"]
    destination = destination.replace(" ", "+")
    base_url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + origin + "&destination=" + destination + "&mode=" + mode + "&key=" + api_key
    client = requests.get(base_url)
    output_json = client.json()
    for item in output_json["routes"][0]["legs"][0]["steps"]:
        if ('maneuver' in item.keys()):
            print("After " + item["distance"]["text"])
            print(item["maneuver"])
            print("")
        else:
            print("Go straight for " + item["distance"]["text"])
            print("")
    return jsonify({"success": "1", "message": "Location request sent successfully to the server"})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
