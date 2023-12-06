import biosppy.signals.ecg as ecg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def read_ecg_data(file_path):
    """
    Read ECG data from a CSV file.
    """
    ecg_data = pd.read_csv(file_path)
    return ecg_data.iloc[:, -1].values

def segment_single_heartbeat(ecg_data, sampling_rate):
    """
    Segment a single heartbeat using QRS complex detection.
    """
    # Perform QRS complex detection
    out = ecg.ecg(signal=ecg_data, sampling_rate=sampling_rate, show=False)

    # Extract R-peaks (QRS complexes)
    rpeaks = out['rpeaks']

    # Choose the first R-peak as the starting point for the single heartbeat
    start_index = rpeaks[0]

    # Choose a fixed duration for the single heartbeat (e.g., 1 second)
    duration = int(sampling_rate)

    # Extract the segment of the ECG signal corresponding to a single heartbeat
    single_heartbeat = ecg_data[start_index:start_index + duration]

    # Create time array for the segment
    time = np.arange(0, duration) / sampling_rate

    return time, single_heartbeat

def single_beat(file_path):

    # Read ECG data
    ecg_data = read_ecg_data(file_path)

    # Specify the sampling rate of the ECG data (modify if needed)
    sampling_rate = 100

    # Segment a single heartbeat
    time, single_heartbeat = segment_single_heartbeat(ecg_data, sampling_rate)

    # Create a DataFrame
    df = pd.DataFrame({
        'Time': time,
        'Single Heartbeat': single_heartbeat
    })

    return df
