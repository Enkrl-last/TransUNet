"""Install dependency"""
from setuptools import setup

setup(
    name="TransUNet",
    version='1.0',
    description='Python Distribution Utilities',
    install_requires=[
        "torch==1.4.0",
        "torchvision==0.5.0",
        "numpy~=1.19.5",
        "tqdm~=4.62.3",
        "tensorboard",
        "tensorboardX~=2.4",
        "ml-collections",
        "medpy~=0.4.0",
        "SimpleITK~=2.1.1",
        "scipy~=1.5.4",
        "h5py~=3.1.0",
        "synapseclient~=2.4.0",
        "nibabel~=3.2.1"]
)
