import sounddevice as sd
from scipy.io.wavfile import write
duration = int(input("How many seconds to record: "))
#duration = 5          # seconds
sample_rate = 44100   # quality

print("Recording starts now...")

audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype='int16'
)

sd.wait()

write("test.wav", sample_rate, audio)

print("Recording saved as test.wav")