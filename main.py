import argparse
from network_simulator import NetworkSimulator
from optimizer import NetworkOptimizer
from utils import setup_logging

if __name__ == "__main__":
    # Setup logging
    logger = setup_logging('INFO')
    
    # Command-line argument parsing for dynamic device count
    parser = argparse.ArgumentParser(description='Network Optimization')
    parser.add_argument('--devices', type=int, default=5, help='Number of devices to simulate')
    args = parser.parse_args()
    
    # Step 1: Simulate network conditions
    logger.info("Starting network simulation...")
    simulator = NetworkSimulator(num_devices=args.devices)
    devices = simulator.simulate_network_conditions()

    logger.info("Initial Simulation Stats (Before Optimization):")
    for device in devices:
        logger.info(f"{device['device_id']} - Bandwidth: {device['bandwidth_usage']} Mbps, Latency: {device['latency']} ms, Packet Loss: {device['packet_loss']}%")
    
    # Step 2: Optimize network using AI
    optimizer = NetworkOptimizer()
    optimized_stats = optimizer.optimize_network(devices)

    if optimized_stats:
        logger.info("Optimized Stats (After AI-Driven Optimization):")
        logger.info(optimized_stats)
    else:
        logger.error("Optimization failed.")
