# Potato Disease Classifier 

This README contains instructions for both of our developed models.

Note: Training the models will use the GPU and will use it at maximum power, suggesting for good ventilation and airconditioned room.

Note: Running these on VSCode would be better instead of in Google Colab (unless you have a Pro subscription)
-------------------------------------------------
## Description of Model A - group9_model1.ipynb
A CNN model with ResNet50 as its base model (pretrained = False), tuned to classify 6 types of potato leaf disease 

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
1. Open Python and use Virtual Environment by running python -m venv venv
2. Select your python version using the recommended above
3. Install all needed dependencies and packages above
4. Now you can click :Run All"
5. Wait for training which can take up to 40-50 minutes
6. It will notify once it is done and the model will be saved as "deeplearning_cnn.pt"

## Instructions to run group9_demo2.ipynb
1. Make sure you installed all packages and dependencies
2. Find the variables:
 "image_dir" - makesure this is the file name of the file folder of the tests
 "model_path" - makesure this is the file name of the model, (usually "deeplearning_cnn.pt")
3. Once changed to the correct file, click "Run All"
4. Wait for the print to ensure that predictions is already done and saved in the csv "group9_model1_predictions.csv"
-------------------------------------------------
## Description of Model B - group9_model2.ipynb
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
1. Open Python and use Virtual Environment by running python -m venv venv
2. Select your python version using the recommended above
3. Install all needed dependencies and packages above
4. Now you can click "Run All"
5. Wait for training which can take up to 2-3 hours
6. It will notify once it is done and the model will be saved as "deeplearning_vit.pt"

Aside: In case you change your filenames, find comments within the notebook to adhere to the changes.

## Instructions to run group9_demo2.ipynb
1. Make sure you installed all packages and dependencies
2. Find the variables:
 "image_dir" - makesure this is the file name of the file folder of the tests
 "model_path" - makesure this is the file name of the model, usually "deeplearning_vit.pt"
3. Once changed to the correct file, click "Run All"
4. Wait for the print to ensure that predictions is already done and saved in the csv "group9_model2_predictions.csv"


