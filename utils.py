import os
import json
from pydub import AudioSegment

def collect_wav_files(directory):
    wav_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.wav'):
                wav_files.append(os.path.join(root, file))
    return wav_files

def create_manifest(wav_files, manifest_file, ignore_files=None):
    if ignore_files is None:
        ignore_files = []

    manifest_entries = []
    for wav_file in wav_files:
        # Check if the file is in the ignore list
        if os.path.basename(wav_file) in ignore_files:
            print(f"file {wav_file} exceeds 8 minutes and will be ignored")
            continue
        
        manifest_entry = {
            "audio_filepath": wav_file,
            "offset": 0,
            "duration": None,
            "label": "infer",
            "text": "-",
            "num_speakers": None,
            "rttm_filepath": "/path/to/rttm/file",
            "uem_filepath": "/path/to/uem/filepath"
        }
        manifest_entries.append(manifest_entry)
    
    with open(manifest_file, 'w') as f:
        for entry in manifest_entries:
            json.dump(entry, f)
            f.write('\n')


def split_wav_file(file_path, output_directory):
    """Split the WAV file into smaller chunks."""
    print(f"Splitting WAV file: {file_path}")

    # Load the audio file
    audio = AudioSegment.from_wav(file_path)
    
    # Define chunk duration (e.g., 1 minute)
    chunk_length_ms = 60 * 1000  # 1 minute in milliseconds

    # Split the audio file
    for i, start in enumerate(range(0, len(audio), chunk_length_ms)):
        chunk = audio[start:start + chunk_length_ms]
        chunk_filename = os.path.join(output_directory, f"chunk_{i + 1}.wav")
        chunk.export(chunk_filename, format="wav")
        print(f"Created chunk: {chunk_filename}")


def get_long_wav_files(directory, min_duration_minutes=8):
    long_files = []
    min_duration_ms = min_duration_minutes * 60 * 1000  # Convert minutes to milliseconds

    for filename in os.listdir(directory):
        if filename.endswith(".wav"):
            file_path = os.path.join(directory, filename)
            try:
                audio = AudioSegment.from_wav(file_path)
                duration_ms = len(audio)  # Duration in milliseconds
                if duration_ms > min_duration_ms:
                    long_files.append(file_path)
            except Exception as e:
                print(f"Could not process file {filename}: {e}")

    return long_files
