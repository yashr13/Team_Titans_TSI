import os
import logging
import numpy as np
from tensorflow.keras.models import load_model  # type: ignore
from tensorflow.keras.preprocessing.image import load_img, img_to_array  # type: ignore
from PIL import UnidentifiedImageError

# Set up logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(message)s')

# Global variable for the model
model = None

# Class labels for traffic signs
classes = {
    0: 'Speed limit (20km/h)',
    1: 'Speed limit (30km/h)', 
    2: 'Speed limit (50km/h)', 
    3: 'Speed limit (60km/h)', 
    4: 'Speed limit (70km/h)', 
    5: 'Speed limit (80km/h)', 
    6: 'End of speed limit (80km/h)', 
    7: 'Speed limit (100km/h)', 
    8: 'Speed limit (120km/h)', 
    9: 'No passing', 
    10: 'No passing veh over 3.5 tons', 
    11: 'Right-of-way at intersection', 
    12: 'Priority road', 
    13: 'Yield', 
    14: 'Stop', 
    15: 'No vehicles', 
    16: 'Veh > 3.5 tons prohibited', 
    17: 'No entry', 
    18: 'General caution', 
    19: 'Dangerous curve left', 
    20: 'Dangerous curve right', 
    21: 'Double curve', 
    22: 'Bumpy road', 
    23: 'Slippery road', 
    24: 'Road narrows on the right', 
    25: 'Road work', 
    26: 'Traffic signals', 
    27: 'Pedestrians', 
    28: 'Children crossing', 
    29: 'Bicycles crossing', 
    30: 'Beware of ice/snow',
    31: 'Wild animals crossing', 
    32: 'End speed + passing limits', 
    33: 'Turn right ahead', 
    34: 'Turn left ahead', 
    35: 'Ahead only', 
    36: 'Go straight or right', 
    37: 'Go straight or left', 
    38: 'Keep right', 
    39: 'Keep left', 
    40: 'Roundabout mandatory', 
    41: 'End of no passing', 
    42: 'End no passing veh > 3.5 tons'
}

# Function to load the model (loads it once and caches globally)
def load_traffic_model():
    global model
    if model is None:
        # Replace the path below with the actual path to your model
        model = load_model(r'C:\Users\Asus\Desktop\Coding\Python\model.h5')
    return model

# Prediction function
def predict_traffic_sign(image_path):
    """
    Predicts the traffic sign in the given image.
    
    Args:
        image_path (str): Path to the uploaded image.

    Returns:
        tuple: (predicted_class_label, confidence_score)
    """
    try:
        # Load and preprocess the image
        image = load_img(image_path, target_size=(30, 30))  # Resize to 30x30 pixels
        image = img_to_array(image) / 255.0  # Normalize pixel values to [0, 1]
        image = np.expand_dims(image, axis=0)  # Add a batch dimension

        # Load the model if not already loaded
        model = load_traffic_model()

        # Predict the traffic sign
        prediction = model.predict(image)
        class_id = np.argmax(prediction)
        confidence = prediction[0][class_id]

        # Return the predicted label and confidence as a percentage
        return classes[class_id], round(confidence * 100, 2)

    except UnidentifiedImageError:
        logging.error("Uploaded file is not a valid image.")
        return "Invalid Image Format", 0.0

    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return "Error", 0.0
