import pandas as pd

def aggregate_data(file_path, application):
    # Load the xDR dataset
    try:
        xdr_data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    
    # Define the download and upload columns based on the application
    dl_column = f"{application} DL (Bytes)"
    ul_column = f"{application} UL (Bytes)"
    
    # Check if the application columns exist (case-insensitive)
    if dl_column.lower() not in xdr_data.columns.str.lower() or ul_column.lower() not in xdr_data.columns.str.lower():
        print(f"Error: Columns for {application} not found in the dataset.")
        return None
    
    # Check if 'Dur. (ms)' and 'Bearer Id' columns exist
    if 'Dur. (ms)' not in xdr_data.columns or 'Bearer Id' not in xdr_data.columns:
        print("Error: Required columns 'Dur. (ms)' or 'Bearer Id' not found in the dataset.")
        return None
    
    # Add a column for Total_Data_Volume (Download + Upload for the specified application)
    xdr_data[f'Total_{application}_Data_Volume'] = xdr_data[dl_column] + xdr_data[ul_column]
    
    # Aggregate the data based on 'Bearer Id'
    aggregated_data = xdr_data.groupby(['Bearer Id']).agg(
        Number_of_Sessions=('Dur. (ms)', 'count'),
        Total_Session_Duration=('Dur. (ms)', 'sum'),
        Total_Download=(dl_column, 'sum'),
        Total_Upload=(ul_column, 'sum'),
        Total_Data_Volume=('Total_' + application + '_Data_Volume', 'sum')
    ).reset_index()
    
    # Save the aggregated data to a new CSV file
    output_file = f'../assets/data/aggregated_{application}_xdr_data.csv'
    aggregated_data.to_csv(output_file, index=False)
    
    # Display the first few rows of the aggregated data
    print(aggregated_data.head())
    return aggregated_data
