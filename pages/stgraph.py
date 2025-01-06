import streamlit as st
import numpy as np
import pandas as pd

#text = 'Example content'
#st.download_button(label='Download text file', data=text, file_name='example.txt', mime='text/plain')
video_file = open("pgraph.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

#st.title("Stlite Sharing: Serverless Streamlit app platform")
st.header("Ploting the Graph")
col1, col2 = st.columns(2, vertical_alignment="center", gap="large")
with col1:
    st.write("Muhammad is the best")
    #st.image("data/logo.png", use_container_width=True)
with col2:
    st.write("Muhammad Fahim Aamir / 03336774947")
    #st.image("https://streamlit.io/images/brand/streamlit-mark-color.svg", use_container_width=True)




value = st.slider("Value?")
st.write("The slider value is", value)



@st.cache_data
def get_chart_data():
    return pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )

st.header("Chart sample")
#st.subheader("Chart sample")
chart_data = get_chart_data()

tab1, tab2, tab3 = st.tabs(["Line chart", "Area chart", "Bar chart"])
with tab1:
    st.line_chart(chart_data)
with tab2:
    st.area_chart(chart_data)
with tab3:
    st.bar_chart(chart_data)

st.subheader("Sample Data")


@st.cache_data
def get_sample_df():
    return pd.DataFrame(
        np.random.randn(50, 20),
        columns=('col %d' % i for i in range(20))
    )


df = get_sample_df()
st.dataframe(df)

#st.subheader("Camera input")
#st.info("Don't worry! The photo data is processed on your browser and never uploaded to any remote servers.")
#enable_camera_input = st.checkbox("Use the camera input")
#if enable_camera_input:
 #   picture = st.camera_input("Take a picture")

  #  if picture:
  #      st.image(picture)