COLUMNS = [
    'ID', 'Age', 'Gender', 'Education', 'Country', 'Ethnicity',
    'Nscore', 'Escore', 'Oscore', 'Ascore', 'Cscore',
    'Impulsive', 'SS',
    'Alcohol', 'Amphet', 'Amyl', 'Benzos', 'Caff', 'Cannabis', 'Choc',
    'Coke', 'Crack', 'Ecstasy', 'Heroin', 'Ketamine', 'Legalh', 'LSD',
    'Meth', 'Mushrooms', 'Nicotine', 'Semer', 'VSA'
]

ORDINAL_FEATURES = [
    'Alcohol', 'Amyl', 'Amphet', 'Benzos', 'Cannabis', 'Coke',
    'Crack', 'Ecstasy', 'Heroin', 'Ketamine', 'Legalh', 'LSD',
    'Meth', 'Mushrooms', 'Nicotine','VSA'
]

AGE_MAPPING = {-0.95197: 0, # '18-24'
               -0.07854: 1, # '25-34'
                0.49788: 2, # '35-44'
                1.09449: 3, # '45-54'
                1.82213: 4, # '56-64'
                2.59171: 5  # '65+'
}

GENDER_MAPPING = {-0.48246: 0, # 'male'
                   0.48246: 1 # 'female'
}

EDUCATION_MAPPING = {-2.43591: 0, # 'Left school before 16 years'
                     -1.73790: 1, # 'Left school at 16 years'
                     -1.43719: 2, # 'Left school at 17 years'
                     -1.22751: 3, # 'Left school at 18 years'
                     -0.61113: 4, # 'Some college or university, no certificate or degree'
                     -0.05921: 5, # 'Professional certificate/ diploma'
                      0.45468: 6, # 'University degree'
                      1.16365: 7, # 'Masters degree'
                      1.98437: 8  #'Doctorate degree'
}

COUNTRY_MAPPING = {
    -0.09765: 0, # 'Australia',
     0.24923: 1, # 'Canada',
    -0.46841: 2, # 'New Zealand',
    -0.28519: 3, # 'Other',
     0.21128: 4, # 'Republic of Ireland',
     0.96082: 5, # 'UK',
    -0.57009: 6  # 'USA'
}

ETHNICITY_MAPPING = {
    -0.50212: 0, # 'Asian'
    -1.10702: 1, # 'Black'
     1.90725: 2, # 'Mixed-Black/Asian'
     0.12600: 3, # 'Mixed-White/Asian'
    -0.22166: 4, # 'Mixed-White/Black'
     0.11440: 5, # 'Other'
    -0.31685: 6  # 'White'
}

CL_MAPPING = {
      'CL0': 0.0, # 'never used the drug'
      'CL1': 1.0, # 'used it over a decade ago'
      'CL2': 2.0, # 'in the last decade'
      'CL3': 3.0, # 'used in the last year'
      'CL4': 4.0, # 'used in the last month'
      'CL5': 5.0, # 'used in the last week'
      'CL6': 6.0  # 'used in the last day'
}

CORR_DISPLAY_COLUMNS = ['Age', 'Gender', 'Education', 'Country', 'Ethnicity', 'Nscore',
                   'Escore','Oscore', 'Ascore','Cscore','Impulsive','SS', 'Benzos',
                   'Cannabis', 'Legalh', 'Amyl', 'Amphet', 'Ecstasy', 'Mushrooms', 'Coke', 'LSD']