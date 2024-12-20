import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_visualizations(file_path, application_name):
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Plot histograms for each quantitative variable
    df[['Total_Session_Duration', 'Total_Download', 'Total_Upload', 'Total_Data_Volume']].hist(bins=30, figsize=(12, 8))
    plt.tight_layout()
    plt.show()

    # Plot boxplots to detect outliers
    sns.boxplot(data=df[['Total_Session_Duration', 'Total_Download', 'Total_Upload', 'Total_Data_Volume']])
    plt.show()
    
    print(f"Visualizations for {application_name} are completed.")

    return True
