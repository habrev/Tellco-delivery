import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def correlation_analysis(file_path, column_name):

    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Check if the required column exists in the dataset
    if column_name not in df.columns:
        print(f"Error: Column '{column_name}' is missing from the dataset.")
        return None
    
    # Compute the correlation matrix for the specified column (if applicable to others)
    correlation_matrix = df[[column_name]].corr()
    
    # Display the correlation matrix
    print(f"Correlation Matrix for {column_name}:\n{correlation_matrix}\n")
    
    # Plot a heatmap for visual interpretation
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title(f'Correlation Matrix for {column_name}')
    plt.show()

    return correlation_matrix
