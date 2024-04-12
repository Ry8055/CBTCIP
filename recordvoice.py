# CipherByte Python Task 
# Voice Recorder 
# by --> Ravi Yadav 

import sounddevice as sd
from scipy.io.wavfile import write

# Set the sampling rate (in Hz)
fs = 44100

# Record audio
print("Recording...")
recorded_audio = sd.rec(int(fs), samplerate=fs, channels=2)
sd.wait()

# Save the recorded audio as a WAV file
write("recorded_audio.wav", fs, recorded_audio)

print("Recording complete. Audio saved as recorded_audio.wav")

# Ask if the user wants to play the recorded audio
play_audio = input("Do you want to play the recorded audio? (y/n): ")
if play_audio.lower() == "y":
    # Play back the recorded audio
    print("Playing recorded audio...")
    sd.play(recorded_audio, fs)
    sd.wait()
    print("Playback complete.")
else:
    print("Audio not played.")