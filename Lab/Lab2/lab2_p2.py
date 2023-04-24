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
filename = 'ENGR203_lab2_p1_1.txt'
x, y = read_data(filename)

# Isolate the first Source Free Response
x, y= x[:282], y[:282]

# Find the period of oscillation
zero_cross = [x[index] for index, val in enumerate(y[:-1]) if val >= 0 and y[index + 1] < 0]
periods = [zero_cross[i] - zero_cross[i - 1] for i in range(1, len(zero_cross))]
average_period = sum(periods) / len(periods)
omega_d = 2 * np.pi / average_period  # rad/s
f_d = 1 / average_period  # Hz

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

# Linearize the exponential function f(t) = Ae^(-alpha*t)
# ln(f(t)) = ln(A)+(-alpha)t
ln_y = np.log(max_y)

# Find the slope of the linearized function
dy = np.array([ln_y[i] - ln_y[i-1] for i in range(1, len(ln_y))])
dx = np.array([max_x[i] - max_x[i-1] for i in range(1, len(max_x))])
slopes = np.array(dy/dx)
slope = sum(slopes/len(slopes))
alpha = slope * -1

# Find the y-intercept: Ln(A)
# ln(f(t)) = -alpha*t + Ln(A) --> Ln(A) = ln(f(t)) + alpha*t
# A = exp(ln(ft)+alpha*t)
y_int = np.exp(ln_y[1] + alpha * max_x[1])

# Print the required values
print(f"Alpha = {alpha}")
print(f"Angular frequency: {omega_d}")
print(f"B_2 = {y_int}")

# Create a plot of the data for the first source free current response curve
plt.scatter(x, y)
plt.xlabel('Time [t] (s)')
plt.ylabel('Current [I_l] (A)')
plt.title('Inductor Current vs. Time')
plt.show()

# Create a plot of the max values
plt.scatter(max_x, max_y)
plt.xlabel('Time [t] (s)')
plt.ylabel('Current [I_l] (A)')
plt.title('Inductor Current Maximums vs. Time')
plt.show()

# Create a plot of the linearized function
plt.scatter(max_x, ln_y)
plt.xlabel('Time [t] (s)')
plt.ylabel('Current [I_l] (A)')
plt.title('Inductor Current Maximums vs. Time')
plt.show()
