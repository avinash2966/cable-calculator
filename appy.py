import streamlit as st
import math

def calculate_cable_size(load_power, voltage, power_factor, length, permissible_vd, derating_factor, ampacity):
    # Convert kW to W
    load_power_w = load_power * 1000
    
    # Calculate required current (I)
    current = load_power_w / (math.sqrt(3) * voltage * power_factor)
    
    # Voltage drop in volts
    vd_limit = (permissible_vd / 100) * voltage
    
    # Resistivity of copper (Ω.mm²/m)
    rho = 0.017  # For Copper (change to 0.028 for Aluminum)
    
    # Calculate minimum required cable size (S)
    cable_size = (2 * length * current * rho) / vd_limit
    
    # Calculate required ampacity considering derating factor
    required_ampacity = current / derating_factor
    
    # Check if selected cable meets the ampacity requirement
    if required_ampacity > ampacity:
        suggestion = "Increase cable size to meet ampacity requirements."
    else:
        suggestion = "Selected cable size is sufficient."
    
    return round(cable_size, 2), round(required_ampacity, 2), suggestion

# Streamlit UI
st.title("⚡ Power Cable Size Calculator")

load_power = st.number_input("Enter Load Power (kW):", value=500.0)
voltage = st.number_input("Enter Rated Voltage (V):", value=415.0)
power_factor = st.number_input("Enter Power Factor:", value=0.8)
length = st.number_input("Enter Cable Length (m):", value=500.0)
permissible_vd = st.number_input("Enter Permissible Voltage Drop (%):", value=2.0)
derating_factor = st.number_input("Enter Derating Factor:", value=0.65)
ampacity = st.number_input("Enter Cable Ampacity (A):", value=100.0)

if st.button("Calculate Cable Size"):
    cable_size, required_ampacity, suggestion = calculate_cable_size(
        load_power, voltage, power_factor, length, permissible_vd, derating_factor, ampacity
    )
    
    st.success(f"Required Cable Size: {cable_size} mm²")
    st.info(f"Required Ampacity: {required_ampacity} A")
    st.warning(suggestion)