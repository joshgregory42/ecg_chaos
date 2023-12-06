import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import qrs_segment as segment

def katz_fractal_dimension(data):
    """
    Calculate the Katz fractal dimension of a waveform.
    """
    N = len(data)
    d = np.abs(np.max(data) - np.min(data))
    L = np.sum(np.abs(np.diff(data)))

    katz_dimension = np.log(N) / (np.log(N) + np.log(d / L))
    
    return katz_dimension

def katz_dim(df):

    t = df.iloc[:, 0]
    waveform = df.iloc[:, 1]

    # Calculate Katz fractal dimension
    katz_dimension = katz_fractal_dimension(waveform)

    print(f"Katz Fractal Dimension: {katz_dimension}")

    return katz_dimension


def main(file_path):
    data = segment.single_beat(file_path)

    katz_dimension = katz_dim(data)

    return katz_dimension

k_1 = main('path_1.csv')
k_2 = main('path_2.csv')
k_3 = main('path_3.csv')
k_4 = main('path_4.csv')
k_5 = main('path_5.csv')


katz_dims = [k_1, k_2, k_3, k_4, k_5]

# Create a box and whisker plot of katz_dims
plt.boxplot(katz_dims)
plt.title('Box and Whisker Plot of Katz Dimensions')
plt.ylabel('Katz Dimension')
plt.savefig('boxplot.png', dpi=1000)
plt.show()

# Convert your list to a pandas Series
katz_dims_series = pd.Series(katz_dims)

# Generate descriptive statistics
stats = katz_dims_series.describe()

print(stats)
