# GNSS receivers internally work in ECEF, not in LLA (lat,lon,alt)
# LLA is geodetic, NOT geometric, GNSS physics only work in geometric space

import numpy as np


# The following implementation is explained on the following link:
# https://en.wikipedia.org/wiki/Geographic_coordinate_conversion#From_geodetic_to_ECEF_coordinates:~:text=projection%20to%20another.-,From%20geodetic%20to%20ECEF%20coordinates,-%5Bedit%5D

def lla_to_ecef(lat, lon, alt):
    a = 6378137.0 # Earth Equatorial radius
    b = 6356752.3142
    e = np.sqrt( (a**2 - b**2)/ a**2)
    print("Value of e ", e)

    lat = np.radians(lat)
    lon = np.radians(lon)
    
    N = a / np.sqrt(1 - e**2 * np.sin(lat)**2)

    x = (N + alt) * np.cos(lat) * np.cos(lon)
    y = (N + alt) * np.cos(lat) * np.sin(lon)
    z = (N * (1 - e**2) + alt) * np.sin(lat)
    print("ECEF coords: ", [x, y, z])
    return np.array([x, y, z])

# Test on equator/prime merdian coords 
# lla_to_ecef(0.0, 0.0, 0)
