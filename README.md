# Documentation for AI-Driven Network Optimization

## Overview

This application is designed to simulate network conditions and optimize device performance using an AI model. It employs Streamlit for the user interface, allowing users to adjust parameters, visualize initial and optimized network states, and see the effects of AI-driven optimizations.

## Dependencies

Before running the application, ensure that you have the following packages installed:

- `os`
- `random`
- `time`
- `numpy`
- `streamlit`
- `openai`

You can install the required libraries using pip:
```bash
pip install numpy streamlit openai
```

## Configuration

### Environment Variables

The application requires an API key for accessing the OpenAI model. Set the environment variable `AIML_API_KEY` with your OpenAI API key.

```bash
export AIML_API_KEY='your_api_key'
```

## Components

### 1. **Configuration Section**

```python
API_KEY = os.getenv('AIML_API_KEY')  # Make sure this is correctly set
BASE_URL = "https://api.aimlapi.com"

# Set up the OpenAI client
client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)
```

- **API_KEY**: Retrieves the OpenAI API key from environment variables.
- **BASE_URL**: Defines the base URL for the OpenAI API.
- **client**: Initializes the OpenAI client with the provided API key and base URL.

### 2. **Network Simulation Functions**

#### `simulate_network_conditions(num_devices=5)`

Simulates network conditions for a specified number of devices.

- **Parameters**:
  - `num_devices` (int): The number of devices to simulate (default is 5).
  
- **Returns**: A list of dictionaries, each representing a device with random `bandwidth_usage`, `latency`, and `packet_loss`.

#### Example:
```python
devices = simulate_network_conditions(5)
```

### 3. **Normalization Function**

#### `normalize_stats(devices)`

Normalizes the network statistics of the devices for fair comparison.

- **Parameters**:
  - `devices` (list): A list of devices with their respective statistics.

- **Returns**: The input list of devices augmented with normalized values for `bandwidth`, `latency`, and `packet_loss`.

#### Example:
```python
normalized_devices = normalize_stats(devices)
```

### 4. **AI Optimization Function**

#### `optimize_network(devices)`

Sends the current network state to the AI model and retrieves optimized values.

- **Parameters**:
  - `devices` (list): A list of devices with their normalized statistics.

- **Returns**: The raw response from the AI, suggesting optimized values.

#### Example:
```python
optimized_results = optimize_network(devices)
```

### 5. **Optimization Weight Application Function**

#### `apply_optimization_weights(devices, bandwidth_weight=0.2, latency_weight=0.4, packet_loss_weight=0.4)`

Calculates optimization scores for each device based on given weights and sorts them for prioritization.

- **Parameters**:
  - `devices` (list): A list of devices.
  - `bandwidth_weight` (float): Weight for bandwidth (default is 0.2).
  - `latency_weight` (float): Weight for latency (default is 0.4).
  - `packet_loss_weight` (float): Weight for packet loss (default is 0.4).
  
- **Returns**: The input list of devices, sorted by their optimization scores.

#### Example:
```python
devices = apply_optimization_weights(devices)
```

### 6. **Main Streamlit Application**

#### `main()`

The main function that initializes the Streamlit application, handles user input, and triggers simulations and AI optimizations.

- **Functionality**:
  - Displays the title and sidebar for configuration options.
  - Simulates network conditions and normalizes statistics.
  - Applies optimization weights and displays results.
  - Allows users to run AI-driven optimization and view results.

#### Example Usage:
```python
if __name__ == "__main__":
    main()
```

## How to Run the Application

1. Ensure you have Python and the necessary packages installed.
2. Set the OpenAI API key in your environment variables.
3. Run the Streamlit application from the terminal:
   ```bash
   streamlit run your_script_name.py
   ```
4. Interact with the UI to simulate network conditions, adjust optimization weights, and run the AI optimization.

## User Interface

### Sidebar Configuration Options
- **Number of Devices**: Adjust the slider to choose the number of devices to simulate (1-10).
- **Weights**: Set the importance of each metric (bandwidth, latency, packet loss) using sliders (0.0 to 1.0).

### Main Area
- **Simulate Network**: Button to simulate network conditions.
- **Initial Network Stats**: Displays the simulated network conditions for the devices.
- **Optimized Network Stats**: Displays the results of the AI optimization.

## Error Handling

The application includes error handling for:
- API call failures (displays error messages in the Streamlit app).
- Invalid responses from the API (ensures that the application does not crash).

## Conclusion

This application provides an interactive way to simulate and optimize network conditions using AI. Users can easily adjust parameters and visualize the impact of AI optimizations on network performance.

--- 

