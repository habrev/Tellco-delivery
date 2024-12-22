import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def calculate_engagement_score(input_file, output_file):
    # Load the dataset from the provided input file path
    aggregated_data = pd.read_csv(input_file)

    # Ensure the dataset contains the necessary columns
    required_columns = ['Bearer Id', 'Number_of_Sessions', 'Total_Session_Duration', 'Total_Data_Volume']
    if not all(col in aggregated_data.columns for col in required_columns):
        raise ValueError(f"The dataset must contain the following columns: {required_columns}")
    
    # First, normalize the aggregated metrics (sessions_frequency, total_session_duration, total_traffic)
    scaler = StandardScaler()
    
    # Normalize the metrics
    aggregated_data[['normalized_sessions_frequency', 'normalized_total_session_duration', 'normalized_total_traffic']] = scaler.fit_transform(
        aggregated_data[['Number_of_Sessions', 'Total_Session_Duration', 'Total_Data_Volume']]
    )
    
    # Cluster 2 centroid (less engaged cluster) (replace with the correct centroid values if needed)
    less_engaged_centroid = np.array([0.05796327, 0.00540888, 0.05256049])
    
    # Calculate the Euclidean distance for each user based on the normalized values
    aggregated_data['engagement_score'] = np.sqrt(
        (aggregated_data['normalized_sessions_frequency'] - less_engaged_centroid[0]) ** 2 +
        (aggregated_data['normalized_total_session_duration'] - less_engaged_centroid[1]) ** 2 +
        (aggregated_data['normalized_total_traffic'] - less_engaged_centroid[2]) ** 2
    )
    
    # Save the results (MSISDN and engagement score) to the specified output file
    aggregated_data[['Bearer Id', 'engagement_score']].to_csv(output_file, index=False)
    
    # Print the first few rows of the output for verification
    print(aggregated_data[['Bearer Id', 'engagement_score']].head())
    print(f"Engagement scores have been saved to {output_file}")

    return calculate_engagement_score


