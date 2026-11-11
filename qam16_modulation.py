from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# =====================================
# 1. GENERATE 16-QAM CONSTELLATION
# =====================================

levels = np.array([-3, -1, 1, 3])

I_const, Q_const = np.meshgrid(levels, levels)

symbols = I_const.flatten() + 1j * Q_const.flatten()


# =====================================
# 2. GENERATE RANDOM BINARY DATA
# =====================================

num_symbols = 20

bits = np.random.randint(0, 2, num_symbols * 4)

# Gray-coded mapping
mapping = {
    (0, 0): -3,
    (0, 1): -1,
    (1, 1): 1,
    (1, 0): 3
}

bit_groups = bits.reshape(-1, 4)

I_bits = bit_groups[:, :2]
Q_bits = bit_groups[:, 2:]

I_signal = np.array([mapping[tuple(b)] for b in I_bits])
Q_signal = np.array([mapping[tuple(b)] for b in Q_bits])


# =====================================
# 3. GENERATE CARRIER SIGNALS
# =====================================

fc = 5

samples_per_symbol = 100

t = np.arange(num_symbols * samples_per_symbol) / samples_per_symbol

I = np.repeat(I_signal, samples_per_symbol)
Q = np.repeat(Q_signal, samples_per_symbol)

carrier_I = np.cos(2 * np.pi * fc * t)
carrier_Q = np.sin(2 * np.pi * fc * t)


# =====================================
# 4. 16-QAM MODULATION
# =====================================

qam_signal = (I * carrier_I - Q * carrier_Q) / np.sqrt(10)


# =====================================
# 5. DISPLAY ALL GRAPHS
# =====================================

plt.figure(figsize=(14, 10))

# Graph 1: Constellation diagram
plt.subplot(3, 1, 1)

plt.scatter(symbols.real, symbols.imag, color='blue')

plt.title("16-QAM Constellation Diagram")
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.grid(True)
plt.axis('equal')


# Graph 2: Random binary data
plt.subplot(3, 1, 2)

plt.step(np.arange(len(bits)), bits, where='post')

plt.title("Random Binary Input Data")
plt.xlabel("Bit Number")
plt.ylabel("Bit Value")
plt.grid(True)


# Graph 3: Modulated waveform
plt.subplot(3, 1, 3)

plt.plot(t, qam_signal, color='red')

plt.title("16-QAM Modulated Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()

output_dir = Path(__file__).resolve().parent / "outputs"
output_dir.mkdir(exist_ok=True)

plt.savefig(
    output_dir / "qam16_analysis.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()