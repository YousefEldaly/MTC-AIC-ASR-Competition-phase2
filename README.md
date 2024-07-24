# International Competition of the Military Technical College (AI Competition)

This README is based on the requirements of the “International Competition of the Military Technical College” AI competition. For more information, visit the following links:
- [MTC-AIC Overview](https://aic.conferences.ekb.eg/)

The provided dataset comprises 3 hours of audio recordings in the Egyptian Arabic dialect containing one or multiple speakers.

## Re-generate Submitted Results
To re-test the submitted model using the provided notebook, follow these steps:

1. **Download the Notebook:**
   - Go to [speaker-diarization-script.ipynb](https://github.com/YousefEldaly/MTC-AIC-ASR-Competition-phase2/blob/main/speaker-diarizarion-script.ipynb).
   - Click on the "Raw" button to download the notebook file.

2. **Upload to Kaggle:**
   - Sign in to your Kaggle account.
   - Navigate to "Kernels" and create a new notebook.
   - Upload the downloaded notebook file.

3. **Run the Notebook:**
   - Execute the notebook cells sequentially.
   - After execution, a file called `submission.zip` will be generated. Download this file to view the regenerated outputs.

## Steps Taken in the Model Pipeline

1. **Load the Dataset and Configuration:**
   - Prepare the manifest file containing audio file paths, durations, and transcriptions.
   - Set the output directory for storing results.

2. **Voice Activity Detection (VAD):**
   - Use a pre-trained VAD model to detect speech segments in the audio recordings.
   - Configure VAD parameters such as window length, shift length, and thresholds for speech detection.

3. **Speaker Embeddings Extraction:**
   - Use the Titanet Large model to extract speaker embeddings from detected speech segments.
   - Save the embeddings for later use in the clustering step.

4. **Clustering:**
   - Perform speaker clustering to group speech segments by speaker identity.
   - Configure parameters such as the maximum number of speakers and clustering thresholds.

5. **Multi-scale Diarization Decoder (MSDD):**
   - Use a pre-trained MSDD model to refine the clustering results and improve speaker diarization accuracy.
   - Configure MSDD parameters including batch size and sigmoid threshold.

6. **Automatic Speech Recognition (ASR):**
   - Use a trained QuartzNet model for ASR to transcribe the audio recordings.
   - Configure ASR parameters such as batch size and decoder settings.

7. **Output Generation:**
   - Combine the results from VAD, speaker embeddings, clustering, MSDD, and ASR.
   - Save the final diarization and transcription results to the specified output directory.

## Configuration File: offline_diarization_with_asr.yaml
The configuration file `offline_diarization_with_asr.yaml` will be generated during execution. It includes all necessary parameters for each step in the pipeline, such as model paths, batch sizes, and various thresholds.
