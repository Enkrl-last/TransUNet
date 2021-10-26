# TransUNet
This repo holds code for [TransUNet: Transformers Make Strong Encoders for Medical Image Segmentation](https://arxiv.org/pdf/2102.04306.pdf)

## Quick start with Docker
```bash
git clone git@github.com:Enkrl-last/TransUNet.git
```
#### If u want to use already existed docker image u can download it by:
```bash
docker pull 1223ssaw/transunet:2.0
sudo docker run -it --rm --gpus all transunet
```
#### If u want to build docker by yourself or make changes go to
```bash
cd docker
sudo docker build -t transunet .
sudo docker run -it --rm --gpus all transunet
```
After that, you must follow the instructions described in 2.
## Usage of test data

### 1. Prepare environment for work (If u decide work w/o docker)
#### 1.1. Download repo
Our repo contain all necessary code except neural network model and example dataset
```bash
git clone git@github.com:Enkrl-last/TransUNet.git
```
#### 1.2. Download one of models.
**Default model is:** _R50+ViT-B_16.npz_

```bash
mkdir -p ./Training-Testing/Reg-Training-Testing/Training-Testing/{img,label}
mkdir -p ./data/Synapse/{test_vol_h5,train_npz} 
mkdir -p ./model/vit_checkpoint/imagenet21k
cd model/vit_checkpoint/imagenet21k/
wget https://storage.googleapis.com/vit_models/imagenet21k/R50+ViT-B_16.npz
cd ../../..
```

#### 1.3. Install requirements

Please prepare an environment with python>=3.7.
```bash
pip install -r requirements.txt
```
or
```bash
sudo python3 setup.py install
```
### 2. Prepare dataset example for work

**Note:** Dataset weight is 15 GB!

To reproduce the results, you can use the dataset from the [official Synapse website](https://www.synapse.org/#!Synapse:syn3193805/wiki/). 
To do this, you need to register on it and take part in the project.
After that, you need to run a sequence of scripts that download data from the site and perform preprocessing.

#### 2.1 Download data
To download data use:
```bash
python3 data_processing_scripts/get_data.py
```

#### 2.2. Preprocess data
To preprocess data use:
```bash
python3 data_processing_scripts/preprocess_data.py
```

### 3. Train and Test
As an example, to train and test neural network, you can use a commands with preset parameters:

#### 3.1. Train

```bash
CUDA_VISIBLE_DEVICES=0 python3 train.py --dataset Synapse --vit_name R50+ViT-B_16 --batch_size=4 --max_epochs=5
```

#### 3.2. Test

To evaluate NN use:
```bash
python3 test.py --dataset Synapse --vit_name R50+ViT-B_16 --max_epoch 5 --batch_size 4
```

## Modifications

### 1. Prepare environment for work (If u decide work w/o docker)
#### 1.1. Download repo
Our repo contain all necessary code except neural network model and example dataset
```bash
git clone git@github.com:Enkrl-last/TransUNet.git
```
#### 1.2. Download one of models.

You can use any of  [custom models](https://console.cloud.google.com/storage/vit_models/imagenet21k/):
R50+ViT-B_16, ViT-B_16, ViT-L_16,
  R26+ViT-B_32.npz, R50+ViT-B_16.npz,  R50+ViT-L_32.npz,  ViT-B_16.npz, ViT-B_32.npz,
ViT-B_8.npz,  ViT-H_14.npz, ViT-L_16.npz,  ViT-L_32.npz or add it by yourself.

```bash
mkdir -p ./Training-Testing/Reg-Training-Testing/Training-Testing/{img,label}
mkdir -p ./data/Synapse/{test_vol_h5,train_npz}
mkdir -p ./model/vit_checkpoint/imagenet21k
cd model/vit_checkpoint/imagenet21k/
wget https://storage.googleapis.com/vit_models/imagenet21k/{MODEL_NAME}.npz
```

### 2. Prepare dataset example for work

#### 2.1. Data preprocessing:
Put your img files to /Training-Testing/Reg-Training-Testing/Training-Testing/img
and label files to /Training-Testing/Reg-Training-Testing/Training-Testing/label and launch: 
```bash
python3 data_processing_scripts/preprocess_data.py
```

### 3. Train and Test
**Note:** Training and testing parameters must be the same
#### 3.1. Preprocess data
You can set the parameters for training and testing by yourself. 
```bash
CUDA_VISIBLE_DEVICES=0 python3 train.py --dataset Synapse --vit_name {MODEL_NAME_FROM_LIST}
```
#### 3.2. Preprocess data

```bash
python test.py --dataset Synapse --vit_name {MODEL_NAME_FROM_LIST}
```

## Afterword
When creating download scripts, we were able to successfully download and process files from the Synapse website, but at the moment there are problems with access to the client and we were unable to reproduce the results.
For example, we attach a small sample, which we left in the github, in order to evaluate the work of train and test scripts.
![img.png](img.png)

## Reference
* [TransUNet](https://github.com/google-research/vision_transformer)
* [Google ViT](https://github.com/google-research/vision_transformer)
* [ViT-pytorch](https://github.com/jeonsworld/ViT-pytorch)
* [segmentation_models.pytorch](https://github.com/qubvel/segmentation_models.pytorch)

## Citations

```bibtex
@article{chen2021transunet,
  title={TransUNet: Transformers Make Strong Encoders for Medical Image Segmentation},
  author={Chen, Jieneng and Lu, Yongyi and Yu, Qihang and Luo, Xiangde and Adeli, Ehsan and Wang, Yan and Lu, Le and Yuille, Alan L., and Zhou, Yuyin},
  journal={arXiv preprint arXiv:2102.04306},
  year={2021}
}
```

## Disclaimer

*“This repository is not an original official implementation of the work, but a refactored codebase. Performed within the FSE coursework at Skoltech.”*
