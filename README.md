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

### Method and Procedures for CT Scan Image Processing 
The two methods of vaible image processing for this project are: "Image-to-Image" processing and "Image-to-Data processing". At it's core, both methods utilze the Hounsfield Unit (HU) measure of radiodensity. "Image-to-Image" Processing was concluded to be the best method for this project because of it's ability to better portray the lung status to the main user (visual dipictions). In addtion, Image-to-Image better complies with the pre-trained ML network as compared to the raw HU matrix that Image-to-Data would output.

#### Hounsfield Unit (HU)
The Hounsfield Unit is a dimensionless unit in CT scans which measures radiodensity. This is a universal and standardized form of measurment in computed tomography (CT). HU calculation is avaialbe in the pydicom package. The HU can be calculated from the pixel data with a DICOM image using the following formula:
![HU](https://user-images.githubusercontent.com/67568998/100667177-26f17980-3328-11eb-86e4-9c175b9cc5ec.JPG)

#### Image-to-Data Method (Peak Detection) 
The original plan for image processing is to convert the CT scan into a unique scale or plot where the convolutional system use a peak detect method. Since the local maxima for the scale is air from the lungs, we can use peak detect and guage the peak intensity with other CT scans to determine lung functionality. Below is a scale of landmarks as a function to the greyscale intensity provided by radiopedia.org, and a graphical representation of that scale. 
![scale](https://user-images.githubusercontent.com/67568998/100674549-4f32a580-3333-11eb-99b1-ce0b8beb44c4.JPG)
