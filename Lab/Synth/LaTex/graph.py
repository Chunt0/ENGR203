import matplotlib.pyplot as plt
import numpy as np

freq = [18.5, 4854]

# Read data from each file
for i in range(2):
    filename = f"./data/CCV{i}.txt"
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


    # Create a new figure and plot
    plt.figure()
    plt.plot(x, y)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (v)')
    plt.title(f'Voltage over Time at Node A: High Frequency - {freq[i]} Hz')

    # Display the plot for each data set
    plt.show()
