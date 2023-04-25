import numpy as np
import matplotlib.pyplot as plt

# Define a function to read data from a file
def read_data(filename):
    x = []
    y = []

    with open(filename, 'r') as file:
        for line in file:
            try:
                parts = line.strip().split('\t')
                x_val = float(parts[0])
                y_val = float(parts[1])
                x.append(x_val)
                y.append(y_val)
            except:
                continue

    return x, y

# Read the data from the file
filename = 'ENGR203_lab2_p2_2.txt'
x, y = read_data(filename)

plt.plot(x,y)
plt.xlabel('Time [t] (s)')
plt.ylabel('Current [I_l] (A)')
plt.title('Inductor Current vs. Time')
plt.show()