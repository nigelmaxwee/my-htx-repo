from fastapi import FastAPI, File, UploadFile
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
import soundfile as sf
import io
import librosa
import numpy as np
import os
import tempfile

app = FastAPI()

# Load ASR Model
model_name = "facebook/wav2vec2-large-960h"
processor = Wav2Vec2Processor.from_pretrained(model_name)
model = Wav2Vec2ForCTC.from_pretrained(model_name)

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/asr")
async def transcribe_audio(file: UploadFile = File(...)):
    temp_filename = None
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            temp_filename = temp_file.name
            temp_file.write(await file.read())

        # Load audio
        audio_data, sample_rate = sf.read(temp_filename, dtype="float32")

        # Convert stereo to mono
        if len(audio_data.shape) > 1:
            audio_data = np.mean(audio_data, axis=1)

        # Resample if needed
        if sample_rate != 16000:
            audio_data = librosa.resample(audio_data, orig_sr=sample_rate, target_sr=16000)

        # Normalize waveform
        audio_data = audio_data / np.max(np.abs(audio_data))

        # Process audio with ASR model
        inputs = processor(audio_data.astype("float32"), sampling_rate=16000, return_tensors="pt", padding=True)
        with torch.no_grad():
            logits = model(inputs.input_values).logits

        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = processor.batch_decode(predicted_ids)[0]

        # Get audio duration
        duration = round(len(audio_data) / 16000, 2)

        return {"transcription": transcription, "duration": duration}

    finally:
        # ✅ Delete the temporary file after processing
        if temp_filename and os.path.exists(temp_filename):
            os.remove(temp_filename)
