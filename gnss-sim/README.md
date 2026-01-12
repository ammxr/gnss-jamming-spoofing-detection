# Signal Generation Rough Data Flow/Process

OpenSky data (LLA format) →  coordinates conversion (ECEF) → satellites / pseudoranges (calculations) → IQ signals (signal compilation) → ZeroMQ (final publishing)

---

## OpenSky Data

OpenSky's API provides historical and real-time active flight tracks for aircraft worldwide. The data returned by the Track endpoint for each aircraft at a specific time includes:

{
    "time": timestamp,
    "lat": latitude,
    "lon": longitude,
    "alt": altitude
}

Combining multiple timestamps this provides the trajectory of the aircraft over the desired timeframe in **LLA (latitude, longitude, altitude)** form.

Since we want to simulate how a GNSS receiver would compute positions, we need this data in a format suitable for GNSS calculations: **ECEF coordinates**.

---

## ECEF Coordinates

ECEF (Earth-Centered, Earth-Fixed) is a 3D Cartesian coordinate system with its origin at the Earth's center. Unlike LLA, which uses angles and altitude, ECEF represents positions in **meters along X, Y, and Z axes**, making it suitable for GNSS physics/calculations **(SPECIFIC EXAMPLES TO BE ADDED LATER)**

Conversion from LLA to ECEF is done using the formula in our `lla_to_ecef.py` file. Further information regarding the equation and its source can be found there as well.
---

## Receiver Concept

In this simulator, the aircraft can be thought of as the **GNSS receiver moving in space**. OpenSky data tells the simulator where the aircraft is at each moment.

This is used to compute:

1. **ECEF coordinates of the receiver**, which then can be used to get distances to satellites **(pseudoranges)** as well as **doppler shifts**.
These results combined with a PRN is then used to compile the **base GNSS signal**, which mimics what a real receiver would measure if it were flying along the aircraft's trajectory.

---

Pretty much up to this point, the goal was to **generate satellite signals based on real aircraft routes** and so I worked backwards from actual routes to achieve that.
