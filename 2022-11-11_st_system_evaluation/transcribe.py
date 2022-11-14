import sys
import yaml
import torch
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import librosa


def transcribe(segmentation_yaml:str, audio_folder:str):

    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h-lv60").to("cuda")
    processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h-lv60", do_upper_case=False)

    with open(segmentation_yaml) as segmentation_file:
        items = yaml.safe_load(segmentation_file)
        for segment in items:
            audio_file = audio_folder + "/" + segment["wav"]
            waveform, _ = librosa.load(audio_file, sr=16000, offset=segment["offset"], duration=segment["duration"])
            features = processor(waveform, sampling_rate=16000, padding=True, return_tensors="pt")
            features = {key: value.to("cuda") for key, value in features.items()}

            logits = model(**features).logits

            predicted_ids = torch.argmax(logits, dim=-1)
            transcription = processor.batch_decode(predicted_ids)

            print(transcription[0].lower())


if __name__ == "__main__":
    transcribe(sys.argv[1], sys.argv[2])    
