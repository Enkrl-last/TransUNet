FROM ubuntu:20.04


RUN apt-get update
RUN apt-get install -y git
RUN git clone https://github.com/Enkrl-last/TransUNet

RUN apt install python3-pip -y
RUN python3 -m pip install --upgrade pip
RUN apt-get update && apt-get install wget

WORKDIR /TransUNet

RUN mkdir -p ./model/vit_checkpoint/imagenet21k && cd model/vit_checkpoint/imagenet21k/ && wget https://storage.googleapis.com/vit_models/imagenet21k/R50+ViT-B_16.npz && cd ../../..

RUN mkdir -p ./data/Synapse/{test_vol_h5,train_npz}

RUN mkdir -p ./model/vit_checkpoint/imagenet21k && cd model/vit_checkpoint/imagenet21k/ && wget https://storage.googleapis.com/vit_models/imagenet21k/R50+ViT-B_16.npz && cd ../../..


RUN pip install -r requirements.txt	
