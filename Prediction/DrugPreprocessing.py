import DrugUtil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DrugPreprocessing:
    def __init__(self, data):
        self.data = data
    
    def initial_screening(self):
        print(self.data.head())
        print('rows', self.data.shape[0])
        print('colums', self.data.shape[0])
        print(self.data.query("Semer != 'CL0'"))
        print(self.data.head(1))
        print(self.data.describe())

    def init_data_conversion(self):
        self.data['Age'] = self.data['Age'].map(DrugUtil.AGE_MAPPING)
        self.data['Gender'] = self.data['Gender'].map(DrugUtil.GENDER_MAPPING)
        self.data['Education'] = self.data['Education'].map(DrugUtil.EDUCATION_MAPPING)
        self.data['Country'] = self.data['Country'].map(DrugUtil.COUNTRY_MAPPING)
        self.data['Ethnicity'] = self.data['Ethnicity'].map(DrugUtil.ETHNICITY_MAPPING)
        for feature in DrugUtil.ORDINAL_FEATURES:
            self.data[feature] = self.data[feature].map(DrugUtil.CL_MAPPING)

    def init_data_exploration(self):
        average_drug_use = self.data[DrugUtil.ORDINAL_FEATURES] \
                               .mean()
        sort_average_drug_use = average_drug_use.sort_values(ascending=False)
        plt.figure(figsize=(14, 6))
        sns.barplot(x=average_drug_use.index, y=sort_average_drug_use.values)

        # Add labels and title for clarity
        plt.xticks(rotation=45)
        plt.ylabel('Average Consumption Score')
        plt.xlabel('Drug Type')
        plt.title('Average Drug Use')

        # Show the plot
        plt.show()

        drugs_df = self.data[DrugUtil.CORR_DISPLAY_COLUMNS]
        print(drugs_df.head())
        plt.figure(figsize=(18, 10))
        sns.heatmap(drugs_df.corr(), annot=True, fmt=".2f", cmap='viridis')

        # Setting the title
        plt.title('Correlation Matrix for Selected Drug and Personality Features')

        # Display the heatmap
        plt.show()