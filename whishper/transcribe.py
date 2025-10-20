# import torch
# import librosa
# from transformers import WhisperProcessor, WhisperForConditionalGeneration

# # =====================================================
# # STEP 1: Load model and processor
# # =====================================================
# print("🔄 Loading model... please wait...")

# MODEL_NAME = "thennal/whisper-medium-ml"
# processor = WhisperProcessor.from_pretrained(MODEL_NAME)
# model = WhisperForConditionalGeneration.from_pretrained(MODEL_NAME)

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model.to(device)

# print("✅ Model loaded successfully!")

# # =====================================================
# # STEP 2: Define helper functions
# # =====================================================

# def load_audio(path, sr=16000):
#     """Loads an audio file and resamples to 16kHz"""
#     audio, _ = librosa.load(path, sr=sr)
#     return audio

# def transcribe_long_audio(audio, sr=16000, chunk_length_s=30, stride_length_s=5):
#     """
#     Splits long audio into overlapping chunks and transcribes each part using the updated generation config method.
#     """
#     # Set generation config directly on the model (new method)
#     model.config.language = "ml"         # Malayalam
#     model.config.task = "transcribe"     # Task: transcribe (not translate)

#     chunk_samples = int(chunk_length_s * sr)
#     stride_samples = int(stride_length_s * sr)
    
#     all_text = []
#     total_chunks = (len(audio) // (chunk_samples - stride_samples)) + 1

#     print(f"🔊 Total audio length: {len(audio)/sr:.1f} sec")
#     print(f"📏 Processing in chunks of {chunk_length_s}s with {stride_length_s}s overlap...")
#     print(f"🧩 Estimated {total_chunks} chunks...\n")

#     for i, start in enumerate(range(0, len(audio), chunk_samples - stride_samples)):
#         end = min(start + chunk_samples, len(audio))
#         chunk = audio[start:end]

#         # Convert to input features
#         inputs = processor(chunk, sampling_rate=sr, return_tensors="pt").input_features.to(device)

#         # Generate text for this chunk
#         with torch.no_grad():
#             predicted_ids = model.generate(
#                 inputs,
#                 max_new_tokens=444,  # stay under 448 limit
#                 do_sample=False,
#             )
        
#         text = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
#         all_text.append(text.strip())
#         print(f"✅ Chunk {i+1}/{total_chunks} done")

#         if end == len(audio):
#             break

#     return " ".join(all_text)

#     """
#     Splits long audio into overlapping chunks and transcribes each part.
#     """
#     forced_decoder_ids = processor.get_decoder_prompt_ids(language="ml", task="transcribe")
#     chunk_samples = int(chunk_length_s * sr)
#     stride_samples = int(stride_length_s * sr)
    
#     all_text = []
#     total_chunks = (len(audio) // (chunk_samples - stride_samples)) + 1

#     print(f"🔊 Total audio length: {len(audio)/sr:.1f} sec")
#     print(f"📏 Processing in chunks of {chunk_length_s}s with {stride_length_s}s overlap...")
#     print(f"🧩 Estimated {total_chunks} chunks...\n")

#     for i, start in enumerate(range(0, len(audio), chunk_samples - stride_samples)):
#         end = min(start + chunk_samples, len(audio))
#         chunk = audio[start:end]

#         # Convert to input features
#         inputs = processor(chunk, sampling_rate=sr, return_tensors="pt").input_features.to(device)

#         # Generate text for this chunk
#         with torch.no_grad():
#             predicted_ids = model.generate(
#                 inputs,
#                 forced_decoder_ids=forced_decoder_ids,
#                 max_new_tokens=444,
#                 do_sample=False,
#             )
        
#         text = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
#         all_text.append(text.strip())
#         print(f"✅ Chunk {i+1}/{total_chunks} done")

#         if end == len(audio):
#             break

#     return " ".join(all_text)

# # =====================================================
# # STEP 3: Run the transcription
# # =====================================================

# if __name__ == "__main__":
#     audio_path = "AUD-20251018-WA0000.m4a"  # your audio file
#     print("🎧 Loading audio...")
#     audio = load_audio(audio_path)

#     print("🧠 Transcribing in chunks...")
#     transcription = transcribe_long_audio(audio)

#     print("\n📝 Final Transcription (Malayalam):\n")
#     print(transcription)

#     # Save output to text file
#     with open("output_transcription.txt", "w", encoding="utf-8") as f:
#         f.write(transcription)

#     print("\n💾 Transcription saved as 'output_transcription.txt'")




# import torch
# import numpy as np
# from pydub import AudioSegment
# from transformers import WhisperProcessor, WhisperForConditionalGeneration
# import os

# # ✅ Point to your working FFmpeg folder
# os.environ["PATH"] += os.pathsep + r"C:\Program Files\ffmpeg-7.1.1-full_build\bin"
# from pydub.utils import which

# # 🧩 Check FFmpeg installation
# ffmpeg_path = which("ffmpeg")
# ffprobe_path = which("ffprobe")

# if ffmpeg_path and ffprobe_path:
#     print(f"✅ FFmpeg found: {ffmpeg_path}")
#     print(f"✅ FFprobe found: {ffprobe_path}")
# else:
#     print("❌ FFmpeg or FFprobe not found. Please verify the path below:")
#     print("   C:\\Program Files\\ffmpeg-7.1.1-full_build\\bin")


# # =====================================================
# # STEP 1: Load model and processor
# # =====================================================
# print("🔄 Loading model... please wait...")

# MODEL_NAME = "thennal/whisper-medium-ml"
# processor = WhisperProcessor.from_pretrained(MODEL_NAME)
# model = WhisperForConditionalGeneration.from_pretrained(MODEL_NAME)

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model.to(device)

# print("✅ Model loaded successfully!")

# # =====================================================
# # STEP 2: Define helper functions
# # =====================================================

# def load_audio(path, sr=16000):
#     """
#     Loads an audio file (any format supported by ffmpeg) and converts it to 16kHz mono.
#     Returns a normalized NumPy array of samples.
#     """
#     try:
#         audio = AudioSegment.from_file(path)
#         audio = audio.set_frame_rate(sr).set_channels(1)

#         print(f"🎵 Loaded audio: {path}")
#         print(f"   Duration: {len(audio) / 1000:.2f}s, Sample Rate: {audio.frame_rate} Hz")

#         samples = np.array(audio.get_array_of_samples()).astype(np.float32)
#         samples /= np.iinfo(audio.array_type).max  # normalize between -1 and 1
#         return samples

#     except Exception as e:
#         print(f"❌ Failed to load audio: {e}")
#         raise


# def transcribe_long_audio(audio, sr=16000, chunk_length_s=30, stride_length_s=5):
#     """
#     Splits long audio into overlapping chunks and transcribes each part.
#     """
#     model.config.language = "ml"       # Malayalam
#     model.config.task = "transcribe"   # Task: Transcribe (not translate)

#     chunk_samples = int(chunk_length_s * sr)
#     stride_samples = int(stride_length_s * sr)
    
#     all_text = []
#     total_chunks = (len(audio) // (chunk_samples - stride_samples)) + 1

#     print(f"🔊 Total audio length: {len(audio)/sr:.1f} sec")
#     print(f"📏 Processing in chunks of {chunk_length_s}s with {stride_length_s}s overlap...")
#     print(f"🧩 Estimated {total_chunks} chunks...\n")

#     for i, start in enumerate(range(0, len(audio), chunk_samples - stride_samples)):
#         end = min(start + chunk_samples, len(audio))
#         chunk = audio[start:end]

#         inputs = processor(chunk, sampling_rate=sr, return_tensors="pt").input_features.to(device)

#         with torch.no_grad():
#             predicted_ids = model.generate(inputs, max_new_tokens=444, do_sample=False)

#         text = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
#         all_text.append(text.strip())
#         print(f"✅ Chunk {i+1}/{total_chunks} done")

#         if end == len(audio):
#             break

#     return " ".join(all_text)

# # =====================================================
# # STEP 3: Run the transcription
# # =====================================================

# if __name__ == "__main__":
#     audio_path = "07_F_set_01_004.wav"  # Change to your file name

#     print("🎧 Loading audio...")
#     audio = load_audio(audio_path)

#     print("🧠 Transcribing in chunks...")
#     transcription = transcribe_long_audio(audio)

#     print("\n📝 Final Transcription (Malayalam):\n")
#     print(transcription)

#     # Save output to text file
#     with open("output_transcription.txt", "w", encoding="utf-8") as f:
#         f.write(transcription)

#     print("\n💾 Transcription saved as 'output_transcription.txt'")



import torch
import numpy as np
from pydub import AudioSegment
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import os
import re
from pydub.utils import which

# =====================================================
# ✅ FFmpeg setup
# =====================================================
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin\ffmpeg.exe"

ffmpeg_path = which("ffmpeg")
ffprobe_path = which("ffprobe")

if ffmpeg_path and ffprobe_path:
    print(f"✅ FFmpeg found: {ffmpeg_path}")
    print(f"✅ FFprobe found: {ffprobe_path}")
else:
    raise EnvironmentError(
        "❌ FFmpeg or FFprobe not found. Update PATH or set AudioSegment.converter/ffprobe."
    )

AudioSegment.converter = ffmpeg_path
AudioSegment.ffprobe = ffprobe_path

# =====================================================
# STEP 1: Load Whisper model
# =====================================================
print("🔄 Loading model... please wait...")
MODEL_NAME = "thennal/whisper-medium-ml"
processor = WhisperProcessor.from_pretrained(MODEL_NAME)
model = WhisperForConditionalGeneration.from_pretrained(MODEL_NAME)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
print("✅ Model loaded successfully!")

# =====================================================
# STEP 2: Helper functions
# =====================================================
def load_audio(path, sr=16000):
    """
    Load any audio format, convert to 16kHz mono, return normalized numpy array.
    """
    try:
        audio = AudioSegment.from_file(path)
        audio = audio.set_frame_rate(sr).set_channels(1)

        print(f"🎵 Loaded audio: {path}")
        print(f"   Duration: {len(audio) / 1000:.2f}s, Sample Rate: {audio.frame_rate} Hz")

        samples = np.array(audio.get_array_of_samples()).astype(np.float32)
        samples /= np.iinfo(audio.array_type).max  # normalize -1 to 1
        return samples
    except Exception as e:
        raise RuntimeError(f"❌ Failed to load audio: {e}")

def deduplicate_overlap(text, overlap_chars=50):
    """
    Remove repeated text caused by overlapping chunks.
    Keeps only the new part after the first occurrence.
    """
    if len(text) <= overlap_chars:
        return text
    return text[overlap_chars:]  # simple removal of first overlapping chars

def transcribe_long_audio(audio, sr=16000, chunk_length_s=60, stride_length_s=15):
    """
    Split audio into overlapping chunks, transcribe each, deduplicate overlaps.
    """
    model.config.language = "ml"       # Malayalam
    model.config.task = "transcribe"   # Transcribe only

    chunk_samples = int(chunk_length_s * sr)
    stride_samples = int(stride_length_s * sr)

    all_text = []
    total_chunks = (len(audio) // (chunk_samples - stride_samples)) + 1

    print(f"🔊 Total audio length: {len(audio)/sr:.1f} sec")
    print(f"📏 Processing chunks of {chunk_length_s}s with {stride_length_s}s overlap...")
    print(f"🧩 Estimated {total_chunks} chunks\n")

    for i, start in enumerate(range(0, len(audio), chunk_samples - stride_samples)):
        end = min(start + chunk_samples, len(audio))
        chunk = audio[start:end]

        print(f"⏱ Chunk {i+1}/{total_chunks}: {start/sr:.1f}s → {end/sr:.1f}s")

        inputs = processor(chunk, sampling_rate=sr, return_tensors="pt").input_features.to(device)

        with torch.no_grad():
            predicted_ids = model.generate(
                inputs, 
                max_new_tokens=400,  # allow longer chunks
                do_sample=False
            )

        text = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0].strip()

        # Deduplicate overlapping text (except for first chunk)
        if i > 0:
            text = deduplicate_overlap(text, overlap_chars=int(stride_length_s * sr / 160))  # approx chars

        all_text.append(text)

        if end == len(audio):
            break

    final_text = " ".join(all_text)

    # Optional: clean repeated sequences caused by overlaps
    final_text = re.sub(r'\b(\w+ \w+ \w+)\b(?=.*\1)', '', final_text)

    return final_text

# =====================================================
# STEP 3: Run transcription
# =====================================================
if __name__ == "__main__":
    audio_path = r"a.wav"  # Change to your audio file

    print("🎧 Loading audio...")
    audio = load_audio(audio_path)

    print("🧠 Transcribing in chunks...")
    transcription = transcribe_long_audio(audio)

    print("\n📝 Final Transcription (Malayalam):\n")
    print(transcription)

    # Save to file
    output_file = "output_transcription.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(transcription)

    print(f"\n💾 Transcription saved as '{output_file}'")

