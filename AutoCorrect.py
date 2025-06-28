#correct the transcription using a spell checker**
 corrected_text = correct_text(transcribed_text)

 print("\n Transcription:\n", corrected_text)

# Save transcription
transcription_filename = f"/content/sample_data/transcription.txt"
with open(transcription_filename, "w", encoding="utf-8") as f:
    # f.write(corrected_text)
    f.write(transcribed_text)

print(f"\n Transcription saved to {transcription_filename}")
