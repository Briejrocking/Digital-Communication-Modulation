import numpy as np
import matplotlib.pyplot as plt

# Day 1: Sinusoidal Wave Generation

# Signal parameters
A = 1
f = 5
t = np.linspace(0, 1, 1000)

# Generate sinusoidal signal
signal = A * np.sin(2 * np.pi * f * t)

# Plot the signal
plt.figure(figsize=(10, 5))
plt.plot(t, signal, label="Sine Wave")

plt.title("Sinusoidal Wave")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Save and display graph
plt.savefig(r"D:\2026 to Further\Project\VS Code\sinusoidal_wave.png")
plt.show()