from omegaconf import OmegaConf

from nemo.collections.asr.parts.utils.decoder_timestamps_utils import ASRDecoderTimeStamps
from nemo.collections.asr.parts.utils.diarization_utils import OfflineDiarWithASR
from nemo.collections.asr.models import EncDecCTCModel
from nemo.core.config import hydra_runner
from nemo.utils import logging
import torch

@hydra_runner(config_path="../", config_name="configs.yaml")
def main(cfg):

    logging.info(f'Hydra config: {OmegaConf.to_yaml(cfg)}')

    # ASR inference for words and word timestamps
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        logging.info("Cleared CUDA cache.")
            
    asr_decoder_ts = ASRDecoderTimeStamps(cfg.diarizer)
    asr_model = asr_decoder_ts.set_asr_model()
            
    word_hyp, word_ts_hyp = asr_decoder_ts.run_ASR(asr_model)

    # Create a class instance for matching ASR and diarization results
    asr_diar_offline = OfflineDiarWithASR(cfg.diarizer)
    asr_diar_offline.word_ts_anchor_offset = asr_decoder_ts.word_ts_anchor_offset

    # Diarization inference for speaker labels
    diar_hyp, diar_score = asr_diar_offline.run_diarization(cfg, word_ts_hyp)
    trans_info_dict = asr_diar_offline.get_transcript_with_speaker_labels(diar_hyp, word_hyp, word_ts_hyp)

    # If RTTM is provided and DER evaluation
    if diar_score is not None:
        # Get session-level diarization error rate and speaker counting error
        der_results = OfflineDiarWithASR.gather_eval_results(
            diar_score=diar_score,
            audio_rttm_map_dict=asr_diar_offline.AUDIO_RTTM_MAP,
            trans_info_dict=trans_info_dict,
            root_path=asr_diar_offline.root_path,
        )

        # Calculate WER and cpWER if reference CTM files exist
        wer_results = OfflineDiarWithASR.evaluate(
            hyp_trans_info_dict=trans_info_dict,
            audio_file_list=asr_diar_offline.audio_file_list,
            ref_ctm_file_list=asr_diar_offline.ctm_file_list,
        )

        # Print average DER, WER and cpWER
        OfflineDiarWithASR.print_errors(der_results=der_results, wer_results=wer_results)

        # Save detailed session-level evaluation results in `root_path`.
        OfflineDiarWithASR.write_session_level_result_in_csv(
            der_results=der_results,
            wer_results=wer_results,
            root_path=asr_diar_offline.root_path,
            csv_columns=asr_diar_offline.csv_columns,
        )


if __name__ == '__main__':
    main()