# ☘️ Plant Diseases Classification with Deep learning ☘️

### 📝 About the dataset:

This dataset is an augmented & modified version of the original dataset, which can be found on this GitHub repository https://github.com/spMohanty/PlantVillage-Dataset. The source of the dataset is kaggele. The dataset includes approximately 87,000 RGB images of healthy and diseased crop leaves, which are classified into 38 categories. The dataset is split into a training set (80%) and a validation set (20%), and the directory structure is maintained. Additionally, a new directory containing 33 test images has been created for prediction purposes. 

The 38 classes are : 
'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'


The first part of the class name is the plant/crop name, and the rest of the name indicates the disease name if it is not healthy. For example, Apple___Black_rot -->> Apple is the name of the plant, and the name of the disease is  Black_rot. Apple___healthy refers to a healthy apple plant.

Below are samples of the dataset images:

![0e527d62-de6c-4ab5-bb49-f7a6686d207b___RS_HL 4808_180deg](https://user-images.githubusercontent.com/10277729/209166019-9d78108c-5935-4c9a-a2a5-8d89a994222e.JPG)
![1a1acd8f-bd8d-47be-945d-ce308dffd678___Crnl_L Mold 6675](https://user-images.githubusercontent.com/10277729/209166198-59b05f96-2cd5-4a6d-b662-32689c5094f0.JPG)
![0a0b8f78-df2d-4cfc-becf-cde10fa2766b___RS_HL 5487_new30degFlipLR](https://user-images.githubusercontent.com/10277729/209166281-0d8fd35d-5be4-4a0a-98d4-d70f77bd8bd2.JPG)![0a6983a5-895e-4e68-9edb-88adf79211e9___RS_Early B 9072](https://user-images.githubusercontent.com/10277729/209166462-8244246e-6388-415a-afee-724263abcd7b.JPG)
![2bbd67e6-0eb0-4569-92fd-bc5fbf4c6570___R S_HL 8344 copy 2](https://user-images.githubusercontent.com/10277729/209166582-7e41446c-9df7-4182-ae33-3566632a43a2.jpg)
![3ddb5798-8a7d-47e7-87cc-4189675cae80___R S_HL 5496 copy 2](https://user-images.githubusercontent.com/10277729/209166639-b71d68fa-953d-4fa5-8254-19e68bd548df.jpg)

![0e30d373-58ad-4464-ab61-89cc9d4ab912___RS_HL 2543_newPixel25](https://user-images.githubusercontent.com/10277729/209166849-73bb5d76-0ec7-4f7a-9e92-19dffe10db04.JPG)
![0a2ed402-5d23-4e8d-bc98-b264aea9c3fb___Rutg _HL 2471](https://user-images.githubusercontent.com/10277729/209166915-0dbf2510-257c-4a7c-bbad-7690209b6622.JPG) ![0ac4ff49-7fbf-4644-98a4-4dc596e2fa87___Mt N V_HL 9004_90deg](https://user-images.githubusercontent.com/10277729/209167743-be98dc16-7ce0-4634-a6bf-7cb6a67a9df5.JPG)

How to download the dataset is clarified in the notebook.ipynb. Below is kaggle link to download the dataset:
https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset


### 🎯 Goal :

Our goal is to build plants diseases classifier that predicts whether a plant is healthy or not, and if it is not healthy, the model will predict the type of the disease. We will use transfer learning in this project, and particularly the 2 pretrained models used are Xception & ResNet50V2, and we will retrain them on our dataset.

To be able to view the notebook online, click on the below link:
https://app.reviewnb.com/AsMoh/Plant-Diseases-Classification/blob/main/notebook.ipynb 

### Running & deploying the model in the local machine:

You can download the final model xception_v1_47_0.9591.h5 from the below link:
https://drive.google.com/file/d/1QtH81thNfShsm8DDs3_ZDkTduc95Ej8R/view?usp=sharing

"Converting Keras model to TF-Lite.ipynb" file contains the code for converting the model to TF-Lite to deploy it in the cloud easily. 

I have created a docker image for the model by running the below commands, and the docker file & the lamda_function.py files have been uploaded in this repository:
<br>
<code>docker build -t plant-disease-model:v1 . </code>  <br>

To run the docker image, I run the below command. <br>
<code> docker run -it --rm -p 8080:8080 plant-disease-model:v1   </code> <br>  


The docker image can be downloaded from docker hub by running the below command: <br>
 <code> docker pull asia2022/plant-diseases-classifier:v1 </code>
 
 To run the docker image downloaded from the docker hub, run the below command: <br>
 <code> docker run -it --rm -p 8080:8080 asia2022/plant-diseases-classifier:v1  </code>
 
 Then, you can modify & run the test.py file to classify the images of the plants.
 
 ### Demo for deploying the model locally with lambda:
 





https://user-images.githubusercontent.com/10277729/209446806-ed2f70b3-4a2a-4b64-88fa-6fe011fffc85.mp4

<br>
The above video shows a demo for deploying the model locally, passing an image of Apple with Apple scab disease to the model and classifying the image by the model as unhealthy with scab disease.

<br>

### Running & deploying the model in the cloud:

I have deployed the model in a serverless environment on AWS using Lambda, and API Gateway. The invoke URL for the service is https://x0ywfq3odb.execute-api.us-east-1.amazonaws.com/FirstTest1/predict . 

test-cloud.py file includes the code for testing the deployed model.

### Demo for deploying the model  in the cloud with serverless:


https://user-images.githubusercontent.com/10277729/210170563-5312c1c0-5704-433d-baf6-094b59f4cc02.mp4


<br>
The above video shows a demo for sending requests to the deployed model & getting the response back with the model prediction.


