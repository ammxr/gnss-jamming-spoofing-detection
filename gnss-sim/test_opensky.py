from time import time
from opensky_route_fetcher import fetch_flight_track, get_active_icao

# Get an actively flying aircraft
icao24 = get_active_icao()

if not icao24:
    print("No active aircraft found")
    exit(1)

print("Using active aircraft ICAO24:", icao24)

end = int(time())
begin = end - 3600  # last 1 hour

track = fetch_flight_track(icao24, begin, end)

print("Number of points:", len(track))
if track:
    print("First point in track as per timeframe:", track[0])
    print ("Most recent point in track as per timeframe:", track[-1])
else:
    print("No data")
