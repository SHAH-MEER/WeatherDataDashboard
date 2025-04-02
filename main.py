import streamlit as st
import plotly.express as px
from backend import get_data


#Add title, Text_Input box, Slider and selectbox
st.title("Weather Data Dashboard")
place = st.text_input(label="Place:")
days = st.slider(label="Forecast Days",min_value=1,max_value=5,help="Select number of days to forecast")
option = st.selectbox(label="Select Data to view",options=("Temperature","Weather"))

#Get weather Data
if place:
    try:
        filtered_data = get_data(place,days)


        st.subheader(f"{option} for the next {days} days in {place}")

        if option == "Temperature":
            #Plot the graph on Temperature data
            temperature = [dict["main"]["temp"] for dict in filtered_data]
            temperature = [temp / 10 for temp in temperature]
            dates = [dict["dt_txt"] for dict in filtered_data]
            fig = px.line(x=dates,y=temperature,labels={"x":"Date","y":"Temperature (C)"})
            st.plotly_chart(figure_or_data=fig)
        else:
            images = {"Clouds":"images/cloud.png",
                      "Clear":"images/clear.png",
                      "Rain":"images/rain.png",
                      "Snow":"images/snow.png"}
            weather = filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
            paths = [images[condition] for condition in weather]
            st.image(paths,width=130)
    except:
        st.info("Please Ensure that that name and spelling of 'Place' correct",)