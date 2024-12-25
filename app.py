from flask import Flask, request, jsonify
import joblib
import numpy as np
import logging

# Set up logging
logging.basicConfig(filename='model_predictions.log', level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Load the model
model = joblib.load('model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the features from the incoming request
        data = request.get_json(force=True)
        features = np.array(data['features']).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features)
        
        # Log prediction
        logging.info(f"Features: {data['features']}, Prediction: {prediction.tolist()}")
        
        # Return the prediction as a JSON response
        return jsonify(prediction=prediction.tolist())
    
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return jsonify({"error": "An error occurred"}), 500

if __name__ == '__main__':
    # Run the app on all interfaces for Docker
    app.run(host='0.0.0.0', port=5000)
