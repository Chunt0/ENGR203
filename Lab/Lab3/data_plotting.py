import numpy as np
import matplotlib.pyplot as plt

def extract_data(data_string):
    data_lines = data_string.strip().split('\n')
    extracted_data = []

    for line in data_lines:
        freq, value = line.split()
        freq = float(freq)
        value = value.replace('dB', '').replace('(','').replace(')','')
        value = value.split(",")
        value = float(value[0])
        extracted_data.append((freq, value))

    return extracted_data


filename = 'ENGR203_lab3.txt'  # Replace with your actual filename

with open(filename, 'r', encoding='utf-8') as file:
    data_string = file.read()

extracted_data = extract_data(data_string)
for freq, value in extracted_data:
    print(f"Frequency: {freq}, Value: {value}")

