# Digital Communication System Simulation Using Python

## Project Overview

This project focuses on the simulation and analysis of fundamental digital modulation techniques using Python. It demonstrates different digital modulation schemes, the effect of Additive White Gaussian Noise (AWGN), and the bit error rate (BER) performance of a 16-QAM system.

The project provides a simulation-based understanding of digital communication concepts through signal generation, modulation, noise analysis, constellation visualisation, and performance evaluation.

## Objectives

- Generate and visualise digital signals.
- Implement fundamental digital modulation techniques.
- Understand the effect of AWGN on transmitted signals.
- Visualise modulation waveforms and constellation diagrams.
- Analyse 16-QAM system performance using BER versus SNR.

## Modulation Techniques Implemented

The following modulation schemes are implemented:

1. Amplitude Shift Keying (ASK)
2. Frequency Shift Keying (FSK)
3. Binary Phase Shift Keying (BPSK)
4. Quadrature Phase Shift Keying (QPSK)
5. 16-Quadrature Amplitude Modulation (16-QAM)

## Tools and Technologies

- **Programming Language:** Python
- **Numerical Computation:** NumPy
- **Data Visualisation:** Matplotlib

## Noise Analysis

Additive White Gaussian Noise (AWGN) is implemented in a standalone simulation to demonstrate how channel noise affects a transmitted signal.

The simulation compares clean and noisy signal representations to illustrate the impact of noise on communication signals.

## BER Performance Analysis

A separate BER analysis is performed for the 16-QAM modulation scheme.

The simulation evaluates bit error rate at different Signal-to-Noise Ratio (SNR) levels and generates a BER versus SNR performance curve.

**Note:** BER analysis is implemented for 16-QAM only. The AWGN demonstration and BER experiment are separate simulations.

## Project Structure

- **Python source files:** Individual modulation and simulation implementations.
- **outputs/:** Generated simulation plots, constellation diagrams, and performance results.
- **README.md:** Project documentation.

## Simulation Results

The project generates visual results including:

- Digital modulation waveforms.
- 16-QAM constellation diagram.
- Clean and noisy signal comparison.
- 16-QAM BER versus SNR performance curve.

## Project Scope and Limitations

This project focuses on individual modulation simulations and separate noise and BER experiments. It does not implement a complete integrated transmitter-to-receiver communication chain.

Hardware implementation, Software Defined Radio (SDR) testing, channel coding, fading channel models, and synchronisation techniques are outside the current project scope.

## Conclusion

This project provides practical exposure to fundamental digital communication techniques through Python-based simulations. It demonstrates digital modulation methods, the influence of AWGN, and the performance evaluation of a 16-QAM system using BER analysis.

