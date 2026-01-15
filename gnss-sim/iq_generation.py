import numpy as np

def pseudorange(receiver_ecef, sattelite_ecef):
    return np.linalg.norm(sat_ecef - receiver_ecef) # distance between sattelite and receiver (vector)

def generate_ca_code(prn, samples):
    np.random.seed(prn)
    return np.where(np.random.randn(samples) > 0, 1, -1)

def generate_iq(prn, pseudorange, doppler_shift, sampling_freq, signal_duration):

    # Array of discrete time samples (ADC Sampling)
    
    t_samples = 1/sampling_freq # Time (in seconds) between samples per complete signal according to the sampling frequency (used as interval step)
    signal_time_samples_array = np.arange(0, signal_duration, t_samples) # Creating evenly spaced sampling intervals (counting up by `t_samples`) for `signal_duration` / `t_samples` amount of enteries. 


    code = generate_ca_code(prn, len(signal_time_samples_array))
    phase = 2 * np.pi * doppler_shift * signal_time_samples_array # as time increases (signal_time_samples_array) the rotation angle increases (phase). The doppler shift (hz) affects speed of rotation 
    
    # IQ aka In-Phase (X-axis) Quadrature (Y-Axis), with the unique CA code randomly flipping signal (value 1 or -1)
    iq = code * np.exp(1j * phase)  # For each Phase point, we create 2 numbers for both axis where I = cos (left/right) and Q = sin (up/down)
    
    # The reason we dont do cos(phase) sin(phase) directly is for simplicity using Eulers Formula, most SDRs like HackRF use the complex number as well (Python complex64 ) so it is aligned with HW simulators out there

    return iq
