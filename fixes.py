# import random
# import numpy as np
# import pandas as pd


# class Fixes:
#     def __init__(self):
#         self.actions = {
#             'Reroute power to core functions': self.reroute_power,
#             'Adjust orientation for passive cooling': self.passive_cooling,
#             'Recalibrate position, tweak pitch, roll, yaw': self.recalibrate_position,
#             'Initiate Docking sequence to ISS': self.initiate_docking,
#             'Increase cooling system power': self.increase_cooling,
#             'Adjust antenna position or switch frequency': self.adjust_antenna,
#             'Optimize data transmission': self.optimize_transmission,
#             'Delete unnecessary data': self.delete_data,
#             'Adjust pitch, yaw, roll for sunlight absorption': self.adjust_sunlight_absorption,
#             'Disable non-essential systems': self.disable_non_essential_systems,
#             'Redistribute workload, reduce power to affected components': self.redistribute_workload
#         }

#     def reroute_power(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
#         attributes = attributes_df.iloc[0].to_dict()
#         attributes['Battery_Level'] = max(0, attributes['Battery_Level'] - random.randint(10, 20))
#         attributes['Power_Consumption_Rate'] = max(5, attributes['Power_Consumption_Rate'] - random.randint(10, 25))
#         attributes['CPU_GPU_Usage'] = max(5, attributes['CPU_GPU_Usage'] - random.randint(10, 20))
#         attributes = recalculate_dependent_attributes(attributes)
#         return pd.DataFrame([attributes])

#     def passive_cooling(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
#         attributes = attributes_df.iloc[0].to_dict()
#         attributes['Temperature'] = max(0, attributes['Temperature'] - random.randint(10, 20))
#         attributes['Power_Consumption_Rate'] = min(100, attributes['Power_Consumption_Rate'] + random.randint(5, 15))
#         attributes = recalculate_dependent_attributes(attributes)
#         return pd.DataFrame([attributes])

#     def recalibrate_position(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
#         attributes = attributes_df.iloc[0].to_dict()
#         attributes['Debris_Risk_Level'] = max(0, attributes['Debris_Risk_Level'] - random.randint(5, 10))
#         attributes['Power_Consumption_Rate'] = min(100, attributes['Power_Consumption_Rate'] + random.randint(10, 20))
#         attributes['CPU_GPU_Usage'] = min(100, attributes['CPU_GPU_Usage'] + random.randint(8, 15))
#         attributes = recalculate_dependent_attributes(attributes)
#         return pd.DataFrame([attributes])

#     def initiate_docking(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
#         attributes = attributes_df.iloc[0].to_dict()
#         attributes['Battery_Health'] = min(100, attributes['Battery_Health'] + random.randint(20, 50))
#         attributes['Component_Health'] = min(100, attributes['Component_Health'] + random.randint(30, 60))
#         attributes['Battery_Level'] = min(100, attributes['Battery_Level'] + random.randint(50, 100))
#         attributes['Data_Storage_Used'] = max(0, attributes['Data_Storage_Used'] - random.randint(30, 70))
#         attributes = recalculate_dependent_attributes(attributes)
#         return pd.DataFrame([attributes])

#     def increase_cooling(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
#         attributes = attributes_df.iloc[0].to_dict()
#         attributes['Temperature'] = max(0, attributes['Temperature'] - random.randint(15, 30))
#         attributes['Power_Consumption_Rate'] = min(100, attributes['Power_Consumption_Rate'] + random.randint(10, 20))
#         attributes['CPU_GPU_Usage'] = min(100, attributes['CPU_GPU_Usage'] + random.randint(8, 15))
#         attributes = recalculate_dependent_attributes(attributes)
#         return pd.DataFrame([attributes])

#     def adjust_antenna(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
#         attributes = attributes_df.iloc[0].to_dict()
#         attributes['Signal_Strength'] = min(100, attributes['Signal_Strength'] + random.randint(15, 30))
#         attributes['Power_Consumption_Rate'] = min(100, attributes['Power_Consumption_Rate'] + random.randint(5, 10))
#         attributes = recalculate_dependent_attributes(attributes)
#         return pd.DataFrame([attributes])

#     def optimize_transmission(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
#         attributes = attributes_df.iloc[0].to_dict()
#         attributes['Data_Storage_Used'] = max(0, attributes['Data_Storage_Used'] - random.randint(10, 25))
#         attributes['CPU_GPU_Usage'] = min(100, attributes['CPU_GPU_Usage'] + random.randint(10, 20))
#         attributes['Signal_Strength'] = max(0, attributes['Signal_Strength'] - random.randint(5, 10))
#         attributes = recalculate_dependent_attributes(attributes)
#         return pd.DataFrame([attributes])

#     def delete_data(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
#         attributes = attributes_df.iloc[0].to_dict()
#         attributes['Data_Storage_Used'] = max(0, attributes['Data_Storage_Used'] - random.randint(20, 40))
#         attributes['CPU_GPU_Usage'] = min(100, attributes['CPU_GPU_Usage'] + random.randint(5, 15))
#         attributes = recalculate_dependent_attributes(attributes)
#         return pd.DataFrame([attributes])

#     def adjust_sunlight_absorption(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
#         attributes = attributes_df.iloc[0].to_dict()
#         attributes['Solar_Panel_Efficiency'] = min(100, attributes['Solar_Panel_Efficiency'] + random.randint(10, 25))
#         attributes['Power_Consumption_Rate'] = min(100, attributes['Power_Consumption_Rate'] + random.randint(5, 10))
#         attributes = recalculate_dependent_attributes(attributes)
#         return pd.DataFrame([attributes])

#     def disable_non_essential_systems(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
#         attributes = attributes_df.iloc[0].to_dict()
#         attributes['Power_Consumption_Rate'] = max(5, attributes['Power_Consumption_Rate'] - random.randint(15, 30))
#         attributes['CPU_GPU_Usage'] = max(5, attributes['CPU_GPU_Usage'] - random.randint(10, 20))
#         attributes = recalculate_dependent_attributes(attributes)
#         return pd.DataFrame([attributes])

#     def redistribute_workload(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
#         attributes = attributes_df.iloc[0].to_dict()
#         attributes['CPU_GPU_Usage'] = max(5, attributes['CPU_GPU_Usage'] - random.randint(10, 20))
#         attributes['Power_Consumption_Rate'] = max(5, attributes['Power_Consumption_Rate'] - random.randint(8, 15))
#         attributes['Component_Health'] = min(100, attributes['Component_Health'] + random.randint(5, 10))
#         attributes = recalculate_dependent_attributes(attributes)
#         return pd.DataFrame([attributes])

#     def apply_fixes(self, data: pd.DataFrame, inputs: np.ndarray) -> pd.DataFrame:
#         for i, (action_name, action_func) in zip(inputs[0], self.actions.items()):
#             if i == 1:  # Execute only if the inputs value is 1
#                 print(f"Executing action: {action_name}")
#                 data = action_func(data)
#         return data

# # Example usage
# if __name__ == "__main__":
#     data = pd.DataFrame([{
#         "Battery_Level": 90.0,
#         "Battery_Health": 40.0,
#         "Signal_Strength": 80.0,
#         "Power_Consumption_Rate": 20.0,
#         "Component_Health": 70.0,
#         "CPU_GPU_Usage": 30.0,
#         "Solar_Panel_Efficiency": 60.0,
#         "Temperature": 25.0,
#         "Data_Storage_Used": 21.27,
#         "Debris_Risk_Level": 2.25
#     }])
#     inputs = np.array([[0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0]])
#     fixes = Fixes()
#     data = fixes.apply_fixes(data, inputs)
#     print(data)
import random
import numpy as np
import pandas as pd


class Fixes:
    def __init__(self):
        self.actions = {
            'Reroute power to core functions': self.reroute_power,
            'Adjust orientation for passive cooling': self.passive_cooling,
            'Recalibrate position, tweak pitch, roll, yaw': self.recalibrate_position,
            'Initiate Docking sequence to ISS': self.initiate_docking,
            'Increase cooling system power': self.increase_cooling,
            'Adjust antenna position or switch frequency': self.adjust_antenna,
            'Optimize data transmission': self.optimize_transmission,
            'Delete unnecessary data': self.delete_data,
            'Adjust pitch, yaw, roll for sunlight absorption': self.adjust_sunlight_absorption,
            'Disable non-essential systems': self.disable_non_essential_systems,
            'Redistribute workload, reduce power to affected components': self.redistribute_workload
        }

    def reroute_power(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
        attributes = attributes_df.iloc[0].to_dict()
        # Direct changes
        power_reduction = random.randint(10, 25)
        cpu_reduction = random.randint(10, 20)
        
        # Apply primary changes - IMPROVED BATTERY IMPACT
        attributes['Power_Consumption_Rate'] = max(5, attributes['Power_Consumption_Rate'] - power_reduction)
        attributes['CPU_GPU_Usage'] = max(5, attributes['CPU_GPU_Usage'] - cpu_reduction)
        # Instead of draining battery, now rerouting power INCREASES battery level
        attributes['Battery_Level'] = min(100, attributes['Battery_Level'] + random.randint(8, 15))
        
        # Apply secondary effects
        attributes['Temperature'] = max(0, attributes['Temperature'] - 3)  # Less heat from lower power use
        attributes['Component_Health'] = min(100, attributes['Component_Health'] + 2)  # Less stress on components
        
        # Round values
        for key in attributes:
            attributes[key] = round(attributes[key], 2)
            
        return pd.DataFrame([attributes])

    def passive_cooling(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
        attributes = attributes_df.iloc[0].to_dict()
        # Direct changes
        temp_reduction = random.randint(10, 20)
        power_increase = random.randint(5, 15)
        
        # Apply primary changes - IMPROVED BATTERY IMPACT
        attributes['Temperature'] = max(0, attributes['Temperature'] - temp_reduction)
        attributes['Power_Consumption_Rate'] = min(100, attributes['Power_Consumption_Rate'] + power_increase)
        # Reduced power draw from cooling systems saves more battery
        attributes['Battery_Level'] = min(100, attributes['Battery_Level'] + random.randint(3, 8))
        
        # Apply secondary effects
        attributes['CPU_GPU_Usage'] = min(100, attributes['CPU_GPU_Usage'] + 5)  # Additional orientation control
        attributes['Component_Health'] = min(100, attributes['Component_Health'] + 2)  # Reduced thermal stress
        
        # Round values
        for key in attributes:
            attributes[key] = round(attributes[key], 2)
            
        return pd.DataFrame([attributes])

    def recalibrate_position(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
        attributes = attributes_df.iloc[0].to_dict()
        # Direct changes
        debris_reduction = random.randint(5, 10)
        power_increase = random.randint(10, 20)
        cpu_increase = random.randint(8, 15)
        
        # Apply primary changes - MODERATE BATTERY IMPACT
        attributes['Debris_Risk_Level'] = max(0, attributes['Debris_Risk_Level'] - debris_reduction)
        attributes['Power_Consumption_Rate'] = min(100, attributes['Power_Consumption_Rate'] + power_increase)
        attributes['CPU_GPU_Usage'] = min(100, attributes['CPU_GPU_Usage'] + cpu_increase)
        
        # Still uses battery, but less than before
        attributes['Battery_Level'] = max(0, attributes['Battery_Level'] - random.randint(1, 3))
        
        # Apply secondary effects
        attributes['Signal_Strength'] = min(100, attributes['Signal_Strength'] + 3)  # Better antenna alignment
        attributes['Temperature'] = min(100, attributes['Temperature'] + 2)  # Heat from thrusters
        
        # Round values
        for key in attributes:
            attributes[key] = round(attributes[key], 2)
            
        return pd.DataFrame([attributes])

    def initiate_docking(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
        attributes = attributes_df.iloc[0].to_dict()
        # Direct changes - GREATLY IMPROVED BATTERY IMPACT
        battery_health_boost = random.randint(20, 50)
        component_health_boost = random.randint(30, 60)
        battery_level_boost = random.randint(80, 100)  # Increased from 50-100 to 80-100
        data_storage_reduction = random.randint(30, 70)
        
        # Apply primary changes
        attributes['Battery_Health'] = min(100, attributes['Battery_Health'] + battery_health_boost)
        attributes['Component_Health'] = min(100, attributes['Component_Health'] + component_health_boost)
        attributes['Battery_Level'] = min(100, attributes['Battery_Level'] + battery_level_boost)
        attributes['Data_Storage_Used'] = max(0, attributes['Data_Storage_Used'] - data_storage_reduction)
        
        # Apply secondary effects
        attributes['Signal_Strength'] = min(100, attributes['Signal_Strength'] + 20)  # Connected to ISS comms
        attributes['Power_Consumption_Rate'] = max(5, attributes['Power_Consumption_Rate'] - 15)  # External power
        attributes['CPU_GPU_Usage'] = max(5, attributes['CPU_GPU_Usage'] - 10)  # Offload to ISS systems
        attributes['Temperature'] = 25  # Climate controlled environment
        attributes['Solar_Panel_Efficiency'] = min(100, attributes['Solar_Panel_Efficiency'] + 15)  # Maintenance
        attributes['Debris_Risk_Level'] = max(0, attributes['Debris_Risk_Level'] - 5)  # ISS protection
        
        # Round values
        for key in attributes:
            attributes[key] = round(attributes[key], 2)
            
        return pd.DataFrame([attributes])

    def increase_cooling(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
        attributes = attributes_df.iloc[0].to_dict()
        # Direct changes
        temp_reduction = random.randint(15, 30)
        power_increase = random.randint(10, 20)
        cpu_increase = random.randint(8, 15)
        
        # Apply primary changes - IMPROVED BATTERY IMPACT
        attributes['Temperature'] = max(0, attributes['Temperature'] - temp_reduction)
        attributes['Power_Consumption_Rate'] = min(100, attributes['Power_Consumption_Rate'] + power_increase)
        attributes['CPU_GPU_Usage'] = min(100, attributes['CPU_GPU_Usage'] + cpu_increase)
        
        # Apply secondary effects - More efficient cooling helps battery performance
        attributes['Battery_Level'] = max(0, attributes['Battery_Level'] - random.randint(2, 5))  # Reduced from -8
        attributes['Component_Health'] = min(100, attributes['Component_Health'] + 5)  # Reduced thermal stress
        
        # Round values
        for key in attributes:
            attributes[key] = round(attributes[key], 2)
            
        return pd.DataFrame([attributes])

    def adjust_antenna(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
        attributes = attributes_df.iloc[0].to_dict()
        # Direct changes
        signal_boost = random.randint(15, 30)
        power_increase = random.randint(5, 10)
        
        # Apply primary changes - IMPROVED BATTERY IMPACT
        attributes['Signal_Strength'] = min(100, attributes['Signal_Strength'] + signal_boost)
        attributes['Power_Consumption_Rate'] = min(100, attributes['Power_Consumption_Rate'] + power_increase)
        
        # Apply secondary effects - More efficient orientation means less battery drain
        attributes['CPU_GPU_Usage'] = min(100, attributes['CPU_GPU_Usage'] + 5)  # Signal processing
        attributes['Battery_Level'] = max(0, attributes['Battery_Level'] - random.randint(1, 2))  # Reduced from -3
        attributes['Data_Storage_Used'] = max(0, attributes['Data_Storage_Used'] - 2)  # Transmit cached data
        
        # Round values
        for key in attributes:
            attributes[key] = round(attributes[key], 2)
            
        return pd.DataFrame([attributes])

    def optimize_transmission(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
        attributes = attributes_df.iloc[0].to_dict()
        # Direct changes - IMPROVED BATTERY IMPACT
        data_reduction = random.randint(10, 25)
        cpu_increase = random.randint(10, 20)
        signal_reduction = random.randint(5, 10)
        
        # Apply primary changes
        attributes['Data_Storage_Used'] = max(0, attributes['Data_Storage_Used'] - data_reduction)
        attributes['CPU_GPU_Usage'] = min(100, attributes['CPU_GPU_Usage'] + cpu_increase)
        attributes['Signal_Strength'] = max(0, attributes['Signal_Strength'] - signal_reduction)
        
        # Apply secondary effects - Efficient transmission saves power
        attributes['Battery_Level'] = min(100, attributes['Battery_Level'] + random.randint(1, 4))  # Changed from -5 to +1-4
        attributes['Power_Consumption_Rate'] = min(100, attributes['Power_Consumption_Rate'] + 7)  # Processing power
        
        # Round values
        for key in attributes:
            attributes[key] = round(attributes[key], 2)
            
        return pd.DataFrame([attributes])

    def delete_data(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
        attributes = attributes_df.iloc[0].to_dict()
        # Direct changes - IMPROVED BATTERY IMPACT
        data_reduction = random.randint(20, 40)
        cpu_increase = random.randint(5, 15)
        
        # Apply primary changes
        attributes['Data_Storage_Used'] = max(0, attributes['Data_Storage_Used'] - data_reduction)
        attributes['CPU_GPU_Usage'] = min(100, attributes['CPU_GPU_Usage'] + cpu_increase)
        
        # Apply secondary effects
        attributes['Power_Consumption_Rate'] = min(100, attributes['Power_Consumption_Rate'] + 4)  # Processing overhead
        attributes['Battery_Level'] = min(100, attributes['Battery_Level'] + random.randint(3, 7))  # Changed from -2 to +3-7
        
        # Round values
        for key in attributes:
            attributes[key] = round(attributes[key], 2)
            
        return pd.DataFrame([attributes])

    def adjust_sunlight_absorption(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
        attributes = attributes_df.iloc[0].to_dict()
        # Direct changes - GREATLY IMPROVED BATTERY IMPACT
        solar_boost = random.randint(10, 25)
        power_increase = random.randint(5, 10)
        
        # Apply primary changes
        attributes['Solar_Panel_Efficiency'] = min(100, attributes['Solar_Panel_Efficiency'] + solar_boost)
        attributes['Power_Consumption_Rate'] = min(100, attributes['Power_Consumption_Rate'] + power_increase)
        
        # Apply secondary effects - Much better charging
        attributes['Battery_Level'] = min(100, attributes['Battery_Level'] + random.randint(15, 25))  # Increased from +5
        attributes['CPU_GPU_Usage'] = min(100, attributes['CPU_GPU_Usage'] + 3)  # Orientation calculations
        attributes['Temperature'] = min(100, attributes['Temperature'] + 2)  # More sun exposure
        
        # Round values
        for key in attributes:
            attributes[key] = round(attributes[key], 2)
            
        return pd.DataFrame([attributes])

    def disable_non_essential_systems(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
        attributes = attributes_df.iloc[0].to_dict()
        # Direct changes - GREATLY IMPROVED BATTERY IMPACT
        power_reduction = random.randint(15, 30)
        cpu_reduction = random.randint(10, 20)
        
        # Apply primary changes
        attributes['Power_Consumption_Rate'] = max(5, attributes['Power_Consumption_Rate'] - power_reduction)
        attributes['CPU_GPU_Usage'] = max(5, attributes['CPU_GPU_Usage'] - cpu_reduction)
        
        # Apply secondary effects - Much more battery savings
        attributes['Battery_Level'] = min(100, attributes['Battery_Level'] + random.randint(10, 20))  # Increased from +3
        attributes['Temperature'] = max(0, attributes['Temperature'] - 4)  # Less heat generation
        attributes['Signal_Strength'] = max(0, attributes['Signal_Strength'] - 5)  # Comms partially disabled
        
        # Round values
        for key in attributes:
            attributes[key] = round(attributes[key], 2)
            
        return pd.DataFrame([attributes])

    def redistribute_workload(self, attributes_df: pd.DataFrame) -> pd.DataFrame:
        attributes = attributes_df.iloc[0].to_dict()
        # Direct changes - IMPROVED BATTERY IMPACT
        cpu_reduction = random.randint(10, 20)
        power_reduction = random.randint(8, 15)
        component_health_boost = random.randint(5, 10)
        
        # Apply primary changes
        attributes['CPU_GPU_Usage'] = max(5, attributes['CPU_GPU_Usage'] - cpu_reduction)
        attributes['Power_Consumption_Rate'] = max(5, attributes['Power_Consumption_Rate'] - power_reduction)
        attributes['Component_Health'] = min(100, attributes['Component_Health'] + component_health_boost)
        
        # Apply secondary effects - Better power management
        attributes['Battery_Level'] = min(100, attributes['Battery_Level'] + random.randint(5, 12))  # Increased from +2
        attributes['Temperature'] = max(0, attributes['Temperature'] - 3)  # Better heat distribution
        
        # Round values
        for key in attributes:
            attributes[key] = round(attributes[key], 2)
            
        return pd.DataFrame([attributes])

    def apply_fixes(self, data: pd.DataFrame, inputs: np.ndarray) -> pd.DataFrame:
        for i, (action_name, action_func) in zip(inputs[0], self.actions.items()):
            if i == 1:  # Execute only if the inputs value is 1
                print(f"Executing action: {action_name}")
                data = action_func(data)
        return data


# Example usage
if __name__ == "__main__":
    data = pd.DataFrame([{
        "Battery_Level": 90.0,
        "Battery_Health": 40.0,
        "Signal_Strength": 80.0,
        "Power_Consumption_Rate": 20.0,
        "Component_Health": 70.0,
        "CPU_GPU_Usage": 30.0,
        "Solar_Panel_Efficiency": 60.0,
        "Temperature": 25.0,
        "Data_Storage_Used": 21.27,
        "Debris_Risk_Level": 2.25
    }])
    inputs = np.array([[0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0]])
    fixes = Fixes()
    data = fixes.apply_fixes(data, inputs)
    print(data)