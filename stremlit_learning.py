import streamlit as st

st.title("Simple Calculator")

# User inputs
number1 = st.number_input("Enter first number", value=0.0)
number2 = st.number_input("Enter second number", value=0.0)

operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform calculation
if operation == "Add":
    result = number1 + number2
elif operation == "Subtract":
    result = number1 - number2
elif operation == "Multiply":
    result = number1 * number2
elif operation == "Divide":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error: Division by zero"

st.write(f"Result: {result}")
