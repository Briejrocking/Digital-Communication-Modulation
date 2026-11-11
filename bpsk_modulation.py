import numpy as np 
import matplotlib.pyplot as plt

# Parameters
bits = [1, 0, 1, 1, 0, 1, 0, 0]
bit_duration = 1
fc = 5
fs = 1000

# Generate time array
samples_per_bit = int(fs * bit_duration)
t = np.arange(0, len(bits) * bit_duration, 1/fs)

# Generate carrier
carrier = np.sin(2 * np.pi * fc * t)

# Convert binary data into bipolar data
digital_signal = np.repeat(bits, samples_per_bit)
bipolar_signal = 2 * digital_signal - 1

# BPSK modulation
bpsk_signal = bipolar_signal * carrier

# Plot results
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.step(np.arange(len(bits) + 1), bits + [bits[-1]], where="post")
plt.title("Binary Input Data")
plt.ylabel("Bits")
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t, carrier)
plt.title("Carrier Signal")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t, bpsk_signal)
plt.title("BPSK Modulated Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.savefig("bpsk_modulation.png", dpi=300)
plt.show()
