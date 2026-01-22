# OpenSky data (LLA format) →  coordinates conversion (ECEF) → satellites / pseudoranges (calculations) → IQ signals (signal compilation) → ZeroMQ (final publishing)
from time import time
import numpy as np 
from opensky_route_fetcher import get_active_icao, fetch_flight_track
from lla_to_ecef import lla_to_ecef
from satellites import generate_satellite_positions
from iq_generation import pseudorange, generate_ca_code, generate_iq
from zeromq_publisher import publish_iq


print("Starting GNSS Signal Simulation")

# SIMULATION PARAMETERS ----------------------------------------
NUM_SATS = 8
SAMPLING_FREQ = 2e6     # 2 MHz
SIGNAL_DURATION = 0.01  # 10 ms
DOPPLER_MIN = -5000     # Hz
DOPPLER_MAX = 5000      # Hz
# --------------------------------------------------------------




# SIMULATION ---------------------------------------------------
print("----- Fetching Live Flight Track -----")
icao24 = get_active_icao()

if not icao24:
    print("No current active aircrafts found")
    exit

print("Using active aircraft ICAO24: ", icao24)

end = int(time())
begin = end - 3600  # last 1 hour

track_lla = fetch_flight_track(icao24, begin, end)
print("Number of points in flight track:", len(track_lla))

# Generating Satellites (ECEF Position Coordinates) ------------
sat_positions = generate_satellite_positions(NUM_SATS)

# MAIN LOOP ----------------------------------------------------
for idx, point in enumerate(track_lla):
    time = point["time"] 
    lat = point["lat"]
    lon = point["lon"]
    alt = point["alt"]
    metadata = [time, lat, lon, alt] 
    
    # Converting aircraft/receiver position to ECEF
    rx_ecef = lla_to_ecef(lat, lon, alt)

    print(f"[{idx+1}/{len(track_lla)}] Receiver ECEF:", rx_ecef)
    
    # Making buffer to accumulate total signal from all satellites
    iq_total = np.zeros(
        int(SAMPLING_FREQ * SIGNAL_DURATION),
        dtype=np.complex64
    )

    for prn, sat_ecef in enumerate(sat_positions):
        # NOTE: Doppler and PRN values for now are random for demo
        pr = pseudorange(rx_ecef, sat_ecef)
        doppler = np.random.uniform(DOPPLER_MIN, DOPPLER_MAX)

        # Generate satellite signal
        iq_sat = generate_iq(
            prn=prn,
            pseudorange=pr,
            doppler_shift=doppler,
            sampling_freq=SAMPLING_FREQ,
            signal_duration=SIGNAL_DURATION
        )

        iq_total += iq_sat
    publish_iq("GNSS", iq_total, metadata)
    print("Published IQ frame to topic: GNSS")

print("Simulation complete")

