#Manually download https://drive.google.com/u/0/uc?export=download&confirm=DOjP&id=1Y7frjVkB_85snZYHTn0PQQG_kC5afoYN
#wget https://mllp.upv.es/europarl-st/v1.1.tar.gz
#tar xvzf v1.1.tar.gz
conda env create -f environment.yml
conda activate shas
pip install librosa
git clone https://github.com/mt-upc/SHAS.git
git clone https://github.com/jairsan/Stream-level_Latency_Evaluation_for_Simultaneous_Machine_Translation.git
cd Stream-level_Latency_Evaluation_for_Simultaneous_Machine_Translation/
pip install .
