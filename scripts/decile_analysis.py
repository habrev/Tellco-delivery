import pandas as pd

def analyze_deciles(file_path, application_name):
    df = pd.read_csv(file_path)
    
    # Sort users by total duration and create decile classes
    df['duration_decile'] = pd.qcut(df['Total_Session_Duration'], 10, labels=False)
    
    # Compute total data (DL + UL) per decile class
    data_per_decile = df.groupby('duration_decile')['Total_Data_Volume'].sum()

    # Top five deciles based on total data (DL + UL)
    top_deciles = data_per_decile.loc[5:10]
    
    # Print results
    print(f"\nResults for {application_name}:")
    print(f"Total data per decile class:\n{data_per_decile}\n")
    print(f"Top five decile classes (5 to 10):\n{top_deciles}")
    
    # Return the results for further processing if needed
    return data_per_decile, top_deciles
