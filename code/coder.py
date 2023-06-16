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
st.set_page_config(page_title="CROP INSURANCE",page_icon=img2, layout="wide")



st.markdown(
    """
    <h1 style="text-align: center; min-width: 400px; margin: 0 auto;">
    CROP INSURANCE CLAIM PORTAL
    </h1>

    <p style="text-align: center;">Farmer's portal for reporting crop damage due to flood</p>
    """,
    unsafe_allow_html=True
)



st.markdown(hide_main_style, unsafe_allow_html=True)
col1, col2, col3, col4, col5, col6, col7, col8= st.columns([1, 1, 1, 1, 3, 1, 1, 1])  # Adjust column widths as needed
with col1:
    st.write("")
with col2:
     st.write("")
with col3:
    st.write("")
with col4:
    st.write("")
with col5:
    st.image("agri2.gif", use_column_width=False)
with col6:
    st.write("")
with col7:
    st.write("")
with col8:
    st.write("")






st.markdown(hide_main_style,unsafe_allow_html=True)
img1=Image.open("img.jpg")
st.image(img1)
    





with st.container():
    st.write("----")
    left_column, right_column= st.columns(2)
    with left_column:
        st.header("What we do?")
        st.write("##")
        st.write(
            """
            Crop Insurance portal to enable the digitization of notification of areas, crops, schemes for enabling information access to multiple stakeholders thereby facilitating ease of access to the farmers in availing crop insurance services.
            """
        )







with st.container():
    st.write("----")
    name=st.text_input('Name')
    farmerid= st.number_input('Farmer Insurance Id')
    state= st.selectbox("Select the State",['Nil','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'])
    district= st.selectbox("Select the District",['Nil','Alappuzha','Ernakulam','Idukki','Kannur','Kasargod','Kollam','Kottayam','Kozhikode','Malappuram','Palakkad','Pathanamthitta','Thiruvananthapuram','Thrissur','Wayanad'])
    taluka= st.selectbox("Select the Taluk",['Nil','Cherthala','Ambalappuzha','Kuttanad','Karthikappally','Chengannur','Mavelikkara'])
    date=st.date_input("Date of crop damage")






with st.container():
    st.write("----")
    st.write("PREVIEW OF DETAILS")
    st.write(name)
    st.write(farmerid)
    st.write(state)
    st.write(district)
    st.write(date)





    
file = st.file_uploader("Upload the images of damaged crop fields", type=["jpg", "jpeg", "png"])

if file is not None: 
    image = Image.open(file)
    st.image(image, caption='Uploaded Image')



    

button_label = "Submit"
url = f"http://localhost:8502?name={name}&age={farmerid}&state={state}&district={district}&date{date}"

css_center = "display: flex; justify-content: center;"
css_button = "background-color: #FF5733; color: white; padding: 10px 20px; border: none; border-radius: 4px; font-size: 16px;"


button = f'<a href="{url}" target="_blank"><button style="{css_button}">{button_label}</button></a>'


st.markdown(f'<div style="{css_center}">{button}</div>', unsafe_allow_html=True)



























