import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversions = {
        ("meters", "kilometers"): 0.001,
        ("kilometers", "meters"): 1000,
        ("grams", "kilograms"): 0.001,
        ("kilograms", "grams"): 1000,
    }
    return value * conversions.get((unit_from, unit_to), "Unsupported conversion")

st.title("Unit Converter")

value = st.number_input("Enter value:", min_value=1.0, step=1.0)
unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted Value: {result}")
