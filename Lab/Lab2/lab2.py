import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Define the function to fit
def exponential_decay(x, a, b, c):
    return a * np.exp(-b * x) + c

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
filename = 'ENGR203_lab2_p1_1.txt'
x, y = read_data(filename)

# Create a plot of the data
plt.scatter(x[:282], y[:282])
plt.xlabel('Time [t] (s)')
plt.ylabel('Current [I_l] (A)')
plt.title('Inductor Current vs. Time')
plt.show()

# Steps through the first source free response curve and isolates the max
y1 = np.abs(y)
max_y = []
max_x = []
step = 29

for i in range(0, len(y1), step):
    temp_y = y1[i:i+step]
    new_val_index = np.argmax(temp_y)
    max_y.append(temp_y[new_val_index])
    max_x.append(np.array(x)[new_val_index+i])
    if i > 225:
        break

print(f"x: {max_x}")
print(f"y: {max_y}")

plt.semilogy(max_x, max_y)
plt.xlabel('Time [t] (s)')
plt.ylabel('Current [I_l] (A)')
plt.title('Inductor Current Maximums vs. Time')
plt.show()





