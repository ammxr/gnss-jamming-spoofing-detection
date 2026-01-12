# For the purpose of this project we will used fixed satellite positions

import numpy as np

def generate_satellite_positions(num_sats=8):
    sats = []
    for i in range(num_sats):
        angle = np.deg2rad(360 * i / num_sats) # Evenly spaced (in circular formation) satellites)
        orbital_radius = 6378000 + 20200000 # Earth radius + rough altitude (in meters) for GPS satellites 
        sats.append(np.array([
            orbital_radius * np.cos(angle),   # X plane
            orbital_radius * np.sin(angle),   # Y plane
            10000000                          # Z plane, 10000 km, instead of having an angular tilt we will just adjust the Z offset to make for angular planes in reference to Earth's equatorial plane
        ]))
        
        # Orbital Planes visual example: https://www.researchgate.net/figure/Orbital-Keplerian-elements-For-GEO-earth-orbiting-satellites-the-reference-plane-is_fig1_318980403
        # In the real world, GPS satellites are spread on 6 orbital planes at roughly 55 degrees inclination to the equator, for this simulation we use a random offset so it is not flat on the XY plane
    
    return sats

