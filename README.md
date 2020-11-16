# Idiopathic Pulmonary Fibrosis Predictor
This project will use image processing and machine learning systems to assist in devloping a prognosis for Idiopathic Pulmonary Fibrosis (IPF). This was inspired by the Kaggle competiton, "OSIC Pulmonary Fibrosis Progression".
### Product Mission
Our goal is to create an architecture that analyzes the CT scans (DICOM images) of the lungs and other metadata which will be used by physician/radiologist to reach a prognosis on the state of the patient's lung tissue.
The User will ideally interface with an app or webpage that will ask to upload an image and fill out medical data. 
### MVP and MVP User Stories 
"As a patient I would like an easy to read and understandable score."
"As a physician I want medically relevent information."
"As a user I want a simple UI."
"As a user I wan a quick "real-time" result."
"As a physician I want an uncertainty of the prediction."
### Technolgies to Evaluate
In the front end, the team has decided to interface with the user with a webpage rather than an app. We are using multiple backend architectures, namely regression models (Logistic and Quantile) and then for the DICOM images we are working on a neural network (convolutional). Subject to change
### Development Environment 
For our project we will be expanding upon the ML algorithims in the Kaggle notebooks. Additonally, we will utilze Github for libraries and other sources. Initial images were provided in the competition and we are in the process of implementing using more publically available data. 
### Definition of Architecture
![IPFDataFlowChart (1)](https://user-images.githubusercontent.com/67568998/96325132-5ad04400-0ff3-11eb-910b-20db1e503233.png)

### Technology Selection and Justification
So far we have tested two backend regression models for the Forced Vital Capacity, a simple Logistic Regression and a more complex Quantile regression model. Both produced acceptable results but for our initial web page we are implementing the Logistic Regression to produce results.
The more important backend is the analysis of the dicom images. We currently also have a working pre-processor for lung fuction using the Hounsfield scale. Models for efficientnets_B6 and ResNet have been trained, and will be retrained using segmented dicom images in order to lower the training error. 
### Functional Demonstration of Major User Story
https://kellenbj.github.io/EC601A1-Kaggle-IPF-group09/
This website is where we will be posting and updating for the forseeable future. 
178.128.191.113 is IP address for live website, currently under development!
