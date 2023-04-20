import numpy as np
import matplotlib.pyplot as plt

def read_data(filename):
    x = []
    y = []

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            x_val = float(parts[0])
            y_val = float(parts[1])
            x.append(x_val)
            y.append(y_val)

    return x, y

filename = "lab1_data.txt"
x, y = read_data(filename)

# Create two subplots with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10), sharex=False)

# First subplot: standard time vs volt data
ax1.plot(x, y, 'o')
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Voltage ")
ax1.set_title("Time vs Volt")
ax1.grid(True)

# Second subplot: second half of the data in semi-log form
half_length = int(len(x) *(1/2.5))
ax2.plot(x[40:half_length:], y[40:half_length], 'o')
#ax2.set_yscale("log")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Voltage (v)")
ax2.set_title("Plot of Charging Phase of Transient RC Circuit : Time vs. Voltage")
ax2.grid(True)

# Display the plots
plt.tight_layout()
plt.show()
