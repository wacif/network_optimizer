import os
import random
import time
import numpy as np
import streamlit as st
from openai import OpenAI

# =========================
# Configuration
# =========================
API_KEY = os.getenv('AIML_API_KEY')  # Make sure this is correctly set
BASE_URL = "https://api.aimlapi.com"

# Set up the OpenAI client
client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

# =========================
# Function to simulate network conditions
# =========================
def simulate_network_conditions(num_devices=5):
    devices = []
    for device_id in range(1, num_devices + 1):
        devices.append({
            "device_id": f"Device_{device_id}",
            "bandwidth_usage": round(random.uniform(10, 100), 2),
            "latency": round(random.uniform(5, 50), 2),
            "packet_loss": round(random.uniform(0, 5), 2),
        })
    return devices

# =========================
# Normalize network stats for fair comparison
# =========================
def normalize_stats(devices):
    bandwidth = [device['bandwidth_usage'] for device in devices]
    latency = [device['latency'] for device in devices]
    packet_loss = [device['packet_loss'] for device in devices]

    # Normalize the data
    normalized_bandwidth = np.interp(bandwidth, (min(bandwidth), max(bandwidth)), (0, 1))
    normalized_latency = np.interp(latency, (min(latency), max(latency)), (0, 1))
    normalized_packet_loss = np.interp(packet_loss, (min(packet_loss), max(packet_loss)), (0, 1))

    for i, device in enumerate(devices):
        device['normalized_bandwidth'] = normalized_bandwidth[i]
        device['normalized_latency'] = normalized_latency[i]
        device['normalized_packet_loss'] = normalized_packet_loss[i]

    return devices

# =========================
# AI-driven optimization logic
# =========================
def optimize_network(devices):
    normalized_devices = normalize_stats(devices)

    # Format the message for the API
    formatted_devices = ", ".join([f"Device ID: {device['device_id']}, Bandwidth: {device['normalized_bandwidth']}, "
                                   f"Latency: {device['normalized_latency']}, Packet Loss: {device['normalized_packet_loss']}"
                                   for device in normalized_devices])

    # Call the AI model
    try:
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct-Turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a network optimization AI. You are tasked with optimizing device performance by reducing latency and packet loss while balancing bandwidth usage."
                },
                {
                    "role": "user",
                    "content": f"Here is the current network state: {formatted_devices}. Suggest optimized values."
                },
            ],
        )
        # Debug: Display raw API response
        st.write("API Response (Raw):", response)

        # Extract the content of the first choice
        optimized_response = response.choices[0].message.content
        return optimized_response
    except Exception as e:
        # Display detailed error message in Streamlit
        st.error(f"API call failed: {str(e)}")
        return None

# =========================
# Apply dynamic weights to prioritize optimization
# =========================
def apply_optimization_weights(devices, bandwidth_weight=0.2, latency_weight=0.4, packet_loss_weight=0.4):
    for device in devices:
        device['optimization_score'] = (
            (1 - device['normalized_bandwidth']) * bandwidth_weight +
            (1 - device['normalized_latency']) * latency_weight +
            (1 - device['normalized_packet_loss']) * packet_loss_weight
        )
    # Sort devices by their optimization score (higher score = better optimization priority)
    devices.sort(key=lambda x: x['optimization_score'], reverse=True)
    return devices

# =========================
# Streamlit UI: Main Application
# =========================
def main():
    st.title("AI-Driven Network Optimization")

    # Sidebar for configuration options
    st.sidebar.header("Configuration")
    num_devices = st.sidebar.slider("Number of Devices", min_value=1, max_value=10, value=5, step=1)
    bandwidth_weight = st.sidebar.slider("Bandwidth Weight", min_value=0.0, max_value=1.0, value=0.2, step=0.1)
    latency_weight = st.sidebar.slider("Latency Weight", min_value=0.0, max_value=1.0, value=0.4, step=0.1)
    packet_loss_weight = st.sidebar.slider("Packet Loss Weight", min_value=0.0, max_value=1.0, value=0.4, step=0.1)

    # Simulate and display initial network conditions
    if st.button("Simulate Network"):
        with st.spinner("Simulating network..."):
            time.sleep(2)  # Simulate processing delay
            devices = simulate_network_conditions(num_devices)
            st.subheader("Initial Network Stats")
            st.write(devices)

            # Normalize and apply optimization weights
            devices = normalize_stats(devices)
            devices = apply_optimization_weights(devices, bandwidth_weight, latency_weight, packet_loss_weight)

            st.subheader("Devices After Applying Optimization Weights")
            st.write(devices)

            # Store devices in session state
            st.session_state.devices = devices

    # Button to trigger AI optimization
    if "devices" in st.session_state:
        if st.button("Run AI-Driven Optimization"):
            with st.spinner("Running AI optimization..."):
                devices = st.session_state.devices
                optimized_results = optimize_network(devices)

                if optimized_results:
                    st.subheader("Optimized Network Stats (After AI)")
                    st.text(optimized_results)  # Display the AI's response
                else:
                    st.error("Optimization failed. Please check the API key or try again later.")

if __name__ == "__main__":
    main()
