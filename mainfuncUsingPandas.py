import random
import os
import time
import pandas as pd
import pickle

events = [
    "Battery Drain",
    "Overheating",
    "Solar Panel Misalignment",
    "Signal Interference",
    "Data Storage Overload",
    "Component Wear",
    "Thruster Misfire",
    "Debris Near Miss",
    "Debris Collision",
    "Solar Storm"
]

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def initialize_attributes():
    # Independent Attributes (Set to Good Condition)
    battery_health = 90.00  # %
    solar_panel_efficiency = 85.00  # %
    temperature = 25.00  # °C
    signal_strength = 80.00  # %
    component_health = 90.00  # %
    
    # Calculate derived attributes directly
    battery_level = min(100, solar_panel_efficiency - (100 - battery_health) * 0.3)
    power_consumption_rate = max(5, (100 - component_health) * 0.2 + temperature * 0.1)
    cpu_gpu_usage = max(10, (100 - component_health) * 0.5 + temperature * 0.3)
    data_storage_used = random.uniform(10, 30)  # Starts low (increases over time)
    debris_risk_level = random.uniform(1, 3)  # Low risk initially

    # Return all attributes in a structured format
    dict1 = {
        "Battery_Level": round(battery_level, 2),
        "Battery_Health": battery_health,
        "Signal_Strength": signal_strength,
        "Power_Consumption_Rate": round(power_consumption_rate, 2),
        "Component_Health": component_health,
        "CPU_GPU_Usage": round(cpu_gpu_usage, 2),
        "Solar_Panel_Efficiency": solar_panel_efficiency,
        "Temperature": temperature,
        "Data_Storage_Used": round(data_storage_used, 2),
        "Debris_Risk_Level": round(debris_risk_level, 2)
    }
    return pd.DataFrame([dict1])

def apply_event(event, attributes_df):
    """
    Modifies all affected attributes directly based on the event,
    considering both direct and indirect effects.
    """
    # Extract current values
    attributes = attributes_df.iloc[0].to_dict()
    print(event)

    # Get current values for calculations
    battery_level = attributes["Battery_Level"]
    battery_health = attributes["Battery_Health"]
    solar_panel_efficiency = attributes["Solar_Panel_Efficiency"]
    temperature = attributes["Temperature"]
    signal_strength = attributes["Signal_Strength"]
    component_health = attributes["Component_Health"]
    cpu_gpu_usage = attributes["CPU_GPU_Usage"]
    power_consumption_rate = attributes["Power_Consumption_Rate"]
    data_storage_used = attributes["Data_Storage_Used"]
    debris_risk_level = attributes["Debris_Risk_Level"]
    
    # Apply event-specific changes
    if event == "Battery Drain":
        battery_level -= 12  # Direct effect
        battery_health -= 2  # Direct effect
        # Secondary effects
        power_consumption_rate += 3  # System compensates
        cpu_gpu_usage += 5  # Additional monitoring processes
        
    elif event == "Overheating":
        temperature += 15  # Direct effect
        # Secondary effects
        battery_level -= 5  # Heat degrades charge
        power_consumption_rate += 8  # Cooling systems activate
        cpu_gpu_usage += 7  # Thermal management processes
        component_health -= 3  # Heat stress on components
        
    elif event == "Solar Panel Misalignment":
        solar_panel_efficiency -= 18  # Direct effect
        # Secondary effects
        battery_level -= 8  # Reduced charging
        power_consumption_rate += 4  # System tries to compensate
        cpu_gpu_usage += 6  # Realignment calculations
        
    elif event == "Signal Interference":
        signal_strength -= 25  # Direct effect
        # Secondary effects
        cpu_gpu_usage += 12  # Signal processing overhead
        power_consumption_rate += 7  # Higher transmission power
        battery_level -= 4  # Extra power draw
        
    elif event == "Data Storage Overload":
        data_storage_used += 25  # Direct effect
        # Secondary effects
        cpu_gpu_usage += 15  # Processing overhead
        power_consumption_rate += 8  # Higher disk activity
        battery_level -= 5  # Extra power consumption
        temperature += 4  # Heat from processing
        
    elif event == "Component Wear":
        component_health -= 8  # Direct effect
        # Secondary effects
        power_consumption_rate += 6  # Inefficient operation
        cpu_gpu_usage += 7  # Error handling overhead
        battery_level -= 3  # Higher power draw
        temperature += 3  # Friction and resistance
        
    elif event == "Thruster Misfire":
        component_health -= 12  # Direct effect
        temperature += 8  # Direct effect
        # Secondary effects
        power_consumption_rate += 10  # Thruster power surge
        battery_level -= 7  # Power drain
        cpu_gpu_usage += 9  # Navigation recalculation
        
    elif event == "Debris Near Miss":
        debris_risk_level += 15  # Direct effect
        # Secondary effects
        cpu_gpu_usage += 14  # Evasion calculations
        power_consumption_rate += 8  # Evasive maneuvers
        battery_level -= 5  # Extra power consumption
        
    elif event == "Debris Collision":
        component_health -= 18  # Direct effect
        solar_panel_efficiency -= 15  # Direct effect
        temperature += 6  # Direct effect
        debris_risk_level += 20  # Direct effect
        # Secondary effects
        battery_level -= 12  # Damage and systems response
        power_consumption_rate += 12  # Damage control systems
        cpu_gpu_usage += 15  # Diagnostic and recovery
        signal_strength -= 10  # Antenna damage
        
    elif event == "Solar Storm":
        signal_strength -= 20  # Direct effect
        temperature += 12  # Direct effect
        solar_panel_efficiency += 5  # Direct effect (temporary boost)
        battery_health -= 3  # Direct effect
        component_health -= 5  # Direct effect
        # Secondary effects
        battery_level -= 8  # Radiation effects
        power_consumption_rate += 10  # Protective systems
        cpu_gpu_usage += 12  # Monitoring and shielding

    # Enforce boundaries on all values
    attributes["Battery_Level"] = max(0, min(100, battery_level))
    attributes["Battery_Health"] = max(0, min(100, battery_health))
    attributes["Solar_Panel_Efficiency"] = max(0, min(100, solar_panel_efficiency))
    attributes["Temperature"] = max(-50, min(100, temperature))
    attributes["Signal_Strength"] = max(0, min(100, signal_strength))
    attributes["Component_Health"] = max(0, min(100, component_health))
    attributes["CPU_GPU_Usage"] = max(0, min(100, cpu_gpu_usage))
    attributes["Power_Consumption_Rate"] = max(0, min(100, power_consumption_rate))
    attributes["Data_Storage_Used"] = max(0, min(100, data_storage_used))
    attributes["Debris_Risk_Level"] = max(0, min(100, debris_risk_level))
    
    # Round all values to 2 decimal places
    for key in attributes:
        attributes[key] = round(attributes[key], 2)

    # Update the DataFrame
    return pd.DataFrame([attributes])

def main():
    attributes = initialize_attributes()
    while True:
        time.sleep(1)
        os.system('cls')
        attributes = apply_event(random.choice(events), attributes)
        print(attributes.to_string(index=False))
        y_pred = model.predict(attributes)
        print(y_pred)

if __name__ == '__main__':
    main()