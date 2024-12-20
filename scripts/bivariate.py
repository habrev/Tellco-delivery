import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

def bivariate_analysis(file_path, application_name):
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Add a new column for the application name (so that it's represented in the plot)
    df['Application'] = application_name
    
    # Bivariate analysis: Boxplot (Total_Data_Volume vs Application)
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Application', y='Total_Data_Volume', data=df)
    plt.title(f'Bivariate Analysis: {application_name} vs Total DL+UL Data')
    plt.xlabel('Application')
    plt.ylabel('Total DL+UL Data (Bytes)')
    plt.show()
    
    # Perform ANOVA to test if there is a significant difference in total data volume between applications
    if df['Application'].nunique() > 1:
        anova_result = f_oneway(*[df[df['Application'] == app]['Total_Data_Volume'] for app in df['Application'].unique()])
        print(f"ANOVA result for {application_name}: F-statistic = {anova_result.statistic}, p-value = {anova_result.pvalue}")
    else:
        print(f"Not enough categories in {application_name} to perform ANOVA.")

    return True
