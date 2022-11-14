BASE_DIR=$PWD/v1.1/
src=en
tgt=es
set=test

mkdir -p data_"$set"_raw

cat $BASE_DIR/$src/$tgt/$set/speeches.lst | while read speech;
do
    ffmpeg -i $BASE_DIR/$src/audios/$speech.m4a -nostdin -ac 1 -ar 16000 -hide_banner -loglevel error data_"$set"_raw/$speech.wav
done
