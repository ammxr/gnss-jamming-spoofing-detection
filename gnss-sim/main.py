# OpenSky data (LLA format) →  coordinates conversion (ECEF) → satellites / pseudoranges (calculations) → IQ signals (signal compilation) → ZeroMQ (final publishing)
from time import time
from opensky_route_fetcher import get_active_icao, fetch_flight_track
from lla_to_ecef import lla_to_ecef

print("Starting GNSS Signal Simulation")
print("----- Fetching Live Flight Track -----")
icao24 = get_active_icao()

if not icao24:
    print("No current active aircrafts found")
    exit

print("Using active aircraft ICAO24: ", icao24)

end = int(time())
begin = end - 3600  # last 1 hour

track_lla = fetch_flight_track(icao24, begin, end)
total_points = len(track_lla)

print("Number of points in flight track:", total_points)

print("----- Converting Flight Track Points LLA to ECEF -----")

track_ecef = []
count = 0
for point in track_lla:
    count+=1
    time = point["time"] 
    lat = point["lat"]
    lon = point["lon"]
    alt = point["alt"]
    print("Attempting conversion", count, "/", total_points, "for LLA:   [" , lat , "        " , lon, "         ",  alt,"]")
    result_ecef = lla_to_ecef(lat, lon, alt)
    print("Conversion Successful ECEF Coordinates: ", result_ecef)
    
    track_ecef.append(result_ecef)
    print("-----------------------------------------------------------------------------------")

print("\n\nFlight Track Conversion Complete " , count , "/", total_points, "\n\n")
