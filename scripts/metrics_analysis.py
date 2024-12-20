import pandas as pd

def analyze_basic_metrics(file_path, application_name):
    # Load the dataset
    df = pd.read_csv(file_path)    
    # Calculate basic metrics
    mean_data = df.mean()  # Mean of each column
    median_data = df.median()  # Median of each column
    std_data = df.std()  # Standard deviation of each column
    
    # Print basic metrics
    print(f"Basic Metrics for {application_name}:")
    print(f"\nMean:\n{mean_data}\n")
    print(f"Median:\n{median_data}\n")
    print(f"Standard Deviation:\n{std_data}\n")
    
    return mean_data, median_data, std_data
