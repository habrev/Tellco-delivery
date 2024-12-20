import pandas as pd

def describe_data(file_path, application_name):
    # Load your dataset
    df = pd.read_csv(file_path)
    
    # Describe relevant variables and associated data types
    print(f"\nDescribing data for {application_name}...\n")
    print(f"Data types of each column:\n{df.dtypes}\n")  # Data types of each column
    print(f"Summary statistics of numeric variables:\n{df.describe()}\n")  # Summary statistics of numeric variables

    return df

# Example usage for each application
applications = ['Google', 'Netflix', 'YouTube', 'Facebook', 'Twitter']
file_path = '../assets/data/preprocessed_xdr_data.csv'

for application_name in applications:
    describe_data(file_path, application_name)
