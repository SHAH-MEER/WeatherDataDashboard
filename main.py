import streamlit as st
import plotly as px


st.title("Weather Data Dashboard")
place = st.text_input(label="Place:")
days = st.slider(label="Forecast Days",min_value=1,max_value=5,help="Select number of days to forecast")
option = st.selectbox(label="Select Data to view",options=("Temperature","Weather"))
st.subheader(f"{option} for the next {days} days in {place}")
