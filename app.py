import streamlit as st
import logging
from network_simulator import NetworkSimulator
from optimizer import call_optimization_model

# Configure logging
logging.basicConfig(level=logging.INFO)

# Title and description
st.title('AI-Driven Network Optimization')
st.write('Simulate network conditions and optimize using AI-powered solutions.')

# Dynamic input for device count
num_devices = st.number_input('Enter the number of devices:', min_value=1, max_value=100, value=5)

# Button to run the simulation
if st.button('Run Simulation'):
    st.write(f"Running network simulation with {num_devices} devices...")
    
    # Step 2: Create the network environment
    devices = NetworkSimulator.simulate_network_environment(num_devices)
    
    # Step 3: Initialize the network simulator
    network_simulator = NetworkSimulator(devices=devices)

    # Step 4: Run the simulation
    simulation_stats = network_simulator.run_simulation(duration=10)
    st.write("Initial Simulation Stats (Before Optimization):")
    for stat in simulation_stats:
        st.json(stat)

    # Call AI model for optimization suggestions
    try:
        model_response = call_optimization_model(simulation_stats)
        optimized_stats, improvements = network_simulator.optimize_network(model_response=model_response)
        
        # Display optimized results
        st.write("\nOptimized Stats (After AI-Driven Optimization):")
        for device in optimized_stats:
            st.json(device)

        st.write("\nImprovements Summary:")
        for device_id, improvement in improvements.items():
            st.write(f"Device {device_id}:")
            st.write(f"  Original Stats: {improvement['original']}")
            if "optimized_bandwidth" in improvement:
                st.write(f"  Optimized Bandwidth: {improvement['optimized_bandwidth']} (Reduced by 15%)")
            if "optimized_latency" in improvement:
                st.write(f"  Optimized Latency: {improvement['optimized_latency']} (Reduced by 10%)")
            if "optimized_packet_loss" in improvement:
                st.write(f"  Optimized Packet Loss: {improvement['optimized_packet_loss']} (Minimized by 20%)")

    except Exception as e:
        st.error(f"An error occurred during optimization: {str(e)}")
