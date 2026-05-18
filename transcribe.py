import whisper

print("Loading model...")

model = whisper.load_model("base")

result = model.transcribe("test.wav")

print("Recognized text:")
print(result["text"])