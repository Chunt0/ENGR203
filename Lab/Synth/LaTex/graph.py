import matplotlib.pyplot as plt

# Read data from the text file
data = []
with open('./data/output.txt', 'r') as file:
    for line in file:
        values = line.split('\t')
        data.append([float(values[0]), float(values[1]), float(values[2])])

# Extract the columns
x_axis = [row[0] for row in data]
V_d = [row[1] for row in data]
V_out = [row[2] for row in data]

# Plot V_d vs x_axis
plt.figure(1)
plt.plot(x_axis, V_d, label='V_d')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (v)')
plt.title('Simulated Voltage Over Time at Node D')


# Plot V_out vs x_axis
plt.figure(2)
plt.plot(x_axis, V_out, label='V_out')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (v)')
plt.title('Simulated Voltage Over Time at V_out1')

# Display the graphs
plt.show()
