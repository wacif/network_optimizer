import random

class NetworkSimulator:
    def __init__(self, num_devices=5):
        self.num_devices = num_devices
        self.devices = []

    def simulate_network_conditions(self):
        devices = []
        for device_id in range(1, self.num_devices + 1):
            devices.append({
                "device_id": f"Device_{device_id}",
                "bandwidth_usage": round(random.uniform(10, 100), 2),
                "latency": round(random.uniform(5, 50), 2),
                "packet_loss": round(random.uniform(0, 5), 2),
            })
        self.devices = devices
        return devices

    def get_simulation_stats(self):
        return self.devices
