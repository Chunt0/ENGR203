import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the model function
def rlc_func(x, A, B, s_1, s_2):
    return A * np.exp(s_1*x) + B * np.exp(s_2*x)

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
filename = 'ENGR203_lab2_p2_1.txt'
x, y = read_data(filename)

# Pull out first response curve
x, y = np.array(x[:81]), np.array(y[:81])

# Fit the data to the model
popt, pcov = curve_fit(rlc_func, x, y)

fit_out = np.array([rlc_func(x,popt[0], popt[1], popt[2], popt[3])])
fit_out = fit_out.reshape(81,)

# Print the estimated parameters
print("A_1:", popt[0])
print("A_2:", popt[1])
print("s_1:", popt[2])
print("s_2:", popt[3])

# Print the estimated parameters
# Create a plot of the data for the first source free current response curve
plt.scatter(x, y, label='Data')
plt.plot(x, fit_out, 'r', label='Fit')
plt.xlabel('Time [t] (s)')
plt.ylabel('Current [I_l] (A)')
plt.title('Inductor Current vs. Time')
plt.legend()
plt.show()