import numpy as np
import matplotlib.pyplot as plt

def transfer_func(s):
    for i, val in enumerate(s):
        s[i] = 20*np.log10(np.abs((val*200)/((val+10)*(val+2))))
    return s

def extract_data(data_string):
    data_lines = data_string.strip().split('\n')
    x = []
    y = []

    for line in data_lines:
        freq, value = line.split()
        freq = float(freq)
        value = float(value.split(",")[0].replace('dB','').replace('(',''))
        x.append(freq)
        y.append(value)

    return x,y


filename = 'ENGR203_lab3.txt'  # Replace with your actual filename

with open(filename, 'r', encoding='utf-8') as file:
    data_string = file.read()

freq, v_out = extract_data(data_string)

# Transfer Function values
values = np.arange(0.01, 100000.01, 0.05).tolist()
s = []
for val in values:
    val = 1j*val
    s.append(val)

y = transfer_func(s)
hertz = [val/(2*np.pi) for val in values]

print()
print()


plt.semilogx(hertz, y)
plt.grid(True)  # Show grid lines
plt.xlabel('Frequency (Hz)')
plt.ylabel('Vo (dB)')
plt.title('Transfer Function Bode Plot')
plt.show()

plt.semilogx(freq, v_out)
plt.grid(True)  # Show grid lines
plt.xlabel('Frequency (Hz)')
plt.ylabel('Vo (dB)')
plt.title('Constructed Circuit Bode Plot')
plt.show()

