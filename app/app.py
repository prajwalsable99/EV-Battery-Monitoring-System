# import modules
import streamlit as st
import joblib

import sklean


#App data starts here
st.set_page_config(page_title="EV BATTERY QUALITY CHECKER", page_icon="https://www.how2shout.com/wp-content/uploads/2020/05/1540471342tech-mahindra-high-resolution-logo.jpg", layout="wide")


@st.cache_data  # 👈 Add the caching decorator
def load_data():  
    return []
data=load_data()

scalar=joblib.load('scalar.pkl')
model=joblib.load('rfc_model.pkl')






with st.sidebar:
 
    st.image(
        "https://www.how2shout.com/wp-content/uploads/2020/05/1540471342tech-mahindra-high-resolution-logo.jpg",width=150
        
    )
    st.divider()
    # st.write("Project By")
    # st.markdown("/)

    # st.divider()
# ------------------------------------------------------------------------------
# Title
st.title("EV BATTERY QUALITY CHECKER")
st.divider()




st.header("Predict Battery Quality")
# State_of_Charge (%)    50
# Cycle_Count             0
# Temperature (°C)       50
# Voltage (V)            50
# Current (A)            50
# Health_Status 

# State_of_Charge (%) 10.06  99.91
# Cycle_Count         104    6843
# Temperature (°C)    15.11  162.11
# Voltage (V)         2.53   4.49
# Current (A)         1.0    29.96
# Health_Status      

c1,c2=st.columns([1,2] , vertical_alignment='center',gap='large')

with c1 :
    st.image('https://cdn.inc42.com/wp-content/uploads/2022/09/ev-battery-ft-760x570.png')
with c2:

    soc = st.slider("State_of_Charge (%)", 10, 100)
    cyclecount = st.slider("Cycle_Count  ", 100, 2000)
    tempearture= st.slider(" Temperature (°C) ", 15, 150)
    voltage = st.slider("Voltage (V) ", 2, 5)
    current = st.slider("Current (A)   ", 1, 30)


    if st.button("Check"):
        x= scalar.transform([[soc,cyclecount,tempearture,voltage,current]])
        y= model.predict(x) [0]
        st.write("Battery Condition : ", y)
        pass

# # ----------------------------------



