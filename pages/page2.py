import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet
#video_file = open("vide2.mp4", "rb")
#video_bytes = video_file.read()
#st.video(video_bytes)
video_file = open("video3.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

st.header("Data Filtering and Graphical Representation")
new_dfs, code = spreadsheet (st.session_state.df)
#st.write(new_dfs)
#st.code(code)