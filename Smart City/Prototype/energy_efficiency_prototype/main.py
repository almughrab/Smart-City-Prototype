from energy_management import EnergyManagement
from dashboard import DashboardApp

def main():
    energy_management = EnergyManagement()
    dashboard_app = DashboardApp(energy_management)
    dashboard_app.run()

if __name__ == "__main__":
    main()
