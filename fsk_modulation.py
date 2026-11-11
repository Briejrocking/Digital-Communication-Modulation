import numpy as np
import matplotlib.pyplot as plt

# Parameters
bits = [1, 0, 1, 1, 0, 1, 0, 0]
bit_duration = 1
fs = 1000

f0 = 5       # Frequency for binary 0
f1 = 10      # Frequency for binary 1

# Generate time array
samples_per_bit = int(fs * bit_duration)
t = np.arange(0, len(bits) * bit_duration, 1/fs)

# Generate digital data
digital_signal = np.repeat(bits, samples_per_bit)

# Generate frequency based on binary data
frequency = np.where(digital_signal == 1, f1, f0)

# Generate continuous-phase FSK signal
phase = 2 * np.pi * np.cumsum(frequency) / fs
fsk_signal = np.sin(phase)

# Plot results
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.step(np.arange(len(bits) + 1), bits + [bits[-1]], where="post")
plt.title("Binary Input Data")
plt.ylabel("Bits")
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t, frequency)
plt.title("Frequency Selection")
plt.ylabel("Frequency (Hz)")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t, fsk_signal)
plt.title("FSK Modulated Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.savefig("fsk_modulation.png", dpi=300)
plt.show()
