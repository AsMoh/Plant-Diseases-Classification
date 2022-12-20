# Plant Diseases Classification with Deep learning

### About the dataset:

This dataset is an augmented & modified version of the original dataset, which can be found on a this GitHub repository https://github.com/spMohanty/PlantVillage-Dataset. The sourcse of the dataset is kaggele. The dataset includes approximately 87,000 RGB images of healthy and diseased crop leaves, which are classified into 38 categories. The dataset is split into a training set (80%) and a validation set (20%), and the directory structure is maintained. Additionally, a new directory containing 33 test images has been created for prediction purposes. 

The 38 classes are : 
'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'

### 🎯 Goal :

Our goal is to build plant diseases classifier that predicts wheter a plant is healthy or not, and if it is not healthy, the model will precict the type of the disease. We will user transfer learning where we 
