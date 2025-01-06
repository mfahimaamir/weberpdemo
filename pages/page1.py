import streamlit as st
import streamlit.components.v1 as components
from pivottablejs import pivot_ui
st.header("Drag and Drop Pivot Table with selected data export to Excel")
t = pivot_ui(st.session_state.df)
with open(t.src) as t:
    components.html(t.read(), width=900, height=1000, scrolling=True)