import streamlit as st


st.markdown("""
    <style>
        .title {
            font-size: 50px;
            font-weight: bold;
            color:rgb(68, 10, 70);  
            text-align: center;
        }
       
        .stSelectbox, .stNumberInput, .stButton {
            font-size: 18px;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
        }
        .stSelectbox {
            background-color:#EAA7EC; 
        }
        .stNumberInput {
            background-color: #EAA7EC;  
        }
        .stButton {
            background-color: #EAA7EC;  
            color: grey;
            border: none;
            cursor: pointer;
        }
        .stButton:hover {
            background-color: #c08fe0;  
        }
        .stSuccess {
            font-size: 24px;
            font-weight: bold;
            color: black;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown('<h1 class="title">QuickConvertApp ⚡️</h1>', unsafe_allow_html=True)

category = st.selectbox("Select the Category", ["Length", "Weight", "Time", "Volume", "Temperature"])

def unitConvertor(category, value, unit):
    if category == "Length":
        if unit == "kilometers to miles":
            return value * 0.621373
        elif unit == "miles to kilometers":
            return value / 0.621373
        
    elif category == "Weight":
        if unit == "kilograms to pounds":
            return value * 2.20462
        elif unit == "pounds to kilograms":
            return value / 2.20462
        
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "days to Hours":
            return value * 24
        
    elif category == "Volume":
        if unit == "liters to gallons":
            return value * 0.264172
        elif unit == "gallons to liters":
            return value / 0.264172
        
    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9

if category == "Length":
    unit = st.selectbox("Select Conversion Unit", ["kilometers to miles", "miles to kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select Conversion Unit", ["kilograms to pounds", "pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("Select Conversion Unit", ["Seconds to Minutes", "Minutes to hours", "Hours to days", "days to Hours"])
elif category == "Volume":
    unit = st.selectbox("Select Conversion Unit", ["liters to gallons", "gallons to liters"])
elif category == "Temperature":
    unit = st.selectbox("Select Conversion Unit", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])

value = st.number_input("Enter the value to convert", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = unitConvertor(category, value, unit)
    st.markdown(f'<h1 class="stSuccess">✅The conversion result is {result:.2f}</h1>', unsafe_allow_html=True)