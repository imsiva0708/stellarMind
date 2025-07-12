import random
import os
import time
# from typing import Dict
import pandas as pd
import pickle

events= ["Battery Drain",
"Overheating",
"Solar Panel Misalignment",
"Signal Interference",
"Data Storage Overload",
"Component Wear",
"Thruster Misfire",
"Debris Near Miss",
"Debris Collision",
"Solar Storm"]


with open('model.pkl','rb') as f:
    model = pickle.load(f)

# def recalculate_dependent_attributes(attributes):
#     # Adjust Battery Level based on solar input and power drain
#     solar_input = attributes["Solar_Panel_Efficiency"] * (attributes["Battery_Health"] / 100)  # Degraded batteries charge less efficiently
#     attributes["Battery_Level"] = min(100, max(0, 
#         attributes["Battery_Level"] + solar_input * 0.6 - attributes["Power_Consumption_Rate"]
#     ))

#     # Power Consumption is affected by CPU usage, component health, and temperature
#     attributes["Power_Consumption_Rate"] = max(2, 
#         attributes["CPU_GPU_Usage"] * 0.3 + (100 - attributes["Component_Health"]) * 0.15 + attributes["Temperature"] * 0.05
#     )

#     # CPU/GPU Usage is influenced by Component Health, Temperature, and Data Storage
#     attributes["CPU_GPU_Usage"] = max(10, 
#         (100 - attributes["Component_Health"]) * 0.3 + attributes["Temperature"] * 0.1 + attributes["Data_Storage_Used"] * 0.2
#     )

#     return attributes

def recalculate_dependent_attributes(attributes):
    # Calculate Power Consumption first as it affects other attributes
    # Base power draw plus factors for CPU usage, component health, and temperature
    base_power = 10  # Minimum power draw when idle
    cpu_factor = attributes["CPU_GPU_Usage"] * 0.3
    health_factor = (100 - attributes["Component_Health"]) * 0.15
    temp_factor = max(0, (attributes["Temperature"] - 20) * 0.2)  # Temperature above 20°C increases power
    
    attributes["Power_Consumption_Rate"] = min(100, base_power + cpu_factor + health_factor + temp_factor)
    
    # Update CPU/GPU Usage based on component health, temperature, and storage used
    base_cpu = 8  # Minimum CPU usage for system operations
    health_impact = (100 - attributes["Component_Health"]) * 0.3
    temp_impact = max(0, (attributes["Temperature"] - 25) * 0.25)  # Performance degrades above optimal temp
    storage_impact = attributes["Data_Storage_Used"] * 0.2
    
    attributes["CPU_GPU_Usage"] = min(100, max(base_cpu, attributes["CPU_GPU_Usage"] * 0.7 + 
                                              health_impact + temp_impact + storage_impact))
    
    # Update Battery Level based on solar input, power consumption, and health
    # Calculate effective solar input (adjusted for panel efficiency and battery health)
    max_solar_input = 25  # Maximum power generation per cycle
    effective_efficiency = attributes["Solar_Panel_Efficiency"] / 100
    battery_efficiency = attributes["Battery_Health"] / 100
    solar_input = max_solar_input * effective_efficiency * battery_efficiency
    
    # Calculate net power balance
    power_balance = solar_input - attributes["Power_Consumption_Rate"]
    
    # Battery charge or discharge rate depends on power balance and current level
    charge_rate = 1.0  # Normal rate
    if attributes["Battery_Level"] > 80:
        charge_rate = 0.5  # Slower charging at high levels
    if attributes["Battery_Level"] < 20:
        charge_rate = 1.5  # Faster charging at low levels
    
    attributes["Battery_Level"] = max(0, min(100, 
        attributes["Battery_Level"] + (power_balance * charge_rate * 0.1)))
    
    return attributes




def initialize_attributes():
    # Independent Attributes (Set to Good Condition)
    battery_health = 90.00  # %
    solar_panel_efficiency = 85.00  # %
    temperature = 25.00  # °C
    signal_strength = 80.00  # %
    component_health = 90.00  # %

    # Derived Attributes (Using Formulas)
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
    Modifies only independent attributes based on the event and recalculates dependent ones.
    """
    # Extract current values
    attributes = attributes_df.iloc[0].to_dict()
    print(event)

    # Modify independent attributes based on the event
    # if event == "Battery Drain":
    #     attributes["Battery_Level"] -= 15  # High drop
    # elif event == "Overheating":
    #     attributes["Battery_Level"] -= 10
    #     attributes["Temperature"] += 10  # High increase
    # elif event == "Solar Panel Misalignment":
    #     attributes["Battery_Level"] -= 10
    #     attributes["Solar_Panel_Efficiency"] -= 15  # High drop
    # elif event == "Signal Interference":
    #     attributes["Signal_Strength"] -= 20  # High drop
    # elif event == "Data Storage Overload":
    #     attributes["Data_Storage_Used"] += 20  # High increase
    # elif event == "Component Wear":
    #     attributes["Component_Health"] -= 10  # Medium drop
    # elif event == "Thruster Misfire":
    #     attributes["Battery_Level"] -= 10
    #     attributes["Temperature"] += 5  # Medium increase
    #     attributes["Component_Health"] -= 10  # Medium drop
    # elif event == "Debris Near Miss":
    #     attributes["Debris_Risk_Level"] += 10  # High increase
    # elif event == "Debris Collision":
    #     attributes["Solar_Panel_Efficiency"] -= 10  # Medium drop
    #     attributes["Temperature"] += 5  # Medium increase
    #     attributes["Component_Health"] -= 20  # High drop
    # elif event == "Solar Storm":
    #     attributes["Battery_Level"] -= 10
    #     attributes["Solar_Panel_Efficiency"] -= 10
    #     attributes["Temperature"] += 15  # High increase
    #     attributes["Signal_Strength"] -= 15  # High drop
    #     attributes["Component_Health"] -= 10  # Medium drop

    
    if event == "Battery Drain":
        attributes["Battery_Level"] -= 12  # Significant but not extreme
        attributes["Battery_Health"] -= 2  # Minor permanent degradation
        
    elif event == "Overheating":
        attributes["Temperature"] += 15  # Significant temperature spike
        # Battery impact handled by formula (temperature affects power consumption and battery)
        
    elif event == "Solar Panel Misalignment":
        attributes["Solar_Panel_Efficiency"] -= 18  # Significant efficiency loss
        # Battery impact will be calculated by formula based on reduced solar input
        
    elif event == "Signal Interference":
        attributes["Signal_Strength"] -= 25  # Significant drop
        attributes["CPU_GPU_Usage"] += 8  # System works harder to maintain connection
        
    elif event == "Data Storage Overload":
        attributes["Data_Storage_Used"] += 25  # Significant increase
        # CPU impact handled by formula (storage affects CPU usage)
        
    elif event == "Component Wear":
        attributes["Component_Health"] -= 8  # Gradual degradation
        # Power and CPU impacts handled by formula
        
    elif event == "Thruster Misfire":
        attributes["Component_Health"] -= 12  # System stress
        attributes["Temperature"] += 8  # Heat from misfire
        attributes["Power_Consumption_Rate"] += 5  # Direct temporary power surge
        
    elif event == "Debris Near Miss":
        attributes["Debris_Risk_Level"] += 15  # Elevated risk
        attributes["CPU_GPU_Usage"] += 10  # Increased monitoring and evasion calculations
        
    elif event == "Debris Collision":
        attributes["Component_Health"] -= 18  # Significant damage
        attributes["Solar_Panel_Efficiency"] -= 15  # Panel damage
        attributes["Temperature"] += 6  # Friction heating
        attributes["Debris_Risk_Level"] += 20  # Surrounding debris field
        
    elif event == "Solar Storm":
        attributes["Signal_Strength"] -= 20  # Interference
        attributes["Temperature"] += 12  # Radiation heating
        attributes["Solar_Panel_Efficiency"] += 5  # Temporarily increased solar energy
        attributes["Battery_Health"] -= 3  # Radiation damage to batteries
        attributes["Component_Health"] -= 5  # Electronics stress
        # Recalculate dependent attributes
    attributes = recalculate_dependent_attributes(attributes)

    # Update the DataFrame
    return pd.DataFrame([attributes])



def main1():
    attributes = initialize_attributes()
    while True:
        time.sleep(1)
        os.system('cls')
        attributes = apply_event(random.choice(events), attributes)
        print(attributes.to_string(index=False))
        y_pred = model.predict(attributes)
        print(y_pred)

if __name__ == '__main__':
    main1()
