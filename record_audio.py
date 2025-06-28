import sounddevice as sd
import wave
import ffmpeg

# Configuration
samplerate = 16000
channels = 1
blocksize = 1024
audio_filename = "recorded_audio.wav"
converted_audio_filename = "converted_audio.wav"

def record_audio():
    """🎤 Record audio until the user stops (CTRL + C)."""
    print("🎤 Recording... Press CTRL + C to stop.")
    frames = []
    
    
    with sd.InputStream(samplerate=samplerate, channels=channels, dtype='int16', blocksize=blocksize) as stream:
        try:
            while True:
                data, overflowed = stream.read(blocksize)
                if overflowed:
                    print("⚠️ Buffer overflow! Adjust settings.")
                frames.append(data.copy())
        except KeyboardInterrupt:
            pass

    with wave.open(audio_filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(b''.join(frames))

    print(f"✅ Recording saved as {audio_filename}")

def convert_audio_format():
    """🎵 Convert to 16kHz mono WAV for best Whisper results."""
    print("\n🔄 Converting audio to correct format...")
    try:
        ffmpeg.input(audio_filename).output(converted_audio_filename, ar=16000, ac=1).run(overwrite_output=True, quiet=True)
        print(f"✅ Audio converted to {converted_audio_filename}")
    except Exception as e:
        print(f"❌ Audio conversion failed: {e}")

if __name__ == "__main__":
    record_audio()
    convert_audio_format()
  
