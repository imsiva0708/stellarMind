import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta

def generate_satellite_dataset(num_samples=1000, time_span_days=365):
    """
    Generate a synthetic dataset for satellite autonomous decision-making.
    
    Parameters:
    -----------
    num_samples : int
        Number of data points to generate
    time_span_days : int
        Number of days the dataset should span
    
    Returns:
    --------
    pandas.DataFrame
        DataFrame containing the satellite attributes
    """
    # Initialize DataFrame with timestamps
    start_date = datetime(2024, 1, 1)
    timestamps = [start_date + timedelta(days=random.uniform(0, time_span_days)) 
                 for _ in range(num_samples)]
    timestamps.sort()  # Sort chronologically
    
    df = pd.DataFrame({'Timestamp': timestamps})
    
    # Generate time-based attribute (days since start)
    df['Days_Since_Start'] = [(ts - start_date).days for ts in df['Timestamp']]
    
    # ------------------------
    # Independent Attributes
    # ------------------------
    
    # Solar Panel Efficiency (30-100%)
    df['Solar_Panel_Efficiency'] = np.random.uniform(30, 100, num_samples)
    
    # Data Storage Used (0-95%)
    df['Data_Storage_Used'] = np.random.uniform(0, 95, num_samples)
    
    # Debris Risk Level (1-10)
    df['Debris_Risk_Level'] = np.random.uniform(1, 10, num_samples)
    
    # Docking to ISS (binary event, approximately once every 60 days)
    df['Docking_Event'] = np.zeros(num_samples)
    dock_days = np.random.choice(time_span_days, size=time_span_days//60, replace=False)
    for i, row in df.iterrows():
        if int(row['Days_Since_Start']) in dock_days:
            df.at[i, 'Docking_Event'] = 1
    
    # ------------------------
    # Power Consumption (semi-independent, slightly influenced by other factors)
    # ------------------------
    # Base power consumption (20-80%)
    base_power = np.random.uniform(20, 80, num_samples)
    
    # ------------------------
    # Temperature (semi-independent, slightly influenced by power consumption)
    # ------------------------
    # Base temperature (-30 to 50°C)
    base_temp = np.random.uniform(-30, 50, num_samples)
    
    # Influence of power consumption on temperature
    # Higher power consumption slightly increases temperature
    power_influence = base_power * 0.2  # Scale factor for influence
    
    # Calculate temperature with power influence
    df['Temperature'] = base_temp + power_influence - 10  # Adjustment to keep in reasonable range
    
    # Ensure temperature stays within physical limits
    df['Temperature'] = df['Temperature'].clip(-40, 80)
    
    # ------------------------
    # Dependent Attributes
    # ------------------------
    
    # Power Consumption Rate (influenced by temperature and battery level)
    df['Power_Consumption_Rate'] = base_power.copy()
    
    # Battery Level (initial calculation, will be refined)
    df['Battery_Level'] = np.random.uniform(40, 100, num_samples)  # Start with random values
    
    # Component Health (starting at 85-100%)
    df['Component_Health'] = np.random.uniform(85, 100, num_samples)
    
    # Battery Health (starting at 90-100%)
    df['Battery_Health'] = np.random.uniform(90, 100, num_samples)
    
    # Signal Strength (starting at 50-100%)
    df['Signal_Strength'] = np.random.uniform(50, 100, num_samples)
    
    # CPU & GPU Usage (starting at 10-90%)
    df['CPU_GPU_Usage'] = np.random.uniform(10, 90, num_samples)
    
    # ------------------------
    # Apply dependencies and interactions (multiple passes for complex interactions)
    # ------------------------
    
    # First pass: Calculate basic dependent relationships
    for i in range(num_samples):
        # Battery Level depends on Solar Panel Efficiency and Power Consumption
        df.at[i, 'Battery_Level'] = min(100, df.at[i, 'Battery_Level'] + 
                                      df.at[i, 'Solar_Panel_Efficiency'] * 0.3 - 
                                      df.at[i, 'Power_Consumption_Rate'] * 0.5)
        
        # Battery Health depends on Temperature, Time, and Docking
        temp_impact = 0.05 * max(0, df.at[i, 'Temperature'] - 20)  # Higher temps degrade battery
        time_impact = df.at[i, 'Days_Since_Start'] * 0.01  # Gradual wear over time
        docking_repair = 5 if df.at[i, 'Docking_Event'] == 1 else 0  # Docking improves battery health
        
        df.at[i, 'Battery_Health'] = df.at[i, 'Battery_Health'] - temp_impact - time_impact + docking_repair
        df.at[i, 'Battery_Health'] = min(100, max(0, df.at[i, 'Battery_Health']))  # Keep in range
        
        # Component Health depends on Time, Temperature, Docking, and Debris Risk
        comp_temp_impact = 0.03 * max(0, df.at[i, 'Temperature'] - 25)  # Higher temps degrade components
        comp_time_impact = df.at[i, 'Days_Since_Start'] * 0.008  # Gradual wear over time
        comp_docking_repair = 8 if df.at[i, 'Docking_Event'] == 1 else 0  # Docking improves component health
        comp_debris_impact = 0.2 * df.at[i, 'Debris_Risk_Level']  # Debris risk degrades components
        
        df.at[i, 'Component_Health'] = df.at[i, 'Component_Health'] - comp_temp_impact - comp_time_impact - comp_debris_impact + comp_docking_repair
        df.at[i, 'Component_Health'] = min(100, max(0, df.at[i, 'Component_Health']))  # Keep in range
    
    # Second pass: Refine interdependent relationships
    for i in range(num_samples):
        # Signal Strength depends on Battery Level and Debris Risk
        battery_signal_impact = max(0, (df.at[i, 'Battery_Level'] - 20) / 80 * 40)  # Scale to 0-40% impact
        debris_signal_impact = df.at[i, 'Debris_Risk_Level'] * 2  # Scale to 0-20% impact
        base_signal = np.random.uniform(40, 60)  # Base signal (40-60%)
        
        df.at[i, 'Signal_Strength'] = base_signal + battery_signal_impact - debris_signal_impact
        df.at[i, 'Signal_Strength'] = min(100, max(0, df.at[i, 'Signal_Strength']))  # Keep in range
        
        # Power Consumption affected by Temperature and Battery Level
        temp_power_factor = max(0, (df.at[i, 'Temperature'] + 40) / 120 * 20)  # Higher temp increases power for cooling
        battery_power_factor = max(0, (100 - df.at[i, 'Battery_Level']) / 100 * 15)  # Lower battery reduces power (power saving)
        
        df.at[i, 'Power_Consumption_Rate'] = df.at[i, 'Power_Consumption_Rate'] + temp_power_factor - battery_power_factor
        df.at[i, 'Power_Consumption_Rate'] = min(100, max(0, df.at[i, 'Power_Consumption_Rate']))  # Keep in range
        
        # CPU & GPU Usage depends on Power Consumption and Battery Level
        power_cpu_impact = df.at[i, 'Power_Consumption_Rate'] * 0.7  # Higher power often means higher CPU/GPU
        battery_cpu_factor = max(0, (100 - df.at[i, 'Battery_Level']) / 100 * 30)  # Lower battery reduces CPU/GPU (throttling)
        
        df.at[i, 'CPU_GPU_Usage'] = (power_cpu_impact - battery_cpu_factor + np.random.uniform(-10, 10))
        df.at[i, 'CPU_GPU_Usage'] = min(100, max(0, df.at[i, 'CPU_GPU_Usage']))  # Keep in range
    
    # Add some random noise to make the dataset more realistic
    df['Battery_Level'] += np.random.normal(0, 2, num_samples)
    df['Signal_Strength'] += np.random.normal(0, 3, num_samples)
    df['Power_Consumption_Rate'] += np.random.normal(0, 2, num_samples)
    df['CPU_GPU_Usage'] += np.random.normal(0, 5, num_samples)
    
    # Final cleanup: ensure all values are within proper ranges
    cols_to_clip = ['Battery_Level', 'Battery_Health', 'Signal_Strength', 
                    'Power_Consumption_Rate', 'Component_Health', 'CPU_GPU_Usage']
    for col in cols_to_clip:
        df[col] = df[col].clip(0, 100)
    
    # Round all numeric columns to 2 decimal places for readability
    for col in df.columns:
        if col != 'Timestamp' and col != 'Docking_Event' and col != 'Days_Since_Start':
            df[col] = df[col].round(2)
    
    return df

# Generate the dataset
np.random.seed(42)  # For reproducibility
satellite_data = generate_satellite_dataset(num_samples=1000)

# Save to CSV
satellite_data.to_csv('satellite_dataset.csv', index=False)

# Display sample of the dataset
print(satellite_data.head())
print("\nDataset shape:", satellite_data.shape)
print("\nDataset summary statistics:")
print(satellite_data.describe())

# Verify correlations between dependent and independent variables
print("\nCorrelation between key attributes:")
corr_matrix = satellite_data[['Solar_Panel_Efficiency', 'Temperature', 'Battery_Level', 
                             'Power_Consumption_Rate', 'Signal_Strength', 'Component_Health']].corr()
print(corr_matrix)