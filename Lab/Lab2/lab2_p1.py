import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

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
zero_cross = [x[index] for index, val in enumerate(y[:-1]) \
              if val >= 0 and y[index + 1] < 0]
periods = [zero_cross[i] - zero_cross[i - 1] \
           for i in range(1, len(zero_cross))]
average_period = sum(periods) / len(periods)
omega_d = 2 * np.pi / average_period  # rad/s
f_d = 1 / average_period  # Hz

# To find the decay envelope, take the absolute value of the function
# and find the peak of each oscillation
y_abs = np.abs(y)
peak_indices, _ = find_peaks(y_abs)
max_y = [y_abs[i] for i in peak_indices]
max_x = [x[i] for i in peak_indices]


# Linearize the exponential function f(t) = Ae^(-alpha*t)
# ln(f(t)) = ln(A)+(-alpha)t
ln_y = np.log(max_y)

# Find the slope of the linearized function
dy = np.array([ln_y[i] - ln_y[i-1] \
               for i in range(1, len(ln_y))])
dx = np.array([max_x[i] - max_x[i-1] \
               for i in range(1, len(max_x))])
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

fig, axs = plt.subplots(3, 1, figsize=(8, 10))

# First subplot
axs[0].scatter(x, y)
axs[0].set_xlabel('Time [t] (s)')
axs[0].set_ylabel('Current [I_l] (A)')
axs[0].set_title('Inductor Current vs. Time')

# Second subplot
axs[1].scatter(max_x, max_y)
axs[1].set_xlabel('Time [t] (s)')
axs[1].set_ylabel('Absolute Value Current Peaks [I_l] (A)')
axs[1].set_title('Inductor Current Envelope vs. Time')

# Third subplot
axs[2].scatter(max_x, ln_y)
axs[2].set_xlabel('Time [t] (s)')
axs[2].set_ylabel('Natural Log of Current [ln(I_l)]')
axs[2].set_title('Semilog Inductor Current Envelope vs. Time')

plt.tight_layout()
plt.show()
