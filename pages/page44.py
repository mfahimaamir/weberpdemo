from st_aggrid import AgGrid
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
import pandas as pd
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from pivottablejs import pivot_ui

# Load your dataset
#st.write("Muhammad is THe Best ")

# Configure grid options

with st.expander("Filter type 1"): 
    url12 = "https://docs.google.com/spreadsheets/d/1eUFk3UyL1663rv6SrGD43IoNnwULg1yW/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true"
    file_id122 = url12.split("/")[-2]
    path1122 = "https://drive.google.com/uc?export=download&id=" + file_id122
            #sce = pd.read_excel(path1)
    st.session_state.df922 = pd.read_excel(path1122)
    df3= st.session_state.df922
  
        #df = pd.read_json("https://www.ag-grid.com/example-assets/olympic-winners.json")
    gb = GridOptionsBuilder.from_dataframe(df3)
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
        df3,
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
            
            
    

with st.expander("Filter type 2"): 
    url12 = "https://docs.google.com/spreadsheets/d/1eUFk3UyL1663rv6SrGD43IoNnwULg1yW/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true"
    file_id122 = url12.split("/")[-2]
    path1122 = "https://drive.google.com/uc?export=download&id=" + file_id122
            #sce = pd.read_excel(path1)
    st.session_state.df922 = pd.read_excel(path1122)
    df3= st.session_state.df922
    
    
    #df = pd.read_json("https://www.ag-grid.com/example-assets/olympic-winners.json")
    
    #video_file = open("video3.mp4", "rb")
    #video_bytes = video_file.read()
    #st.video(video_bytes)
    st.header("Data filtration and exportation")
    ##df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
    #AgGrid(st.session_state.df,data_return_mode = 'FILTERED',enable_enterprise_modules=True,




    data = df3


    #@st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv(index=False).encode('utf-8')


    df = pd.DataFrame(data)


    gb = GridOptionsBuilder()
    gb.configure_default_column(
            alwaysShowHorizontalScroll = True,
            alwaysShowVerticalScroll= False,
            filter = True,
            groupable=True,
            enableCellTextSelection=True,
            rowHeight=100,
            #wrapText=wrap_text,
            #autoHeight=auto_height,
            wrapText=True,
            autoHeight=True,
            enableRangeSelection=True,
            
            
        )

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
    gb.configure_selection(selection_mode="multiple", use_checkbox=True)
    gb.configure_side_bar()
    gridoptions = gb.build()

    response = AgGrid(
        df,
        height=200,
        gridOptions=gridoptions,
        enable_enterprise_modules=True,
        update_mode=GridUpdateMode.MODEL_CHANGED,
        data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
        fit_columns_on_grid_load=False,
        header_checkbox_selection_filtered_only=True,
        use_checkbox=True)





    # st.write(type(response))
    # st.write(response.keys())

    v = response['selected_rows']
    if v:
        st.write('Selected rows')
        st.dataframe(v)
        dfs = pd.DataFrame(v)
        csv = convert_df(dfs)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='selected.csv',
            mime='text/csv',
        )
with st.expander("Filter type 3"): 
    

    data = {
        'Region': ['North America', 'North America', 'Europe', 'Oceania',
                'North America', 'North America', 'Europe', 'Oceania',
                'North America', 'North America', 'Europe', 'Oceania'],
        'Country': ['USA', 'Canada', 'UK', 'Australia',
                    'USA', 'Canada', 'UK', 'Australia',
                    'USA', 'Canada', 'UK', 'Australia'],
        'City': ['New York', 'Toronto', 'London', 'Sydney',
                'New York', 'Toronto', 'London', 'Sydney',
                'New York', 'Toronto', 'London', 'Sydney'],
        'District': ['Manhattan', 'Downtown', 'Westminster', 'CBD',
                    'Brooklyn', 'Midtown', 'Kensington', 'Circular Quay',
                    'Queens', 'Uptown', 'Camden', 'Bondi']
    }

    #df = pd.DataFrame({'Name': ['A', 'B', 'C'], 'Age': [25, 24, 1]})
    df = pd.DataFrame(data)

    #if "names_active" not in st.session_state:
        #st.session_state["names_active"] = list(df['Name'])
    #   st.session_state["names_active"] = list(df['Region'])
        
    #st.markdown(st.session_state["names_active"])

    return_df = AgGrid(data = df, data_return_mode = 'FILTERED')
    #st.session_state["names_active"] = list(return_df['data']['Name'])
    #st.session_state["names_active"] = list(return_df['data']['Region'])

    #st.markdown(st.session_state["names_active"])


