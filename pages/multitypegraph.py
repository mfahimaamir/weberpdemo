import altair as alt
from vega_datasets import data
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
from openpyxl import Workbook
import numpy as np
import plotly as py
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode


datammmm = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
  "duration3": [50, 40, 45]
}


def read_data():
    df = pd.DataFrame( 
                     
       {
  "Data1": np.random.randint(19,85 ,size=10),
  "data2": np.random.randint(19,85 ,size=10),
  "data3": np.random.randint(19,85 ,size=10)
}               
                     
                      
      )
    return df



#data = ( "Apples" : np.random.randint(19,05 ,size=10), 
 #       "Bears" : np.random.randint(19,05 ,size=10),  
  #      "Cates" : np.random.randint(19,05 ,size=10)   
                       
   #                    )
        
chart_data = read_data()


editor_df = st.data_editor(chart_data
   # chart_data, key="airport_edit", num_rows="dynamic", use_container_width=True
)

st.line_chart(chart_data)
st.bar_chart(chart_data)
st.altair_chart(chart_data)
#st.bar_chart(source, x="variety", y="yield", color="site", horizontal=True)
#st.bar_chart(source, x="year", y="yield", color="site", stack=False)


col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    st.line_chart(chart_data)
    #st.pie_chart(chart_data)
#    st.header("A cat")
 #   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.bar_chart(chart_data)
    #st.header("A dog")
    #st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
    st.area_chart(chart_data)
    #st.header("An owl")
    #st.image("https://static.streamlit.io/examples/owl.jpg")
with col4:
    st.scatter_chart(chart_data)
    #st.header("An owl")
    #st.image("https://static.streamlit.io/examples/owl.jpg")
with col5:
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)
 
 #   st.map(chart_data)
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg")
    
    
    
    
    

source = data.cars()
#.mark_bar()
#_circle
chart = alt.Chart(source).mark_bar().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()


chart2 = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()


tab1, tab2, tab3, tab4 = st.tabs(["Streamlit theme (default)", "Altair native theme","Pie Graph","Pie Graph-2"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(chart2, theme=None, use_container_width=True)
with tab3:

    data = {
    'ctry': ['USA', 'PHI', 'CHN'],
    'gold': [12, 1, 20,],
    'silver': [4,4, 12],
    'bronze': [8, 2, 30],
    'sum': [24, 7, 62]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)

    cols = st.columns([1, 1])

    with cols[0]:
        medal_type = st.selectbox('Medal Type', ['gold', 'silver', 'bronze'])
    
        fig = px.pie(df, values=medal_type, names='ctry',
                 title=f'number of {medal_type} medals',
                 height=300, width=200)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=0),)
        st.plotly_chart(fig, use_container_width=True)

    with cols[1]:
        st.text_input('sunburst', label_visibility='hidden', disabled=True)
        fig = px.sunburst(df, path=['ctry', 'gold', 'silver', 'bronze'],
                      values='sum', height=300, width=200)
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=0),)
        st.plotly_chart(fig, use_container_width=True)
        
with tab4:
 #       #simester,course
        st.session_state.df
  #      labels = st.session_state.df['SIMESTER'].value_counts().index
   #     values = st.session_state.df['SIMESTER'].value_counts().values
    #    trace = go.Pie(labels=labels, values=values)
     #   st.plot([trace], filename='basic_pie_chart')