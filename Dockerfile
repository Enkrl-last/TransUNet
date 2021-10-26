FROM nvidia/cuda:9.2-devel-ubuntu18.04


RUN apt-get update
RUN apt-get install -y git
RUN git clone https://github.com/Enkrl-last/TransUNet

RUN apt install python3-pip -y
RUN python3 -m pip install --upgrade pip

WORKDIR /TransUNet

RUN pip install -r requirements.txt