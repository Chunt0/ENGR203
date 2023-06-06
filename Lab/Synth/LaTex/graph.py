import matplotlib.pyplot as plt

# Plotting function
def plot_graph(filename):
    x = []
    y = []
    with open(filename, 'r') as file:
        for _ in range(999):  # Discard first 999 lines
            next(file)
        for line in file:
            line = line.strip().split('\t')
            x.append(float(line[0]))
            y.append(float(line[1]))
    name = filename.strip(".txt")
    plt.plot(x, y)
    plt.xlabel('Time (s)')
    plt.ylabel('Voltage (v)')
    plt.title(f"Voltage over Time Node A: {name}")
    plt.show()

# Plot graphs in separate windows
for i in range(1, 6):
    filename = f"VC{i}.txt"
    plot_graph(filename)
