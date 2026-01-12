import requests

# OpenSky REST API docs on https://openskynetwork.github.io/opensky-api/rest.html

# Since we are simulating a GNSS attack we will need an airborne aircraft (identified by ICAO24)

def get_active_icao():
    url = "https://opensky-network.org/api/states/all"
    response = requests.get(url)
    data = response.json()

    for s in data["states"]:
        on_ground = s[8]
        if not on_ground:
            return s[0]  # ICAO24

# Fetch flight track of aircraft in timeframe
def fetch_flight_track(icao24, begin, end):
    url = "https://opensky-network.org/api/tracks/all"
    params = {
            "icao24": icao24,  # Aircraft identifier as assigned by ICAO
            "begin": begin,    # Timeframe begin/end for search. These params are not officially written on the API documentation but are supported)
            "end": end
    }
    
    response = requests.get(url, params)
    data = response.json()

    track = []
    for t in data["path"]:
        track.append({
            "time": t[0],
            "lat": t[1],
            "lon": t[2],
            "alt": t[3]
        })
    return track
