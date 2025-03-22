import streamlit as st
import pandas as pd
import numpy as np
st.write("muhammad ")   # ok ok ok 
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(
        np.random.randn(12, 5), columns=["a", "b", "c", "d", "e"]
    )

event = st.dataframe(
    st.session_state.df,
    key="data",
    on_select="rerun",
    selection_mode=["single-row", "multi-column"],
)
#selection_mode=["multi-row", "multi-column"],
#df_selected = event.selection[0].value()

df_selected = st.session_state.df.loc[event.selection['rows']] # is give me error 
#df_selected = st.session_state.df.loc[event.selection['rows'],['columns']] # is give me error 
#df_selected = st.session_state.df.loc[event.selection['rows','columns']]  # is also give the error 
#f_selected = st.session_state.df.loc[event.selection['rows']]  # this run ok 
#df_selected = st.session_state.df.loc[event.selection['columns']] # this run ok 
st.write(df_selected)
selected_info = event['selection']
st.write(selected_info)
#df3 = pd.DataFrame(selected_info)
#st.write(event.selection.header)
st.write(event.selection["columns"])   # ok ok ok 
mfa1 =event.selection["columns"]   # ok ok ok 
ages = df_selected[mfa1]
st.write(ages)   # ok ok ok 
st.write("muhammad ")   # ok ok ok 
#selected_info(df.columns.values))
#print("Column headers from list(df):", list(df))
#print("Column headers from list(df.columns):", 
#      list(df.columns))

#@stdf.selection['columns'] ]  # is also give the error 