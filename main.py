import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import ollama

duration = int(input("Enter recording time (sec): "))
sample_rate = 44100

print("Recording...")

audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype='int16'
)

sd.wait()

write("test.wav", sample_rate, audio)

print("Transcribing...")

model = whisper.load_model("base")
result = model.transcribe("test.wav")

question = result["text"]

print("You said:")
print(question)

print("\nGenerating answer...\n")

response = ollama.chat(
    model="phi3:mini",
    messages=[
        {"role": "user", "content": question}
    ]
)

print(response["message"]["content"])