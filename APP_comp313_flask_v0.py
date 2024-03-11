from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import pandas as pd
import numpy as np
import sys
import traceback



# Folder and models
project_folder = r'/Users/josemuniz/Desktop/COMP313_AI_PRY/best_result'

# Load the trained models and the scaler
lr_model = joblib.load(f'{project_folder}/LR_model_drug_use.pkl')
rf_model = joblib.load(f'{project_folder}/RF_model_drug_use.pkl')
scaler   = joblib.load(f'{project_folder}/scaler_drug_use.pkl')

# Define feature names as expected by the model
feature_names = ['Nscore', 'Escore', 'Oscore', 'Ascore', 'Cscore', 'Impulsive', 'SS', 
                 'Alcohol', 'Amphet', 'Amyl', 'Benzos', 'Cannabis', 'Coke', 'Crack', 'Ecstasy',
                 'Heroin', 'Ketamine', 'Legalh', 'LSD', 'Meth', 'Mushrooms', 'Nicotine', 'VSA']

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        print('Received data:', data)
        print(f'ruta: {lr_model}')
        # Extract the features from the data
        features = np.array([[data.get(feature, 0) for feature in feature_names]])
        print (f'features: {features}')
        # Scale the features using the loaded scaler
        features_scaled = scaler.transform(features)
        print (f'features_scaled: {features_scaled}')
        # Generate predictions using the trained models

        print(f'lr_result: {lr_model.predict(features_scaled)[0]}')
        print(f'lr_result: {lr_model.predict(features_scaled)}')

        lr_result = "Likely" if lr_model.predict(features_scaled)[0]> 0.5 else "Unlikely"
        print (f'LR is {lr_result}')
        rf_result = "Likely" if rf_model.predict(features_scaled)[0]> 0.5 else "Unlikely"
        print (f'RF is {rf_result}')
        # Return the prediction results as JSON
        # Prepare the response
        response = {
            'prediction1': lr_result,
            'prediction2': rf_result
        }
        
        return jsonify(response)

    except Exception as e:
        print('Error:', str(e))
        return jsonify({'error': str(e)})


#port number
if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except:
        port = 12412

    app.run(port=port, debug=True)
