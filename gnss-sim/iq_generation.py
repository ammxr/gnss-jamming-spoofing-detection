import numpy as np

def pseudorange(receiver_ecef, sattelite_ecef):
    return np.linalg.norm(sat_ecef - rx_ecef) # distance between sattelite and receiver (vector)

def generate_ca_code(prn, samples):
    np.random.seed(prn)
    return np.where(np.random.randn(samples) > 0, 1, -1)

def generate_iq(prn, pseudorange, doppler_shift, sampling_freq, signal_duration):

    # Array of discrete time samples (ADC Sampling)
    
    t_samples = 1/sampling_freq # Time (in seconds) between samples per complete signal according to the sampling frequency (used as interval step)
    signal_time_samples_array = np.arange(0, signal_duration, t_samples) # Creating evenly spaced sampling intervals (counting up by `t_samples`) for `signal_duration` / `t_samples` amount of enteries. 


    # code = generate_ca_code(prn, len(signal_time_samples_array))
    # phase = 
    # iq = 
    return # iq 


