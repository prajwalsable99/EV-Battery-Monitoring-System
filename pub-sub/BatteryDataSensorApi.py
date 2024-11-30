import random
import json
import time
from datetime import datetime

# Define vehicle IDs
vehicle_ids = [i for i in range(1, 11)]




# Function to calculate power output
def calculate_power_output(voltage, current):
    return round((voltage * current) / 1000, 2)  # Convert to kW

# Function to generate correlated EV data
def generate_correlated_ev_data(vehicle_ids):
    data = []
    current_time = datetime.now().replace(second=0, microsecond=0)  # Minute-level timestamp
    
    for vehicle in vehicle_ids:
        soc = round(random.uniform(5, 100), 2)  # State of Charge (%)

        # Correlating voltage with SOC (higher SOC -> higher voltage)
        voltage = round(300 + (soc / 100) * 100, 2)  # Voltage increases with SOC (300V to 400V)

        # Correlating current based on SOC (lower SOC -> higher current if charging or in use)
        if soc < 20:
            current = round(random.uniform(100, 150), 2)  # High current for low SOC (charging or discharging)
        elif soc < 50:
            current = round(random.uniform(70, 100), 2)  # Moderate current for medium SOC
        else:
            current = round(random.uniform(50, 70), 2)  # Lower current for high SOC

        # Correlating temperature with current (higher current -> higher temperature)
        temperature = round(20 + (current / 150) * 25, 2)  # Temp between 20°C and 45°C

        # Power output is correlated directly with voltage and current
        power_output = calculate_power_output(voltage, current)

        # Create a dictionary for the current vehicle's data
        vehicle_data = {
            'timestamp': current_time.strftime("%Y-%m-%d %H:%M:%S"),
            'vehicleid': vehicle,
            'voltage': voltage,
            'current': current,
            'temperature': temperature,
            'stateofcharge': soc,
            'poweroutput': power_output
        }

        data.append(vehicle_data)

    return data





