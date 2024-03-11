import DrugUtil, DrugPreprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DrugModel:
    def __init__(self, file_path):
        print(file_path)
        self.data = pd.read_csv(file_path, 
                                header=None, 
                                names=DrugUtil.COLUMNS)
        self.preprocess_obj = DrugPreprocessing.DrugPreprocessing(self.data)

    def data_screen(self):
        self.preprocess_obj.initial_screening()

    def data_conversion(self):
        self.preprocess_obj.init_data_conversion()

    def data_exploration(self):
        self.preprocess_obj.init_data_exploration()

    def preprocessing(self):
        self.data_screen()
        self.data_conversion()
        self.data_exploration()
    
    #just for testing purpose
    def predict(self, age, gender, education, country, ethnicity):
        prediction = age * gender * education * country * ethnicity 
        return prediction