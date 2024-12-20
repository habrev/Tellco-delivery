import pandas as pd

def compute_dispersion(file_path, application_name):
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Compute dispersion parameters for each quantitative variable
    dispersion_params = df[['Total_Session_Duration', 'Total_Download', 'Total_Upload', 'Total_Data_Volume']].agg(['mean', 'median', 'std', 'min', 'max'])
    
    # Print dispersion parameters
    print(f"Dispersion Parameters for {application_name}:")
    print(dispersion_params)
    
    return dispersion_params
