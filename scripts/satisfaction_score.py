import numpy as np
import pandas as pd

def calculate_satisfaction_score(input_file, output_file, top_10_output_file):
    data = pd.read_csv(input_file)
    
    # Ensure the dataset contains the necessary columns
    required_columns = ['Bearer Id', 'engagement_score', 'experience_score']
    if not all(col in data.columns for col in required_columns):
        raise ValueError(f"The dataset must contain the following columns: {required_columns}")

    # Calculate the satisfaction score as the average of engagement_score and experience_score
    data['satisfaction_score'] = (data['engagement_score'] + data['experience_score']) / 2
   # satisfaction_score

    # Save the entire dataset with satisfaction scores to the overall output file
    data.to_csv(output_file, index=False)
    
    # Sort by satisfaction_score in descending order to get the top satisfied customers
    top_10_satisfied_customers = data[['Bearer Id', 'satisfaction_score']].sort_values(by='satisfaction_score', ascending=False).head(10)
    
    # Save the top 10 satisfied customers to the output file
    top_10_satisfied_customers.to_csv(top_10_output_file, index=False)

    
    # Print the top 10 satisfied customers for verification
    print("Top 10 Satisfied Customers:")
    print(top_10_satisfied_customers)
    print(f"Top 10 satisfied customers have been saved to {top_10_output_file}")
    return calculate_satisfaction_score

