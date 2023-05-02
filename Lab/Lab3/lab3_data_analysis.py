import numpy as np
import matplotlib.pyplot as plt

def transfer_func(s):
    max_val = None

    for i, val in enumerate(s):
        val_db = 20 * np.log10(np.abs((val * 200) / ((val + 10) * (val + 2))))

        if max_val is None or val_db > max_val:
            max_val = val_db
            max_freq_index = i

        s[i] = val_db

    return s, max_val, max_freq_index

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

    return x, y

filename = 'ENGR203_lab3.txt'  # Replace with your actual filename

with open(filename, 'r', encoding='utf-8') as file:
    data_string = file.read()

freq, v_out1 = extract_data(data_string)

# Transfer Function values
values = np.arange(0.01, 100000.01, 0.05).tolist()
s = [1j * val for val in values]

v_out2, max_val, max_freq_index = transfer_func(s)
hertz = [val / (2 * np.pi) for val in values]

print("Transfer Function Bode Plot:")
print(f"Max Vo: {max_val} dB")
print(f"Frequency: {hertz[max_freq_index]} Hz")
print()

print("Constructed Circuit Bode Plot:")
print(f"Max Vo: {max(v_out1)} dB")
print(f"Frequency: {freq[v_out1.index(max(v_out1))]} Hz")
print()

fig, axs = plt.subplots(1, 2, figsize=(15, 5))

axs[0].semilogx(hertz, v_out2)
axs[0].grid(True)
axs[0].set_xlabel('Frequency (Hz)')
axs[0].set_ylabel('Vo (dB)')
axs[0].set_title('Transfer Function Bode Plot')

axs[1].semilogx(freq, v_out1)
axs[1].grid(True)
axs[1].set_xlabel('Frequency (Hz)')
axs[1].set_ylabel('Vo (dB)')
axs[1].set_title('Constructed Circuit Bode Plot')

plt.tight_layout()
plt.show()
