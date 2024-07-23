import os
import sys
from utils import collect_wav_files, create_manifest



def main(wavs_dir_path):
    # Ask user for the WAVs directory path
    if len(sys.argv) > 1:
        wavs_directory = sys.argv[1]

    if not os.path.isdir(wavs_directory):
        print("The specified WAVs directory does not exist. Exiting.")
        sys.exit(1)
    


    wav_files = collect_wav_files(wavs_directory)
    #long_wav_files = get_long_wav_files(wavs_directory)
    filename_to_remove = 'audio_sample_63.wav'

# Remove the specified file from the list
    wav_files = [file for file in wav_files if filename_to_remove not in os.path.basename(file)]



    root_directory = os.path.abspath(os.path.dirname(__file__))
    manifest_path = os.path.join(root_directory, "manifest.json")

    create_manifest(wav_files, manifest_path)
    print(f"Manifest file created at: {manifest_path}")


if __name__ == "__main__":
    main()
