import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np

# Load audio file
audio, sample_rate = sf.read(r"C:\Users\aumda\OneDrive\Desktop\clg_stuff\sem-3\python\data_sets_for_lab\testing.opus")

# Save as WAV (optional)
sf.write("converted_audio.wav", audio, sample_rate)

# Create time axis
time = np.arange(0, len(audio)) / sample_rate

# Plot audio signal
plt.figure(figsize=(10, 4))
plt.plot(time, audio)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Audio Signal Waveform")
plt.grid(True)
plt.show()
