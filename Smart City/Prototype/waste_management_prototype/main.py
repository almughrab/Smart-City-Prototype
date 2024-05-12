# main.py
from strategy.landfill_strategy import LandfillStrategy
from context.waste_management_system import WasteManagementSystem
from dashboard import Dashboard

def main():
    landfill_strategy = LandfillStrategy()
    waste_management_system = WasteManagementSystem(landfill_strategy)
    dashboard = Dashboard()

    # Simulate data collection from sensors
    sensor_data = {"Waste Composition": "Mixed waste", "Weather Forecast": "Sunny"}
    dashboard.display_sensor_data(sensor_data)

    # Simulate waste disposal
    waste_management_system.dispose_waste(sensor_data)

    # Display selected strategy
    dashboard.display_strategy(landfill_strategy.__class__.__name__)

    # Run the dashboard application
    dashboard.run()

if __name__ == "__main__":
    main()
