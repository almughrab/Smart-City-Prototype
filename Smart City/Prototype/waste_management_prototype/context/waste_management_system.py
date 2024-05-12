# context/waste_management_system.py
from strategy.waste_disposal_strategy import WasteDisposalStrategy

class WasteManagementSystem:
    def __init__(self, disposal_strategy: WasteDisposalStrategy):
        self.disposal_strategy = disposal_strategy

    def set_disposal_strategy(self, disposal_strategy: WasteDisposalStrategy):
        self.disposal_strategy = disposal_strategy

    def dispose_waste(self, waste_data):
        # Dynamically select disposal strategy based on input data and decision-making algorithms
        # Example: If environmental impact assessment indicates recycling is favorable, select recycling strategy
        self.disposal_strategy.dispose_waste(waste_data)
