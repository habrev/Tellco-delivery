import pandas as pd

def preprocess_data(file_path, application_name):
    # Load the xDR dataset
    df = pd.read_csv(file_path)
    
    # Check for missing values
    missing_values = df.isnull().sum()
    print(f"Missing values:\n{missing_values}\n")
    
    # Replace missing values with the mean for each column
    df.fillna(df.mean(), inplace=True)

    # Calculate IQR for numerical columns specific to the application
    # Add the application's download and upload columns dynamically
    dl_column = "Total_Download"
    ul_column = "Total_Upload"
    
    # Check if the application columns exist
    if dl_column not in df.columns or ul_column not in df.columns:
        print(f"Error: Columns for {application_name} not found in the dataset.")
        return None
    
    # Calculate IQR for numerical columns
    Q1 = df[['Total_Session_Duration', 'Total_Download', 'Total_Upload', 'Total_Data_Volume']].quantile(0.25)
    Q3 = df[['Total_Session_Duration', 'Total_Download', 'Total_Upload', 'Total_Data_Volume']].quantile(0.75)
    IQR = Q3 - Q1

    # Define lower and upper bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Identify outliers
    outliers_iqr = (df[['Total_Session_Duration', 'Total_Download', 'Total_Upload', 'Total_Data_Volume']] < lower_bound) | \
                   (df[['Total_Session_Duration', 'Total_Download', 'Total_Upload', 'Total_Data_Volume']] > upper_bound)

    # Display rows with outliers
    outliers_iqr_data = df[outliers_iqr.any(axis=1)]
    print(f"Outliers detected (IQR method):\n{outliers_iqr_data}")

    # Replace outliers with upper and lower bounds based on IQR
    df[['Total_Session_Duration', 'Total_Download', 'Total_Upload', 'Total_Data_Volume']] = df[['Total_Session_Duration', 'Total_Download', 'Total_Upload', 'Total_Data_Volume']].apply(
        lambda x: x.clip(lower=lower_bound[x.name], upper=upper_bound[x.name]))

    # Replace outliers with the median value of each column
    df[['Total_Session_Duration', 'Total_Download', 'Total_Upload', 'Total_Data_Volume']] = df[['Total_Session_Duration', 'Total_Download', 'Total_Upload', 'Total_Data_Volume']].apply(
        lambda x: x.apply(lambda val: x.median() if val < lower_bound[x.name] or val > upper_bound[x.name] else val))

    # Save the preprocessed data to a new CSV file for further analysis
    output_file = f'../assets/data/preprocessed_{application_name}_xdr_data.csv'
    df.to_csv(output_file, index=False)

    # Check for missing values again after treatment
    missing_values_after = df.isnull().sum()
    print(f"Missing values after treatment:\n{missing_values_after}\n")

    return df

