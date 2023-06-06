import matplotlib.pyplot as plt

# Data
voltage = [0, 1, 2, 3, 4, 5]
frequency = [18, 36.23, 74.41, 154.2, 321.0, 669.4]

# Create the graph
plt.scatter(voltage, frequency)
plt.xlabel('CV Input Voltage (V)')
plt.ylabel('Frequency (Hz)')
plt.title('CV Input Voltage vs Frequency')

# Display the graph
plt.show()

