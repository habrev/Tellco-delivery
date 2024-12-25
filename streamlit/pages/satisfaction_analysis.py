import pandas as pd
import streamlit as st
import numpy as np
from scipy.spatial.distance import cdist

# for engagement_score.py

# Load pre-uploaded results
precomputed_file_path = '../assets/data/engagement_scores.csv'
try:
    df = pd.read_csv(precomputed_file_path)
    st.write("### Results Preview", df.head())

    # Option to visualize engagement scores
    st.write("## Engagement Scores Summary")
    st.write("### Descriptive Statistics")
    st.write(df['engagement_score'].describe())

    # Plot engagement scores
    st.write("### Distribution of Engagement Scores")
    st.bar_chart(df['engagement_score'])

    # Download option for the results
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Results CSV",
        data=csv,
        file_name="engagement_scores_results.csv",
        mime="text/csv"
    )
except FileNotFoundError:
    st.error("Precomputed results file not found at the specified path.")


# for experience_score.py

import pandas as pd
import streamlit as st
import numpy as np
from scipy.spatial.distance import cdist

# Function to calculate experience scores
def calculate_experience_score(data, centroid):
    features = data.select_dtypes(include=np.number).values  # Extract numerical features
    distances = cdist(features, [centroid], metric='euclidean')
    data['experience_score'] = distances.flatten()
    return data

# Load pre-uploaded user data

output_file_path = '../../assets/data/user_data_with_experience_scores.csv'

try:
    user_data = pd.read_csv(precomputed_file_path)
    st.title("User Experience Score Analysis")

    # Predefined worst experience cluster centroid
    centroid_cluster_1 = np.array([2.064230e+07, 65.010918, 1372.051897])

    st.write("### User Data Preview", user_data.head())

    # Calculate experience scores
    user_data_with_scores = calculate_experience_score(user_data, centroid_cluster_1)
    st.write("### User Data with Experience Scores", user_data_with_scores.head())

    # Save the updated data
    user_data_with_scores.to_csv(output_file_path, index=False)

    # Provide download option
    csv = user_data_with_scores.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download User Data with Experience Scores",
        data=csv,
        file_name="user_data_with_experience_scores.csv",
        mime="text/csv"
    )

    # Summary of experience scores
    st.write("### Experience Scores Summary")
    st.write(user_data_with_scores['experience_score'].describe())

    # Plot distribution of experience scores
    st.write("### Distribution of Experience Scores")
    st.bar_chart(user_data_with_scores['experience_score'])

except FileNotFoundError:
    st.error("Precomputed user data file not found at the specified path.")
