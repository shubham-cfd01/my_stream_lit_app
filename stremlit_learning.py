import streamlit as st

st.title("Battery Calculator")

# User inputs
st.subheader("Battery Energy Calculation")
capacity = st.number_input("Enter Battery Capacity (Ah)", value=0.0)
nom_v = st.number_input("Enter Nominal voltage (V)", value=0.0)
power = capacity*nom_v/1000
st.write(f"Total Energy of the Battery is: {power}W")
