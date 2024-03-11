from flask import Flask, render_template, request
from DrugModel import DrugModel

app = Flask(__name__, template_folder='../frontend/templates')

# change the filepath in your end as this is my directory :)
file_path = 'C:\\Sem-06\\COMP313_SEC004-W2024\\comp313-004-Team3-W24\\Backend\\drug_consumption.data'

# Drugmodel Initialization
drug_model = DrugModel(file_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':

        # Retrieving form data from index.html
        age = request.form['age']
        gender = request.form['gender']
        education = request.form['education']
        country = request.form['country']
        ethnicity = request.form['ethnicity']
        #cl = request.form['cl']
       
        # Mapping form inputs to numerical representations
        age_mapping = {'-0.95197': 0, '-0.07854': 1, '0.49788': 2, '1.09449': 3, '1.82213': 4, '2.59171': 5}
        gender_mapping = {'-0.48246': 0, '0.48246': 1}
        education_mapping = {'-2.43591': 0, '-1.73790': 1, '-1.43719': 2, '-1.22751': 3, '-0.61113': 4, '-0.05921': 5, '0.45468': 6, '1.16365': 7, '1.98437': 8}
        country_mapping = {'-0.09765': 0, '0.24923': 1, '-0.46841': 2, '-0.28519': 3, '0.21128': 4, '0.96082': 5, '-0.57009': 6}
        ethnicity_mapping = {'-0.50212': 0, '-1.10702': 1, '1.90725': 2, '0.12600': 3, '-0.22166': 4, '0.11440': 5, '-0.31685': 6}
        #cl_mapping = {'CL0': 0.0, 'CL1': 1.0, 'CL2': 2.0, 'CL3': 3.0, 'CL4': 4.0, 'CL5': 5.0, 'CL6': 6.0 }
        
        age = age_mapping[age]
        gender = gender_mapping[gender]
        education = education_mapping[education]
        country = country_mapping[country]
        ethnicity = ethnicity_mapping[ethnicity]
        #cl = cl_mapping[cl]

        # Predicting drug consumption and passing value to the prediction.html
        prediction = drug_model.predict(age, gender, education, country, ethnicity)
        
        return render_template('prediction.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

