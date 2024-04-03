from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
from keras.models import load_model
import pandas as pd
import numpy as np
import sys
import traceback



# Folder and models
project_folder = r'/Users/josemuniz/Desktop/COMP313_AI/best_result'

# Load the trained models and the scaler
lr_model = joblib.load(f'{project_folder}/LR_model_drug_use.pkl')
lr_model_h = joblib.load(f'{project_folder}/LR_model_heroin.pkl')
rf_model = joblib.load(f'{project_folder}/RF_model_drug_use.pkl')
dl_model = load_model(f'{project_folder}/ANN_model_drug_use.h5')
scaler   = joblib.load(f'{project_folder}/scaler_drug_use.pkl')

# Define feature names as expected by the model
feature_names = ['Nscore', 'Escore', 'Oscore', 'Ascore', 'Cscore', 'Impulsive', 'SS', 
                 'Alcohol', 'Amphet', 'Amyl', 'Benzos', 'Cannabis', 'Coke', 'Crack', 'Ecstasy',
                 'Heroin', 'Ketamine', 'Legalh', 'LSD', 'Meth', 'Mushrooms', 'Nicotine', 'VSA']

# Define feature names as expected by the model
feature_names_h = ['Nscore', 'Escore', 'Oscore', 'Ascore', 'Cscore', 'Impulsive', 'SS', 
                 'Alcohol', 'Amphet', 'Amyl', 'Benzos', 'Cannabis', 'Coke', 'Crack', 'Ecstasy',
                 'Ketamine', 'Legalh', 'LSD', 'Meth', 'Mushrooms', 'Nicotine', 'VSA']

models=['Heroin']

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
        #print(f'ruta: {lr_model}')
        
        # Extract the features from the data
        features = np.array([[data.get(feature, 0) for feature in feature_names]])
        print (f'features: {features}')
        # Scale the features using the loaded scaler
        features_scaled = scaler.transform(features)
        print (f'features_scaled: {features_scaled}')
        # Generate predictions using the trained models

        # Extract the features from the data
        features_h = np.array([[data.get(feature, 0) for feature in feature_names_h]])
        print (f'features_h: {features_h}')
        # Scale the features using the loaded scaler
        features_h_scaled = np.array(features_h).reshape(1, -1)
        print (f'features_h_scaled: {features_h_scaled}')
        # Generate predictions using the trained models
        lr_result_h = "Likely" if lr_model_h.predict(features_h_scaled)[0]> 0.5 else "Unlikely"
        print (f'LR_h is {lr_result_h}')
        
        
        lr_result = "Likely" if lr_model.predict(features_scaled)[0]> 0.5 else "Unlikely"
        print (f'LR is {lr_result}')
        rf_result = "Likely" if rf_model.predict(features_scaled)[0]> 0.5 else "Unlikely"
        print (f'RF is {rf_result}')
        dl_result = "Likely" if dl_model.predict(features_scaled)[0]> 0.5 else "Unlikely"
        print (f'DNN is {dl_result}')
                
                     
        response = {
                'prediction1': lr_result,
                'prediction2': rf_result,
                'prediction3': dl_result,
                'prediction4': lr_result_h,
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
        port = 1200

    app.run(port=port, debug=True)
