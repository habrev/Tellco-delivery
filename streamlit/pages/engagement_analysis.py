import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title of the app
st.title("Top 3 Most Used Applications Based on Total Data Volume")

# Load the aggregated data (total traffic per application)
data_path = '../assets/data/total_traffic_per_user_per_application.csv'  # Update the path as needed
total_traffic_per_application = pd.read_csv(data_path)

# Sort applications by total data volume and select the top 3 most used applications
top_3_applications = total_traffic_per_application.sort_values(by='Total_Data_Volume', ascending=False).head(3)

# Set up the plot using Seaborn and Matplotlib
plt.figure(figsize=(10, 6))
sns.barplot(x='application_name', y='Total_Data_Volume', data=top_3_applications, palette='viridis')

# Add titles and labels
plt.title('Top 3 Most Used Applications Based on Total Data Volume', fontsize=16)
plt.xlabel('Application Name', fontsize=12)
plt.ylabel('Total Data Volume (Bytes)', fontsize=12)

# Display the plot in Streamlit
st.pyplot(plt)

# Optionally display the data in a table
st.write("Data for the top 3 applications:")
st.dataframe(top_3_applications)
