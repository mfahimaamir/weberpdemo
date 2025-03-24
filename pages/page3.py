import streamlit as st
import pandas as pd
#video_file = open("video3.mp4", "rb")
#video_bytes = video_file.read()
#st.video(video_bytes)
#video_file = open("vide2.mp4", "rb")
#video_bytes = video_file.read()
#st.video(video_bytes)

global mfat
global uploaded_file
uploaded_file = st.file_uploader("upload FK file", type={"xlsx"})
#mfa = uploaded_file
#filename=uploaded_file.name

def myfunc():
    
    if uploaded_file is not None:
        st.header(mfat)
        mfa2 = pd.read_excel(uploaded_file, sheet_name=['ff1', 'Sheet1'])
        #st.session_state.df922 = pd.read_excel(uploaded_file, sheet_name=['ff1', 'Sheet1'])
        specific_sheet = mfa2['Sheet1']
        st.write(specific_sheet)
# Read Excel file with multiple sheets
#xls = pd.read_excel("D:\\SamNewLocation\\Desktop\\my_file.xlsx", sheet_name=['Sheet1', 'Sheet2'])

# Access individual sheets using sheet names
#sheet1_df = xls['Sheet1']
#sheet2_df = xls['Sheet2']

#print(sheet1_df)
#print(sheet2_df)

    else:
        st.warning("you need to upload a csv or excel file.")
        
with st.expander("Data view "): 
    st.header("Organization, finding and exportation of data")
    st.write(st.session_state.df)
with st.expander("Filter type 1"): 
    mfat =1
    myfunc()
    #st.write(st.session_state.df922)
with st.expander("Filter type 2"): 
    mfat =2
    myfunc()
    #st.write(st.session_state.df922)
with st.expander("Filter type 3"): 
    mfat =3
    myfunc()
    #st.write(st.session_state.df922)
    

#if you want to capture the file name of uploaded, you can write code like this:

