import random
import os
import time
from typing import Dict
# import pandas as pd

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

def recalculate_dependent_attributes(attributes: Dict[str:float]) -> Dict[str:float]:
    attributes["Battery_Level"] = min(100, max(0, 
        attributes["Battery_Level"] + attributes["Solar_Panel_Efficiency"] * 0.8 - attributes["Power_Consumption_Rate"]
    ))

    attributes["Power_Consumption_Rate"] = max(2, 
        attributes["CPU_GPU_Usage"] * 0.3 + (100 - attributes["Component_Health"]) * 0.15 + attributes["Temperature"] * 0.05
    )

    attributes["CPU_GPU_Usage"] = max(10, 
        (100 - attributes["Component_Health"]) * 0.3 + attributes["Temperature"] * 0.1 + attributes["Data_Storage_Used"] * 0.2
    )

    return attributes

def initialize_attributes():
    # Independent Attributes (Set to Good Condition)
    battery_health = 90  # %
    solar_panel_efficiency = 85  # %
    temperature = 25  # °C
    signal_strength = 80  # %
    component_health = 90  # %

    # Derived Attributes (Using Formulas)
    battery_level = min(100, solar_panel_efficiency - (100 - battery_health) * 0.3)  
    power_consumption_rate = max(5, (100 - component_health) * 0.2 + temperature * 0.1)  
    cpu_gpu_usage = max(10, (100 - component_health) * 0.5 + temperature * 0.3)  
    data_storage_used = random.uniform(10, 30)  # Starts low (increases over time)  
    debris_risk_level = random.uniform(1, 3)  # Low risk initially  

    # Return all attributes in a structured format
    return {
        "Battery_Health": battery_health,
        "Battery_Level": round(battery_level, 2),
        "Solar_Panel_Efficiency": solar_panel_efficiency,
        "Temperature": temperature,
        "Signal_Strength": signal_strength,
        "Component_Health": component_health,
        "Power_Consumption_Rate": round(power_consumption_rate, 2),
        "CPU_GPU_Usage": round(cpu_gpu_usage, 2),
        "Data_Storage_Used": round(data_storage_used, 2),
        "Debris_Risk_Level": round(debris_risk_level, 2)
    }


def apply_event(event, attributes):
    """
    Modifies only independent attributes based on the event and recalculates dependent ones.
    """
    # Extract current values
    battery_health = attributes["Battery_Health"]
    solar_efficiency = attributes["Solar_Panel_Efficiency"]
    temperature = attributes["Temperature"]
    signal_strength = attributes["Signal_Strength"]
    component_health = attributes["Component_Health"]

    # Modify independent attributes based on the event
    if event == "Battery Drain":
        attributes["Battery_Level"] -= 15  # High drop
    elif event == "Overheating":
        attributes["Battery_Level"] -= 10
        attributes["Temperature"] += 10  # High increase
    elif event == "Solar Panel Misalignment":
        attributes["Battery_Level"] -= 10
        attributes["Solar_Panel_Efficiency"] -= 15  # High drop
    elif event == "Signal Interference":
        attributes["Signal_Strength"] -= 20  # High drop
    elif event == "Data Storage Overload":
        attributes["Data_Storage_Used"] += 20  # High increase
    elif event == "Component Wear":
        attributes["Component_Health"] -= 10  # Medium drop
    elif event == "Thruster Misfire":
        attributes["Battery_Level"] -= 10
        attributes["Temperature"] += 5  # Medium increase
        attributes["Component_Health"] -= 10  # Medium drop
    elif event == "Debris Near Miss":
        attributes["Debris_Risk_Level"] += 10  # High increase
    elif event == "Debris Collision":
        attributes["Solar_Panel_Efficiency"] -= 10  # Medium drop
        attributes["Temperature"] += 5  # Medium increase
        attributes["Component_Health"] -= 20  # High drop
    elif event == "Solar Storm":
        attributes["Battery_Level"] -= 10
        attributes["Solar_Panel_Efficiency"] -= 10
        attributes["Temperature"] += 15  # High increase
        attributes["Signal_Strength"] -= 15  # High drop
        attributes["Component_Health"] -= 10  # Medium drop


    attributes = recalculate_dependent_attributes(attributes)

    return attributes

while True:
    time.sleep(1)
    os.system('cls')
    attributes = initialize_attributes()
    attributes = apply_event(random.choice(events),attributes)
    for key, value in attributes.items():
        print(f"{key}: {value}")
