satellite_actions = [
    {
        "Attribute(s) Affected": "Battery Level",
        "Action": "Disable non-essential systems",
        "Resource Group": "Power"
    },
    {
        "Attribute(s) Affected": "Battery Level, Power Usage",
        "Action": "Reroute power to core functions",
        "Resource Group": "Power"
    },
    {
        "Attribute(s) Affected": "Temperature",
        "Action": "Increase cooling system power",
        "Resource Group": "Thermal"
    },
    {
        "Attribute(s) Affected": "Temperature, Orientation",
        "Action": "Adjust orientation for passive cooling",
        "Resource Group": "Thermal, Position"
    },
    {
        "Attribute(s) Affected": "Solar Panel Alignment",
        "Action": "Adjust pitch, yaw, roll for sunlight absorption",
        "Resource Group": "Position"
    },
    {
        "Attribute(s) Affected": "Signal Strength",
        "Action": "Adjust antenna position or switch frequency",
        "Resource Group": "Communication"
    },
    {
        "Attribute(s) Affected": "Data Storage",
        "Action": "Optimize data transmission",
        "Resource Group": "Data"
    },
    {
        "Attribute(s) Affected": "Data Storage",
        "Action": "Delete unnecessary data",
        "Resource Group": "Data"
    },
    {
        "Attribute(s) Affected": "CPU/GPU Usage",
        "Action": "Redistribute workload, reduce power to affected components",
        "Resource Group": "Power, Compute"
    },
    {
        "Attribute(s) Affected": "Thruster Accuracy",
        "Action": "Run recalibration sequence, adjust power to thrusters",
        "Resource Group": "Propulsion"
    },
    {
        "Attribute(s) Affected": "Orbital Position",
        "Action": "Recalibrate position, tweak pitch, roll, yaw",
        "Resource Group": "Position"
    }
]

# Print the list to verify
for action in satellite_actions:
    print(action)