// Attaches an event listener to the Upload button
document.getElementById('uploadBtn').addEventListener('click', () => {
    // Gets references to the input field, preview image, and result display area
    const fileInput = document.getElementById('fileInput');
    const previewImage = document.getElementById('previewImage');
    const predictionResult = document.getElementById('predictionResult');

    // Hides the previous prediction results
    predictionResult.style.display = 'none';
    predictionResult.className = 'prediction-result';

    // Checks if a file is selected
    if (fileInput.files.length > 0) {
        const file = fileInput.files[0]; // Accesses the selected file
        const reader = new FileReader(); // FileReader to preview the image

        // When the image is loaded, set it in the preview area
        reader.onload = function (e) {
            previewImage.src = e.target.result; // Sets image source
            previewImage.style.display = "block"; // Makes the preview visible
        };

        reader.readAsDataURL(file); // Reads the file as a data URL for preview

        // Prepares the image for upload
        const formData = new FormData();
        formData.append("file", file); // Attaches the file to the form

        // Displays a loading message while the image is being analyzed
        predictionResult.textContent = '🔄 Analyzing image, please wait...';
        predictionResult.style.display = 'block';
        predictionResult.className = 'prediction-result';

        // Sends the file to the backend API for prediction
        fetch('http://127.0.0.1:8000/predict', { //Feel free to change the port here, and also in api.py

            method: 'POST',
            body: formData // Sends the form with the file
        })
            .then(response => {
                // Checks if the response from the server is okay
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json(); // Converts the response to JSON
            })
            .then(data => {
                // If a prediction is received, this displays it
                if (data.prediction) {
                    predictionResult.textContent = `✅ Prediction: ${data.prediction}`;
                    predictionResult.classList.add('prediction-success');
                } else {
                    // Displays any errors returned by the API
                    predictionResult.textContent = `❌ Error: ${data.error}`;
                    predictionResult.classList.add('prediction-error');
                }
            })
            .catch(error => {
                // Catches and displays any errors during the fetch process
                console.error('Error:', error);
                predictionResult.textContent = '❌ Error making prediction. Please try again.';
                predictionResult.classList.add('prediction-error');
            });
    } else {
        // Informs the user to select an image if no file is chosen
        predictionResult.textContent = "❌ Please select an image to upload.";
        predictionResult.classList.add('prediction-error');
        predictionResult.style.display = 'block';
    }
});
