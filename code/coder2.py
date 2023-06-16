import streamlit as st
from PIL import Image
import json


hide_main_style= """
      <style>
      #MainMenu{visibility:hidden;}
      footer{visibility:hidden;}
      </style>
      """



img2=Image.open("ww.jpeg")
st.set_page_config(page_title="Insurance Company Portal",page_icon=img2, layout="wide")

st.markdown(
    """
    <h1 style="text-align: center;">Insurance Company Portal</h1>
    <p style="text-align: center;">Farmer's claim details </p>
    """,
    unsafe_allow_html=True
    )   



name=st.experimental_get_query_params().get("name",[""])[0]
farmerid = st.experimental_get_query_params().get("farmerid", ["105"])[0]
state=st.experimental_get_query_params().get("state",[""])[0]
district=st.experimental_get_query_params().get("district",[""])[0]
date=st.experimental_get_query_params().get("date",["2018-08-10"])[0]



st.write(name)
st.write(farmerid)
st.write(state)
st.write(district)
st.write(date)




with st.container():
    st.write("----")
    left_column, right_column= st.columns(2)
    with left_column:
        st.header("Details of the flooded region")
        st.write("##")
        st.write("")




import streamlit as st


button1_label = "Flood Statistics"
button1_url = "http://localhost:8081/mapstore/#/dashboard/33"
button2_label = "Flood Raster Layers"
button2_url = "http://localhost:8081/qgis2web_2023_06_16-19_10_44_886140/#9/9.4922/76.4962"


css_center = "display: flex; justify-content: center;"
css_button = "background-color: #FF5733; color: white; padding: 10px 20px; border: none; border-radius: 4px; font-size: 16px;"
css_margin = "margin-bottom: 20px;"  


button1 = f'<a href="{button1_url}" target="_blank"><button style="{css_button}">{button1_label}</button></a>'
button2 = f'<a href="{button2_url}" target="_blank"><button style="{css_button}">{button2_label}</button></a>'


st.markdown(f'<div style="{css_center}{css_margin}">{button1}</div>', unsafe_allow_html=True)
st.markdown(f'<div style="{css_center}">{button2}</div>', unsafe_allow_html=True)
