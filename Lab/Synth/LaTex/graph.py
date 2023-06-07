import matplotlib.pyplot as plt
import numpy as np

# Read data from each file
for i in range(6):
    filename = f"./data/CV{i}.txt"
    x = []
    y = []
    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split()
            x.append(float(values[0]))
            y.append(float(values[1]))
    # Shift x-axis values to start at zero
    min_x = x[0]
    x = [val - min_x for val in x]

    # Find the peaks and calculate the frequency
    peaks, _ = np.where(np.diff(np.sign(np.diff(y))) < 0)
    if len(peaks) >= 2:
        peak_diff = x[peaks[1]] - x[peaks[0]]
        frequency = 1 / peak_diff
        print(f"CV{i} Frequency: {frequency:.2f} Hz")
    else:
        print(f"CV{i} Frequency: Not enough peaks to calculate")

    # Create a new figure and plot
    plt.figure()
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'CV{i} Data')

    # Display the plot for each data set
    plt.show()
