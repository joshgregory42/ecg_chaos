# ECG Segmentation and Katz Fractal Dimension

This Python script takes in ECG files written in comma separated values (CSV) format (typically from an Excel file), uses QRS detection to extract a single heartbeat, and then calculates the fractal dimension using a formula written by Michael J. Katz in the following:

Michael J. Katz. “Fractals and the analysis of waveforms”. In: Computers in Biology and Medicine 18.3
(1988), pp. 145–156. issn: 0010-4825. doi: https://doi.org/10.1016/0010-4825(88)90041-8. url:
https://www.sciencedirect.com/science/article/pii/0010482588900418.

To run this, replace lines 38-42 of `fractal_dim.py` with the paths of the ECG CSV files, and modify line 53 in `qrs_segment.py` with the appropriate sampling rate.

After making the necessary modifications, run `fractal_dim_calc.py` to obtain the associated Katz fractal dimensions.

Completed in part for University of Colorado Boulder APPM 3010-001: Chaos in Dynamical Systems, Fall 2023.
