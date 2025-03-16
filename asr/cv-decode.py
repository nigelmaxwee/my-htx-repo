import os
import pandas as pd
import requests

# Dataset configuration
DATASET_NAME = "cv-valid-dev"

# Define paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  
DATA_DIR = os.path.join(BASE_DIR, "data", DATASET_NAME)
CSV_FILE = os.path.join(BASE_DIR, "data", f"{DATASET_NAME}.csv")
OUTPUT_CSV = os.path.join(BASE_DIR, "asr", f"{DATASET_NAME}.csv")

if not os.path.exists(CSV_FILE):
    raise FileNotFoundError(f"CSV file not found: {CSV_FILE}")

df = pd.read_csv(CSV_FILE)
API_URL = "http://localhost:8001/asr"

transcriptions = []
durations = []

for _, row in df.iterrows():
    audio_path = os.path.join(DATA_DIR, row["filename"])

    if os.path.exists(audio_path):
        print(f"Processing: {row['filename']}...")

        if not row["filename"].endswith(".mp3"):
            print(f"Skipping {row['filename']}: Not an MP3 file")
            transcriptions.append("INVALID FILE FORMAT")
            durations.append(None)
            continue

        with open(audio_path, "rb") as f:
            response = requests.post(API_URL, files={"file": f})

        if response.status_code == 200:
            result = response.json()
            transcriptions.append(result.get("transcription", "ERROR"))
            durations.append(result.get("duration", None))
        else:
            print(f"Error processing {row['filename']}: {response.text}")
            transcriptions.append("ERROR")
            durations.append(None)
    else:
        print(f"File not found: {row['filename']}")
        transcriptions.append("MISSING")
        durations.append(None)

df["generated_text"] = transcriptions
df["duration"] = durations

os.makedirs(os.path.join(BASE_DIR, "asr"), exist_ok=True)
df.to_csv(OUTPUT_CSV, index=False)

print(f"Transcriptions saved to {OUTPUT_CSV}")
