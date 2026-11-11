from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. GENERATE RANDOM BINARY DATA
# ==========================================

np.random.seed(42)

num_symbols = 100

bits = np.random.randint(0, 2, num_symbols * 4)

# Gray-coded 16-QAM mapping
mapping = {
    (0, 0): -3,
    (0, 1): -1,
    (1, 1): 1,
    (1, 0): 3
}

bit_groups = bits.reshape(-1, 4)

I_bits = bit_groups[:, :2]
Q_bits = bit_groups[:, 2:]

I_signal = np.array([
    mapping[tuple(b)] for b in I_bits
])

Q_signal = np.array([
    mapping[tuple(b)] for b in Q_bits
])


# ==========================================
# 2. GENERATE 16-QAM SYMBOLS
# ==========================================

tx_symbols = (
    I_signal + 1j * Q_signal
) / np.sqrt(10)


# ==========================================
# 3. CALCULATE SIGNAL POWER
# ==========================================

signal_power = np.mean(
    np.abs(tx_symbols) ** 2
)

print("Signal Power:", signal_power)


# ==========================================
# 4. GENERATE AWGN NOISE
# ==========================================

snr_db = 25

snr_linear = 10 ** (snr_db / 10)

noise_power = signal_power / snr_linear

noise = np.sqrt(noise_power / 2) * (
    np.random.randn(num_symbols)
    + 1j * np.random.randn(num_symbols)
)


# ==========================================
# 5. ADD NOISE TO TRANSMITTED SYMBOLS
# ==========================================

rx_symbols = tx_symbols + noise


# ==========================================
# 6. GENERATE MODULATED WAVEFORM
# ==========================================

fc = 5

samples_per_symbol = 100

t = np.arange(
    num_symbols * samples_per_symbol
) / samples_per_symbol

I = np.repeat(I_signal, samples_per_symbol)
Q = np.repeat(Q_signal, samples_per_symbol)

carrier_I = np.cos(2 * np.pi * fc * t)
carrier_Q = np.sin(2 * np.pi * fc * t)

qam_signal = (
    I * carrier_I - Q * carrier_Q
) / np.sqrt(10)


# ==========================================
# 7. ADD NOISE TO WAVEFORM
# ==========================================

waveform_power = np.mean(qam_signal ** 2)

waveform_noise_power = (
    waveform_power / snr_linear
)

waveform_noise = np.sqrt(
    waveform_noise_power
) * np.random.randn(len(t))

received_signal = qam_signal + waveform_noise


# ==========================================
# 8. DISPLAY ALL RESULTS
# ==========================================

plt.figure(figsize=(14, 10))

# Clean constellation
plt.subplot(2, 2, 1)

plt.scatter(
    tx_symbols.real,
    tx_symbols.imag,
    color='blue'
)

plt.title("Clean 16-QAM Constellation")
plt.xlabel("In-phase")
plt.ylabel("Quadrature")
plt.grid(True)
plt.axis('equal')


# Noisy constellation
plt.subplot(2, 2, 2)

plt.scatter(
    rx_symbols.real,
    rx_symbols.imag,
    color='red'
)

plt.title("16-QAM with AWGN Noise")
plt.xlabel("In-phase")
plt.ylabel("Quadrature")
plt.grid(True)
plt.axis('equal')


# Clean waveform
plt.subplot(2, 2, 3)

plt.plot(t[:1000], qam_signal[:1000])

plt.title("Transmitted 16-QAM Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)


# Received waveform
plt.subplot(2, 2, 4)

plt.plot(t[:1000], received_signal[:1000])

plt.title("Received Signal with AWGN")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)


plt.tight_layout()

# Create outputs folder
output_dir = Path(__file__).resolve().parent / "outputs"
output_dir.mkdir(exist_ok=True)

# Save all four graphs in one image
plt.savefig(
    output_dir / "awgn_analysis.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================
# 9. DISPLAY RESULTS
# ==========================================

print("\nAWGN SIMULATION RESULTS")

print("SNR:", snr_db, "dB")

print("Noise Power:", noise_power)

print("AWGN simulation completed successfully!")
