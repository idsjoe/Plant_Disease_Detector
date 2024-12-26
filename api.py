# Imports necessary libraries and modules
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn  # Server module required to run the FastAPI app
from predict_app import predict  # Imports the prediction function
import tempfile  # To handle temporary file storage
import os  # For file and system operations

# Initializes the FastAPI application
app = FastAPI()

# Adds the CORS middleware to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from all origins, replace by backend URL; if hosting online
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Defines the prediction endpoint
@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    try:
        # Saves the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
            contents = await file.read()  # Reads the file contents
            temp_file.write(contents)  # Writes contents to the temp file
            temp_path = temp_file.name  # Gets the path of the saved file
        
        # Passes the image to the prediction function in predict_app.py
        prediction = predict(temp_path)
        os.unlink(temp_path)  # Deletes the temp file after use

        # Returns the prediction result to the frontend
        return {"prediction": prediction}
    except Exception as e:
        # Returns an error message in case of an exception to the frontend
        return {"error": str(e)}

# Runs the server when the script is executed directly
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000) 
    #Feel free to change the port here, and also in scrip.js 
