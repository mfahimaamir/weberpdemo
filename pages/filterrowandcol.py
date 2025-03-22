import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode

# Load your dataset
df = pd.read_json("https://www.ag-grid.com/example-assets/olympic-winners.json")

# Configure grid options
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(
    groupable=True,
    value=True,
    enableRowGroup=True,
    aggFunc='sum'
)

# Customize specific column behaviors
gb.configure_column('country', header_name="Home Country")
gb.configure_pagination(enabled=True, paginationPageSize=5)
gb.configure_selection(selection_mode="multiple", use_checkbox=True)
gb.configure_side_bar(filters_panel=True, defaultToolPanel='filters')

# Build the final option object
grid_options = gb.build()

# Render AgGrid
mfatt = AgGrid(
    df,
    gridOptions=grid_options,
    height=400,
    width='100%',
    allow_unsafe_jscode=True,
        
#    gridOptions=gridoptions,
    enable_enterprise_modules=True,
    update_mode=GridUpdateMode.MODEL_CHANGED,
    data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
    fit_columns_on_grid_load=False,
    header_checkbox_selection_filtered_only=True,
    use_checkbox=True)
    


st.markdown("### All Possible builder options")
for p in dir(GridOptionsBuilder):
    if not p.startswith("_"):
        _ = gb.__getattribute__(p)
        #st.write(_)
        
        
cap_button = st.button("Start Capturing") # Give button a variable name
if cap_button: # Make button a condition.
    st.write("muhammad is the best")
    #st.write(mfatt['selected_rows'])
    #st.write(mfatt['data'])
    #st.datagrame(mfatt("data"))
    ###https://docs.google.com/spreadsheets/d/1vu-5QOoLpir98duhVuumD0ABr_kZCww2/edit?usp=sharing&ouid=106062244503517417798&rtpof=true&sd=true
    #https://docs.google.com/spreadsheets/d/10QnGoTTz3ZsgxiTliIbJ8yk36s1BUu7WlDi9kZhMQS0/edit?usp=sharing
    #https://docs.google.com/spreadsheets/d/10QnGoTTz3ZsgxiTliIbJ8yk36s1BUu7WlDi9kZhMQS0/edit?gid=858585402#gid=858585402
    
    #https://docs.google.com/spreadsheets/d/10uBt4S7CRmfTV4vEGniqPA0igXz9Ywti/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true
    #https://docs.google.com/spreadsheets/d/10QnGoTTz3ZsgxiTliIbJ8yk36s1BUu7WlDi9kZhMQS0/edit?usp=sharing
    url1 = "https://docs.google.com/spreadsheets/d/10QnGoTTz3ZsgxiTliIbJ8yk36s1BUu7WlDi9kZhMQS0/edit?usp=sharing"
    file_id12 = url1.split("/")[-2]
    path112 = "https://drive.google.com/uc?export=download&id=" + file_id12
    #sce = pd.read_excel(path1)
    st.session_state.df92 = pd.read_excel(path112)
    st.write(st.session_state.df92 )
    data = st.session_state.df92
#    data3 = data.pivot_table(index='Country', columns='City', values='salary')
 #   st.write(data3)