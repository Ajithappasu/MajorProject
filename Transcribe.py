import  whisper
import torch
import os
import soundfile as sf
import noisereduce as nr
from symspellpy import SymSpell, Verbosity
from pydub import AudioSegment
import numpy as np
# import pkg_resources
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model_size = "turbo"  # Best balance of speed & accuracy
device = "cuda" if torch.cuda.is_available() else "cpu"
fp16 = True if device == "cuda" else False
print(f"\n🔄 Loading Whisper model ({model_size}) on {device.upper()}...")
model = whisper.load_model(model_size, device=device)
print("✅ Whisper model loaded successfully.")
cleaned_audio = "/content/sample_data/converted_audio.wav"

with torch.inference_mode():
    result = model.transcribe(
        cleaned_audio,
        temperature=0.0,
        beam_size=10,
        best_of=10,
        fp16=fp16,
        suppress_tokens=[-1],  # Prevents hallucinations
        language=None  # Auto-detect language
    )

detected_lang = result.get("language", "unknown")
transcribed_text = result.get("text", "").strip()
print(detected_lang)
print(f"Transcribed Text:{transcribed_text}")
# **Correct the transcription using a spell checker**
 corrected_text = correct_text(transcribed_text)
+ print("\n Transcription:\n", corrected_text)

# Save transcription
transcription_filename = f"/content/sample_data/transcription.txt"
with open(transcription_filename, "w", encoding="utf-8") as f:
    # f.write(corrected_text)
    f.write(transcribed_text)

print(f"\n Transcription saved to {transcription_filename}")
