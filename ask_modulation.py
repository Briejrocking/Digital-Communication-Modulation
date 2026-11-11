import numpy as np
import matplotlib.pyplot as plt

# Parameters
bits = [1, 0, 1, 1, 0, 1, 0, 0]
bit_duration = 1
fc = 5
fs = 1000

# Generate time array
t = np.arange(0, len(bits) * bit_duration, 1/fs)

# Generate carrier signal
carrier = np.sin(2 * np.pi * fc * t)

# Generate digital data signal
digital_signal = np.repeat(bits, fs * bit_duration)

# ASK modulation
ask_signal = digital_signal * carrier

# Plot results
plt.figure(figsize=(12, 7))

plt.subplot(3, 1, 1)
plt.step(np.arange(len(bits)), bits, where="post")
plt.title("Binary Input Data")
plt.ylabel("Bits")
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t, carrier)
plt.title("Carrier Signal")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t, ask_signal)
plt.title("ASK Modulated Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.savefig("ask_modulation.png", dpi=300)
plt.show()
