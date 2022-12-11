mkdir -p using_detectron2

mkdir -p using_yolov5
cd using_yolov5
git clone https://github.com/ultralytics/yolov5.git  # clone repo
conda create -p ./env python==3.8 -y
source activate ./env
cd yolov5
pip install -r requirements.txt  
pip install notebook
cd ../..
cd using_detectron2
conda create -p ./env python==3.8 -y
source activate ./env
pip install -r requirements.txt
pip install git+https://github.com/facebookresearch/detectron2.git
