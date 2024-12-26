# Imports necessary libraries
import numpy as np
import joblib  # For loading the SVM model
from PIL import Image  # For image handling
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Defines the class names for the plant diseases
class_names = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Blueberry___healthy', 'Cherry___healthy', 'Cherry___Powdery_mildew', 
    'Corn___Cercospora_leaf_spot Gray_leaf_spot', 'Corn___Common_rust', 'Corn___healthy', 
    'Corn___Northern_Leaf_Blight', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 
    'Grape___healthy', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
    'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 
    'Potato___healthy', 'Potato___Late_blight', 'Raspberry___healthy', 'Soybean___healthy', 
    'Squash___Powdery_mildew', 'Strawberry___healthy', 'Strawberry___Leaf_scorch', 
    'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___healthy', 
    'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 
    'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 
    'Tomato___Tomato_mosaic_virus', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus'
]


# Loads the trained SVM model
svm_model = joblib.load("svm_model.pkl")

# Loads the MobileNetV2 model as a feature extractor
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
feature_extractor = base_model.output
feature_extractor_model = tf.keras.Model(inputs=base_model.input, outputs=tf.keras.layers.GlobalAveragePooling2D()(feature_extractor))

# Functions to preprocess the input image
def preprocess_image(image_path, target_size=(224, 224)):
    img = Image.open(image_path).convert("RGB")  # Opens and converts the image to RGB
    img = img.resize(target_size)  # Resizes the image to 224x224
    img_array = np.array(img, dtype=np.float32)  # Converts the image to a numpy array
    img_array = preprocess_input(img_array)  # Normalizes the image for MobileNetV2
    return np.expand_dims(img_array, axis=0)  # Adds a batch dimension

# Functions to extract features using MobileNetV2
def extract_features(image):
    return feature_extractor_model.predict(image)

# This is the prediction function
def predict(image_path):
    preprocessed_image = preprocess_image(image_path)  # Preprocesss the image
    features = extract_features(preprocessed_image)  # Extracts features
    prediction = svm_model.predict(features)  # Predicts the class using the SVM model
    predicted_class = class_names[prediction[0]]  # Maps the predicted label to the class name
    return predicted_class
