# TransUNet
This repo holds code for [TransUNet: Transformers Make Strong Encoders for Medical Image Segmentation](https://arxiv.org/pdf/2102.04306.pdf)

## Quick start with Docker
```bash
git@github.com:Enkrl-last/TransUNet.git
```
#### If u want to use already existed docker image u can download it by:
```bash
Somehow download docker image
```
#### If u want to build docker by yourself or make changes go to docker
```bash
cd Docker
docker build -t transunet .
```
#### For run docker container do next comman
```bash
docker container run -it --rm --gpus all transunet
```

## Usage of test data

### 1. Prepare environment for work (If u decide work w/o docker)
#### 1.1. Download repo
Our repo contain all necessary code except neural network model and example dataset
```bash
git clone https://github.com/Enkrl-last/TransUNet.git
```
#### 1.2. Download one of models.
**Default model is:** _R50+ViT-B_16.npz_

```bash
wget https://storage.googleapis.com/vit_models/imagenet21k/R50+ViT-B_16.npz &&
mkdir -p ../model/vit_checkpoint/imagenet21k &&
mv R50+ViT-B_16.npz ../model/vit_checkpoint/imagenet21k/R50+ViT-B_16.npz
```
Or use custom model:
[List of models](https://console.cloud.google.com/storage/vit_models/imagenet21k/): R50-ViT-B_16, ViT-B_16, ViT-L_16...
  R26+ViT-B_32.npz, R50+ViT-B_16.npz,  R50+ViT-L_32.npz,  ViT-B_16.npz, ViT-B_32.npz,
ViT-B_8.npz,  ViT-H_14.npz, ViT-L_16.npz,  ViT-L_32.npz.

```bash
wget https://storage.googleapis.com/vit_models/imagenet21k/{MODEL_NAME}.npz &&
mkdir -p ../model/vit_checkpoint/imagenet21k &&
mv {MODEL_NAME}.npz ../model/vit_checkpoint/imagenet21k/{MODEL_NAME}.npz
```
#### 1.3. Install requirements

Please prepare an environment with python=3.7.
```bash
python 3.7 ???
pip install -r requirements.txt
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

#### 2.1. Preprocess data
**Default model name:** R50+ViT-B_16

To train NN use:
```bash
CUDA_VISIBLE_DEVICES=0 python train.py --dataset Synapse --vit_name {MODEL_NAME_FROM_LIST}
```

#### 2.2. Preprocess data
**Default model name:** R50+ViT-B_16

To evaluate NN use:
```bash
python test.py --dataset Synapse --vit_name {MODEL_NAME_FROM_LIST}
```
## Modifications

### 1. Prepare environment for work (If u decide work w/o docker)
```bash
cd Docker
```

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
