import numpy as np
import matplotlib.pyplot as plt

def extract_data(data_string):
    data_lines = data_string.strip().split('\n')
    x = []
    y = []

    for line in data_lines:
        freq, value = line.split()
        freq = float(freq)
        value = float(value)
        x.append(freq)
        y.append(value)

    return x, y

def time_domain(t):
    sf = 1/166 # scaling factor
    output = [sf*(250*np.exp(-10*time)-50*np.exp(-2*time)) for time in t]
    return output

# Extract LTSpice Data
filename = "./ENGR203_lab3_step_response.txt"
with open(filename, 'r', encoding='utf-8') as file:
    data_string = file.read()

time_1, v_out_1 = extract_data(data_string)

# Inverse Laplace Transform
time_2 = np.arange(0, 2.5, 0.01).tolist()
v_out_2 = time_domain(time_2)


plt.plot(time_2, v_out_2)
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Vo (v)')
plt.title('Theoretically Analysed Step Response')
plt.show()

plt.plot(time_1, v_out_1)
plt.grid(True)
plt.xlabel('Time (s)')
plt.ylabel('Vo (v)')
plt.title('Simulated Step Response')
plt.show()