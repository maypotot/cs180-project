# Potato Disease Classifier 

This readme contains instructions for two models

Note: Training the models will use the GPU and will use it at maximum power, suggesting for good ventilation and airconditioned room.

Note: Please Run these ipynb files at vscode not at collab
-------------------------------------------------
## Description of Modal A - deeplearning_cnn.ipynb
A ResNet50 CNN from scratch (Pretrained = False), tuned to classify 6 types of potato leaf disease 

## Versions:
Python 12.0-13.0 

## Installation:
pip install tabulate
pip install torch torchvision torchaudio --index-url://download.pytorch.org/whl/cu118
pip install opencv-python
pip install matplotlib
pip install tqdm
pip install transformers
pip install matplot
pip install scikit-learn
pip install torch
pip install pandas


## Instructions:
1. Open python and use Virtual Environment by running python -m venv venv
2. Select your python version using the recommended above
3. Install all needed dependencies and packages above
4. Now you can Click Run All
5. Wait for training which can take up to 40 minutes
6. It will notify once it is done and the model will be saved as "deeplearning_cnn.pt"

## Instructions to run demo_deeplearning_cnn.ipynb
1. Make sure you installed all packages and dependencies
2. Find the variables:
 "image_dir" - makesure this is the file name of the file folder of the tests
 "model_path" - makesure this is the file name of the model, (usually "deeplearning_cnn.pt")
3. Once changed to the correct file, click Run All
4. Wait for the print to ensure that predictions is already done and saved in the csv "deeplearning_cnn_predictions.csv"
-------------------------------------------------
## Description of Modal B - deeplearning_vit.ipynb
A Vision Transformer (ViT) model structure made from scratch, tuned to classify 6 types of potato leaf disease 

## Versions:
Python 12.0-13.0 

## Installation:
pip install sns
pip install seaborn
pip install transformers
pip install matplot
pip install scikit-learn
pip install torch
pip install tqdm
pip install torch torchvision torchaudio --index-url://download.pytorch.org/whl/cu118
pip install tabulate

## Instructions:
1. Open python and use Virtual Environment by running python -m venv venv
2. Select your python version using the recommended above
3. Install all needed dependencies and packages above
4. Now you can Click Run All
5. Wait for training which can take up to 2-3 hours
6. It will notify once it is done and the model will be saved as "deeplearning_vit.pt"

Note that to change the filenames of the models and csv in your directory

## Instructions to run demo_deeplearning_vit.ipynb
1. Make sure you installed all packages and dependencies
2. Find the variables:
 "image_dir" - makesure this is the file name of the file folder of the tests
 "model_path" - makesure this is the file name of the model, usually "deeplearning_vit.pt"
3. Once changed to the correct file, click Run All
4. Wait for the print to ensure that predictions is already done and saved in the csv "deeplearning_vit_predictions.csv"


