
import numpy as np
import matplotlib.pyplot as plt

# Parameters
bits = [1, 0, 1, 1, 0, 1, 0, 0]
fc = 5
fs = 1000
symbol_duration = 1

# QPSK phase mapping (Gray coding)
phase_map = {
    (0, 0): np.pi/4,
    (0, 1): 3*np.pi/4,
    (1, 1): 5*np.pi/4,
    (1, 0): 7*np.pi/4
}

# Group bits into pairs
bit_pairs = [
    tuple(bits[i:i+2])
    for i in range(0, len(bits), 2)
]

# Generate QPSK signal
samples_per_symbol = int(fs * symbol_duration)
qpsk_signal = []
phase_values = []

for pair in bit_pairs:
    phase = phase_map[pair]
    phase_values.append(np.degrees(phase))

    t = np.arange(samples_per_symbol) / fs

    signal = np.cos(2*np.pi*fc*t + phase)
    qpsk_signal.extend(signal)

qpsk_signal = np.array(qpsk_signal)

# Time array
time = np.arange(len(qpsk_signal)) / fs

# Plot results
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.step(np.arange(len(bits)), bits, where="post")
plt.title("Binary Input Data")
plt.ylabel("Bits")
plt.grid()

plt.subplot(3, 1, 2)
plt.step(
    np.arange(len(phase_values)),
    phase_values,
    where="post"
)
plt.title("QPSK Phase Selection")
plt.ylabel("Phase (degrees)")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(time, qpsk_signal)
plt.title("QPSK Modulated Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.savefig("qpsk_modulation.png", dpi=300)
plt.show()
