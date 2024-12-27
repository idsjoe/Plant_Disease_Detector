# Plant_Disease_Detector
# Plant Disease Detector

This repository hosts a webpage-based application that allows users to upload images of crop leaves and identify up to 38 different plant diseases. The project utilizes the PlantVillage dataset, MobileNetV2 for feature extraction, and Support Vector Machine (SVM) for classification.

## Features
- Detects up to **38 plant diseases** with high accuracy.
- Utilizes **MobileNetV2** for feature extraction.
- Includes a user-friendly **web interface** for uploading images and viewing results.
- Backend implemented using **FastAPI**.
- Designed to run locally or on a cloud server.

## Requirements

### Recommended Python Version
- **Python 3.10.1** or higher, but not exceeding **3.10.9**.

### Python Libraries
Install the required Python libraries using the following command:
```bash
pip install -r requirements.txt
```

## Installation and Setup

### Clone the Repository
```bash
git clone https://github.com/<your-username>/Plant_Disease_Detector.git
cd Plant_Disease_Detector
```

### Install Dependencies
Ensure that you are using a Python virtual environment.
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### Start the Backend Server
Navigate to the project directory and run:
```bash
python api.py
```
This will start the FastAPI server locally at `http://127.0.0.1:8000`.

### Run the Web Interface
Open `index.html` in any modern web browser. You can also deploy the frontend on platforms like **Netlify** or **Vercel** for remote access.

## Usage
1. Open the web interface.
2. Upload an image of a crop leaf.
3. Click the **Upload Image** button.
4. View the predicted disease and confidence score.

## Project Structure
```
Plant_Disease_Detector/
├── api.py             # Backend API using FastAPI
├── predict_app.py     # Feature extraction and prediction logic
├── script.js          # Frontend interaction logic
├── styles.css         # Frontend styling
├── index.html         # Web interface
├── svm_model.pkl      # Trained SVM model
├── requirements.txt   # Required Python libraries
└── README.md          # Documentation
```

## Dataset
- **PlantVillage Dataset**: A collection of over 54,000 images across 14 crop species and 38 diseases.
- Source: [PlantVillage Website](https://plantvillage.psu.edu/) and [Kaggle](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset).

## Model Details
- **Feature Extractor**: MobileNetV2 pre-trained on ImageNet.
- **Classifier**: Support Vector Machine (SVM) with a linear kernel.
- **Comparison Models**: Random Forest and XGBoost (performance details in the [Performance Analysis Report](link-to-report)).

## Future Enhancements
- Add more plant species and disease types.
- Optimize for mobile devices with TensorFlow Lite.
- Experiment with hybrid models for improved rare class detection.

## Contributing
We welcome contributions to enhance this project. Please fork the repository and submit a pull request with detailed descriptions of your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Authors
- **Idhant Joshi**  
- **Mayank Kundalwal**  
- **Dr. Deepak Mishra**

## References
1. [PlantVillage Dataset on Kaggle](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)
2. [PlantVillage Website](https://plantvillage.psu.edu/)

## GitHub Repository
The full source code, documentation, and setup instructions can be found here: [Plant Disease Detector Repository](https://github.com/<your-username>/Plant_Disease_Detector).
