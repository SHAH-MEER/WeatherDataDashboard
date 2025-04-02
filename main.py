import streamlit as st
import plotly.express as px
from backend import get_data



st.title("Weather Data Dashboard")
place = st.text_input(label="Place:")

days = st.slider(label="Forecast Days",min_value=1,max_value=5,help="Select number of days to forecast")
option = st.selectbox(label="Select Data to view",options=("Temperature","Weather"))

data = get_data(place,days,option)

st.subheader(f"{option} for the next {days} days in {place}")

fig = px.line(x=date,y=temperature,labels={"x":"Date","y":"Temperature"})
st.plotly_chart(figure_or_data=fig)
