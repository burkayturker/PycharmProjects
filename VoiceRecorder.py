import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
seconds = 5

my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()
write('output.wav', fs, my_recording)


