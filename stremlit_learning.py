import streamlit as st
import matplotlib.pyplot as plt
def CalculateEnergy (capacity,voltage):
    return capacity*voltage/1000
def CalculateSOC(instant_cap,total_cap):
    return round (instant_cap/total_cap*100,3)
def CalculateSOH(current_total_cap,intial_total_cap):
    return round (current_total_cap/intial_total_cap*100,3)

st.title("Battery Calculator")
option = st.sidebar.selectbox("Select Calculation", ("Calculate Energy", "Build Pack From Cells", "Calculate SOC", "Calculate SOH"))
# User inputs
if option == "Calculate Energy":
    st.subheader("Battery Energy Calculation")
    capacity = st.number_input("Enter Battery Capacity (Ah)", value=0.0)
    nom_v = st.number_input("Enter Nominal Voltage (V)", value=0.0)
    power = CalculateEnergy(capacity,nom_v)
    st.write(f"Total Energy of the Battery is: {power} kWh")
    
elif option == "Calculate SOC":
    st.subheader("Battery SOC Calculation")
    instant_cap = st.number_input("Enter the Instant Battery Capacity (Ah)", value=0.1)
    total_cap = st.number_input("Enter Total Battery Capacity (Ah)", value=0.1)
    soc = CalculateSOC(instant_cap,total_cap)
    st.write(f"SOC is: {soc*100} %")
    
elif option == "Calculate SOH":
    st.subheader("Battery SOH calculation")
    instant_cap = st.number_input("Enter the Current Total Battery Capacity (Ah)", value=0.1)
    total_cap = st.number_input("Enter Intial Total Battery Capcity (Ah)", value=0.1)
    soh = CalculateSOH(instant_cap,total_cap)
    st.write(f"SOH is: {soh*100} %")

elif option == "Build Pack From Cells":
    st.subheader("Pack Builder")
    cell_in_series = st.number_input("Enter the Cell in Series", value=1)
    cell_in_parallel =st.number_input('Enter the Total Number of Cells in Parallel',value=1)
    cell_cap = st.number_input("Enter One Cell Capacity (Ah)", value=1)
    cell_nominal_voltage = st.number_input ("Enter the Nominal Voltage of the Cell (V)",value=3.6)
    pack_capacity = cell_in_parallel*cell_cap
    pack_nominal_voltage =cell_in_series*cell_nominal_voltage
    pack_enrgy = CalculateEnergy(pack_capacity,pack_nominal_voltage)
    st.write(f"Pack Capacity is: {pack_capacity} Ah")
    st.write(f"Pack Nominal Voltage is: {pack_nominal_voltage} V")
    st.write(f"Pack Total Enegy is {pack_enrgy} kWh")
    
else:
    st.header ('Code is under deblopment')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        