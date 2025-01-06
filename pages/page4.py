from st_aggrid import AgGrid
import pandas as pd
import streamlit as st
video_file = open("video3.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

#df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
AgGrid(st.session_state.df)