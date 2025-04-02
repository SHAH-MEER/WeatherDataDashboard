import streamlit as st
import plotly.express as px


st.title("Weather Data Dashboard")
place = st.text_input(label="Place:")

days = st.slider(label="Forecast Days",min_value=1,max_value=5,help="Select number of days to forecast")
option = st.selectbox(label="Select Data to view",options=("Temperature","Weather"))


st.subheader(f"{option} for the next {days} days in {place}")
date = ["2025-4-2","2025-4-3","2025-4-4"]
temperature = [23,27,31]
fig = px.line(x=date,y=temperature,labels={"x":"Date","y":"Temperature"})
st.plotly_chart(figure_or_data=fig)
