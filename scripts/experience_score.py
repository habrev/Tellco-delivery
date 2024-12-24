

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cdist

def load_user_data(file_path):
    return pd.read_csv(file_path)

def normalize_data(user_data):
    features = user_data[['Total_Session_Duration', 'Total_Download', 'Total_Upload']]
    scaler = StandardScaler()
    return scaler.fit_transform(features)

def calculate_experience_score(user_data, centroid):
    """
    Calculate the Euclidean distance between each user's data and the centroid of the worst experience cluster.
    """
    user_features_normalized = normalize_data(user_data)
    distances = cdist(user_features_normalized, [centroid])
    user_data['experience_score'] = distances
    return user_data

def save_data_with_scores(user_data, output_path):
    
    user_data.to_csv(output_path, index=False)
    print(f"Experience scores saved to {output_path}")
