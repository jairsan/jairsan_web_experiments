AUDIO_LOC=$PWD/data_test_raw
SHAS_ROOT=$PWD/SHAS
out_folder=$PWD/data_test_segmented
path_to_wavs=$AUDIO_LOC/

set=test
maxlen=10;
path_to_custom_segmentation_yaml=$out_folder/maxlen"$maxlen"_segmentation.yaml

thres=0.3

python3 ${SHAS_ROOT}/src/supervised_hybrid/segment.py \
  -wavs $path_to_wavs \
  -yaml $path_to_custom_segmentation_yaml \
  --dac_threshol $thres \
  -ckpt en_sfc_model_epoch-6.pt \
  -max $maxlen

