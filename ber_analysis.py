import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Basic settings
np.random.seed(42)

num_symbols = 20000
bits_per_symbol = 4

# Gray-coded 16-QAM mapping
mapping = {
    (0, 0): -3,
    (0, 1): -1,
    (1, 1):  1,
    (1, 0):  3
}

reverse_mapping = {
    -3: (0, 0),
    -1: (0, 1),
     1: (1, 1),
     3: (1, 0)
}

levels = np.array([-3, -1, 1, 3])
bit_pairs = np.array([
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0]
])

# 2. Generate random bits
bits = np.random.randint(
    0, 2, num_symbols * bits_per_symbol
)

bit_groups = bits.reshape(-1, 4)

# 3. 16-QAM modulation
I_signal = np.array([
    mapping[tuple(pair)] for pair in bit_groups[:, :2]
])

Q_signal = np.array([
    mapping[tuple(pair)] for pair in bit_groups[:, 2:]
])

tx_symbols = (I_signal + 1j * Q_signal) / np.sqrt(10)

signal_power = np.mean(np.abs(tx_symbols)**2)

# 4. Test different SNR values
snr_values = np.arange(0, 22, 2)
ber_values = []

for snr_db in snr_values:

    snr_linear = 10**(snr_db / 10)
    noise_power = signal_power / snr_linear

    noise = np.sqrt(noise_power / 2) * (
        np.random.randn(num_symbols)
        + 1j * np.random.randn(num_symbols)
    )

    rx_symbols = tx_symbols + noise

    # 5. Demodulation: find nearest constellation levels
    normalized_levels = levels / np.sqrt(10)

    i_indices = np.argmin(
        np.abs(
            rx_symbols.real[:, None]
            - normalized_levels[None, :]
        ),
        axis=1
    )

    q_indices = np.argmin(
        np.abs(
            rx_symbols.imag[:, None]
            - normalized_levels[None, :]
        ),
        axis=1
    )

    # Convert detected levels back into bits
    i_bits = bit_pairs[i_indices]
    q_bits = bit_pairs[q_indices]

    received_bits = np.column_stack(
        (i_bits, q_bits)
    ).reshape(-1)

    # 6. Calculate BER
    errors = np.sum(bits != received_bits)
    ber = errors / len(bits)

    ber_values.append(ber)

    print(
        f"SNR: {snr_db:2d} dB | "
        f"Errors: {errors:5d} | BER: {ber:.6f}"
    )

# 7. Plot BER versus SNR
plt.figure(figsize=(8, 5))

plt.semilogy(
    snr_values,
    ber_values,
    marker="o",
    label="16-QAM"
)

plt.xlabel("SNR (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.title("16-QAM: BER vs SNR")
plt.grid(True, which="both")
plt.legend()

plt.tight_layout()

# Save output graph
output_dir = Path(__file__).resolve().parent / "outputs"
output_dir.mkdir(exist_ok=True)

plt.savefig(
    output_dir / "ber_analysis.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nBER analysis completed successfully!")
