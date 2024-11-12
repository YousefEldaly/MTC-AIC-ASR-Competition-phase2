# MTC-AIC Speaker Diarization & ASR Pipeline

This project was developed for the **International Competition of the Military Technical College (AI Competition)**, focusing on speaker diarization and automatic speech recognition (ASR) in Egyptian Arabic audio recordings. The provided dataset includes 3 hours of audio featuring one or multiple speakers in the Egyptian dialect.

For more details on the competition, visit: [MTC-AIC Overview](https://aic.conferences.ekb.eg/)

## Pipeline Overview

The speaker diarization and ASR pipeline consists of the following steps:

![Pipeline Diagram](https://github.com/NVIDIA/NeMo/blob/main/tutorials/speaker_tasks/images/diar_pipeline.png)

1. **Input Speech**: The pipeline begins with raw audio input that may contain multiple speakers.

2. **Voice Activity Detection (VAD)**:

   - The **MarbleNet** model is used to detect segments containing speech. This step isolates speech regions from silence or background noise, helping focus on areas where speakers are active.
   - VAD settings include parameters like `window_length_in_sec` and `shift_length_in_sec`.

3. **Segmentation**:

   - After detecting speech, the audio is divided into segments to facilitate speaker embedding extraction and clustering in later stages.

4. **Speaker Embedding Extraction**:

   - The **TitaNet-L** model extracts unique speaker embeddings from each segment. These embeddings represent the voice characteristics of each speaker, aiding in distinguishing between different speakers.

5. **Clustering**:

   - In this step, segments are grouped by speaker identity based on the embeddings. Clustering configurations include settings for the expected number of speakers and thresholds for similarity.

6. **Neural Diarizer (MSDD)**:

   - The **Multi-scale Diarization Decoder (MSDD)** refines clustering results to improve speaker separation accuracy. This model ensures that each segment is accurately assigned to the correct speaker.

7. **Automatic Speech Recognition (ASR)**:

   - The **QuartzNet** model is used for transcribing the segmented audio. ASR generates text from the speaker-labeled audio, providing transcriptions for each identified speaker.

8. **Speaker Labels**:
   - Final output includes speaker labels assigned to each segment, along with the corresponding transcription. This enables easy identification of who spoke when and what they said.

## Steps Taken in the Model Pipeline

1. **Load Dataset and Configuration**:

   - Load audio file paths, durations, and transcriptions via a manifest file.
   - Define the output directory for storing results.

2. **Voice Activity Detection (VAD)**:

   - Run VAD to isolate speech regions. Adjust parameters for window length, shift length, and detection thresholds.

3. **Speaker Embeddings Extraction**:

   - Extract speaker embeddings with TitaNet-L. Save embeddings for clustering.

4. **Clustering**:

   - Group speech segments by speaker identity using clustering, setting the maximum number of speakers and clustering thresholds.

5. **MSDD Refinement**:

   - Use MSDD to refine clustering results, with batch size and sigmoid threshold configurations for enhanced accuracy.

6. **ASR with QuartzNet**:

   - Transcribe the audio with ASR, specifying batch size and decoder settings.

7. **Output Generation**:
   - Integrate results from all stages (VAD, embeddings, clustering, MSDD, ASR) and save final outputs in the defined directory.

## Re-generate Submitted Results

To replicate the submitted results using the provided notebook, follow these steps:

1. **Download the Notebook:**

   - Go to [speaker-diarization-script.ipynb](https://github.com/YousefEldaly/MTC-AIC-ASR-Competition-phase2/blob/main/speaker-diarization-script.ipynb).
   - Click the "Raw" button to download the file.

2. **Upload to Kaggle:**

   - Sign in to Kaggle, go to "Kernels," and create a new notebook.
   - Upload the downloaded notebook.

3. **Run the Notebook:**
   - Execute each cell in sequence.
   - After running, a `submission.zip` file will be generated. Download it to review the regenerated outputs.

## Configuration File: `offline_diarization_with_asr.yaml`

The configuration file, `offline_diarization_with_asr.yaml`, includes all parameter settings for each pipeline step, including model paths, batch sizes, and thresholds.

## Re-generate Submitted Conformer-CTC Results

To re-test the Conformer-CTC model:

1. **Download the Notebook**:

   - Go to [ctc-small-ctc-test-script.ipynb](https://github.com/YousefEldaly/MTC-AIC-ASR-Competition-phase2/blob/main/ctc-small-char-test-script.ipynb).
   - Click "Raw" to download the file.

2. **Upload to Kaggle**:

   - Sign in, create a new notebook, and upload the file.

3. **Run the Notebook**:
   - Run cells sequentially. A `submission.csv` file will be generated to review outputs.

---

This README provides a comprehensive overview of the steps in the pipeline, the models used, and instructions for re-generating results. Let me know if there’s anything you’d like to add or modify!
