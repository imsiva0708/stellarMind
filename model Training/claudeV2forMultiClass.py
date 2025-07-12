import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta


actions = [
    'Reroute power to core functions',
    'Adjust orientation for passive cooling',
    'Recalibrate position, tweak pitch, roll, yaw',
    'Initiate Docking sequence to ISS',
    'Increase cooling system power',
    'Adjust antenna position or switch frequency',
    'Optimize data transmission',
    'Delete unnecessary data',
    'Adjust pitch, yaw, roll for sunlight absorption',
    'Disable non-essential systems',
    'Redistribute workload, reduce power to affected components'
]

def generate_satellite_dataset(num_samples=10000, time_span_days=365):
    """
    Generate a synthetic dataset for satellite autonomous decision-making with action recommendations.
    """
    # Use the existing dataset generation code
    start_date = datetime(2024, 1, 1)
    timestamps = [start_date + timedelta(days=random.uniform(0, time_span_days)) 
                 for _ in range(num_samples)]
    timestamps.sort()  # Sort chronologically
    
    df = pd.DataFrame({'Timestamp': timestamps})
    
    # Generate time-based attribute (days since start)
    df['Days_Since_Start'] = [(ts - start_date).days for ts in df['Timestamp']]
    

    # Generate independent and dependent attributes with random values
    df['Battery_Level'] = np.random.uniform(0, 100, num_samples)
    df['Battery_Health'] = np.random.uniform(20, 100, num_samples)
    df['Signal_Strength'] = np.random.uniform(0, 100, num_samples)
    df['Power_Consumption_Rate'] = np.random.uniform(0, 100, num_samples)
    df['Component_Health'] = np.random.uniform(40, 100, num_samples)
    df['CPU_GPU_Usage'] = np.random.uniform(0, 100, num_samples)
    df['Solar_Panel_Efficiency'] = np.random.uniform(0, 100, num_samples)
    df['Temperature'] = np.random.uniform(-30, 90, num_samples)
    df['Data_Storage_Used'] = np.random.uniform(0, 100, num_samples)
    df['Debris_Risk_Level'] = np.random.uniform(0, 10, num_samples)
    
    # Define optimal ranges for key attributes
    attribute_ranges = {
        'Battery_Health':{
            'critical_low': 30
        },
        'Component_Health':{
            'critical_low': 50
        },
        'Battery_Level': {
            'critical_low': 20,
            'low': 40,
            'optimal_min': 60,
            'optimal_max': 90
        },
        'Temperature': {
            'critical_low': -20,
            'low': 0,
            'optimal_min': 10,
            'optimal_max': 40,
            'high': 60,
            'critical_high': 80
        },
        'Signal_Strength': {
            'critical_low': 30,
            'low': 50,
            'optimal_min': 70,
            'optimal_max': 100
        },
        'Solar_Panel_Efficiency': {
            'critical_low': 40,
            'low': 60,
            'optimal_min': 80,
            'optimal_max': 100
        },
        'Data_Storage_Used': {
            'critical_high': 85,
            'high': 75,
            'optimal_max': 60
        },
        'Debris_Risk_Level': {
            'critical_high': 8,
            'high': 6,
            'optimal_max': 4
        },
        'CPU_GPU_Usage': {
            'critical_high': 90,
            'high': 80,
            'optimal_max': 70
        }
    }
    for action in actions:
        df[action] = 0
    
    # Function to determine actions based on attribute values
    def determine_actions(row):
        actions = []
        
        # Battery Health and Component Health Actions
        if row['Battery_Health'] < attribute_ranges['Battery_Health']['critical_low'] or row['Component_Health'] < attribute_ranges['Component_Health']['critical_low']:
            actions.append("Initiate Docking sequence to ISS")
    
        # Battery Level Actions
        if row['Battery_Level'] < attribute_ranges['Battery_Level']['critical_low']:
            actions.append('Disable non-essential systems')
            actions.append('Reroute power to core functions')
        elif row['Battery_Level'] < attribute_ranges['Battery_Level']['low']:
            actions.append('Reroute power to core functions')
        
        # Temperature Actions
        if row['Temperature'] > attribute_ranges['Temperature']['critical_high']:
            actions.append('Increase cooling system power')
            actions.append('Adjust orientation for passive cooling')
        elif row['Temperature'] > attribute_ranges['Temperature']['high']:
            actions.append('Increase cooling system power')
        elif row['Temperature'] < attribute_ranges['Temperature']['critical_low']:
            actions.append('Adjust orientation for passive cooling')
        
        # Solar Panel Efficiency Actions
        if row['Solar_Panel_Efficiency'] < attribute_ranges['Solar_Panel_Efficiency']['critical_low']:
            actions.append('Adjust pitch, yaw, roll for sunlight absorption')
        
        # Signal Strength Actions
        if row['Signal_Strength'] < attribute_ranges['Signal_Strength']['critical_low']:
            actions.append('Adjust antenna position or switch frequency')
        
        # Data Storage Actions
        if row['Data_Storage_Used'] > attribute_ranges['Data_Storage_Used']['critical_high']:
            actions.append('Optimize data transmission')
            actions.append('Delete unnecessary data')
        
        # CPU/GPU Usage Actions
        if row['CPU_GPU_Usage'] > attribute_ranges['CPU_GPU_Usage']['critical_high']:
            actions.append('Redistribute workload, reduce power to affected components')
        
        # Debris Risk Actions
        if row['Debris_Risk_Level'] > attribute_ranges['Debris_Risk_Level']['critical_high']:
            actions.append('Recalibrate position, tweak pitch, roll, yaw')
        
        return actions
    
    # Apply action determination
    df['Recommended_Actions'] = df.apply(determine_actions, axis=1)

    for index, row in df.iterrows():
        for action in row['Recommended_Actions']:
            df.at[index, action] = 1  # Mark the action as '1' in the corresponding column
    
    # Explode the actions to create multiple rows for each unique action
    # df_exploded = df.explode('Recommended_Actions')
    
    # Round and clip values as in the original implementation
    cols_to_clip = ['Battery_Level', 'Battery_Health', 'Signal_Strength', 
                    'Power_Consumption_Rate', 'Component_Health', 'CPU_GPU_Usage']
    for col in cols_to_clip:
        df[col] = df[col].clip(0, 100)
    
    # Round numeric columns
    for col in df.columns:
        if col not in ['Timestamp', 'Docking_Event', 'Days_Since_Start', 'Recommended_Actions']:
            df[col] = df[col].round(2)
    
    return df

# Generate the dataset
np.random.seed(42)  # For reproducibility
satellite_data = generate_satellite_dataset(num_samples=10000)

# Save to CSV
satellite_data.to_csv('satellite_dataset_with_actions.csv', index=False)

# Display sample of the dataset
print(satellite_data.head(10))
corr_matrix = satellite_data[['Solar_Panel_Efficiency', 'Temperature', 'Battery_Level', 
                             'Power_Consumption_Rate', 'Signal_Strength', 'Component_Health', 
                             'CPU_GPU_Usage', 'Data_Storage_Used', 'Debris_Risk_Level']].corr()
# Count and display action frequencies
action_counts = satellite_data['Recommended_Actions'].value_counts()
print("\nRecommended Actions Frequency:")
print(action_counts)

# Verify correlations between key attributes
print("\nCorrelation between key attributes:")
corr_matrix = satellite_data[['Solar_Panel_Efficiency', 'Temperature', 'Battery_Level', 
                             'Power_Consumption_Rate', 'Signal_Strength', 'Component_Health']].corr()
satellite_data.to_csv("issDockingadded.csv")
print(corr_matrix)