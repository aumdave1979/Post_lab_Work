import numpy as np
import matplotlib.pyplot as plt

def a():
    # Sampling details
    fs = 1000        # Sampling frequency (Hz)
    t = np.linspace(0, 1, fs, endpoint=False)  # Time vector (1 second, 1000 samples)

    # Frequencies
    f1 = 5   # Hz
    f2 = 10  # Hz

    # Generate sine waves
    sine1 = np.sin(2 * np.pi * f1 * t)   # 5 Hz sine wave
    sine2 = np.sin(2 * np.pi * f2 * t)   # 10 Hz sine wave

    # Add the two signals
    combined_signal = sine1 + sine2

    # Plot the signals
    plt.figure(figsize=(10,6))

    plt.subplot(3,1,1)
    plt.plot(t, sine1)
    plt.title("5 Hz Sine Wave")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")

    plt.subplot(3,1,2)
    plt.plot(t, sine2, color='orange')
    plt.title("10 Hz Sine Wave")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")

    plt.subplot(3,1,3)
    plt.plot(t, combined_signal, color='green')
    plt.title("Combined Signal (5 Hz + 10 Hz)")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.show()

def b():
    fs = 500       # Sampling frequency
    t = np.linspace(0, 2, 2*fs, endpoint=False)  # 2 seconds

    sine = np.sin(2 * np.pi * 5 * t)   # 5 Hz sine wave
    cosine = np.cos(2 * np.pi * 10 * t) # 10 Hz cosine wave

    multiplied = sine * cosine

    plt.figure(figsize=(8,4))
    plt.plot(t, multiplied, label="5Hz Sine × 10Hz Cosine")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.title("Multiplication of Sine (5Hz) and Cosine (10Hz)")
    plt.legend()
    plt.grid(True)
    plt.show()

def c():
    fs = 500
    t = np.linspace(0, 1, fs, endpoint=False)

    sine = np.sin(2 * np.pi * 5 * t)   # 5 Hz sine wave
    shifted = np.sin(2 * np.pi * 5 * (t - 0.1))  # Shifted by 0.1 sec

    plt.figure(figsize=(8,4))
    plt.plot(t, sine, label="Original")
    plt.plot(t, shifted, label="Shifted by 0.1s", linestyle="--")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.title("5 Hz Sine Wave (Original vs Shifted)")
    plt.legend()
    plt.grid(True)
    plt.show()

def d():
    fs = 500
    t = np.linspace(0, 1, fs, endpoint=False)

    sine = np.sin(2 * np.pi * 10 * t)   # 10 Hz sine wave
    scaled = 3 * sine                   # Amplitude scaled by 3

    plt.figure(figsize=(8,4))
    plt.plot(t, sine, label="Original (10Hz)")
    plt.plot(t, scaled, label="Scaled by 3", linestyle="--")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.title("10 Hz Sine Wave (Original vs Scaled)")
    plt.legend()
    plt.grid(True)
    plt.show()

def e():
    fs = 500
    t = np.linspace(0, 1, fs, endpoint=False)

    sine = np.sin(2 * np.pi * 5 * t)   # 5 Hz sine wave
    reversed_sine = sine[::-1]          # Reverse in time

    plt.figure(figsize=(8,4))
    plt.plot(t, sine, label="Original")
    plt.plot(t, reversed_sine, label="Reversed", linestyle="--")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.title("5 Hz Sine Wave (Original vs Reversed)")
    plt.legend()
    plt.grid(True)
    plt.show()

e()



