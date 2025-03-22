import pandas as pd
import streamlit as st
from st_aggrid import JsCode, AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode

def GetLastName(row):
    nsarr = row['orgHierarchy'].split('|')
    return(nsarr[len(nsarr)-1])

df=pd.DataFrame({ "orgHierarchy": ['Erica Rogers', 
                                   'Erica Rogers|Malcolm Barrett',
                                   'Erica Rogers|Malcolm Barrett|Esther Baker',
                                   'Erica Rogers|Malcolm Barrett|Esther Baker|Brittany Hanson',
                                   'Erica Rogers|Malcolm Barrett|Esther Baker|Brittany Hanson|Leah Flowers',
                                   'Erica Rogers|Malcolm Barrett|Esther Baker|Brittany Hanson|Tammy Sutton',
                                   'Erica Rogers|Malcolm Barrett|Esther Baker|Derek Paul',
                                   'Erica Rogers|Malcolm Barrett|Francis Strickland',
                                   'Erica Rogers|Malcolm Barrett|Francis Strickland|Morris Hanson',
                                   'Erica Rogers|Malcolm Barrett|Francis Strickland|Todd Tyler',
                                   'Erica Rogers|Malcolm Barrett|Francis Strickland|Bennie Wise',
                                   'Erica Rogers|Malcolm Barrett|Francis Strickland|Joel Cooper'],
                  "jobTitle": [ 'CEO', 'Exec. Vice President', 'Director of Operations', 'Fleet Coordinator', 'Parts Technician',
                                'Service Technician', 'Inventory Control', 'VP Sales', 'Sales Manager', 'Sales Executive',
                                'Sales Executive', 'Sales Executive' ], 
                  "employmentType": [ 'Permanent', 'Permanent', 'Permanent', 'Permanent', 'Contract', 'Contract', 'Permanent', 'Permanent',
                                      'Permanent', 'Contract', 'Contract', 'Permanent' ]}, 
)

df['Name'] = df.apply(lambda row: GetLastName(row), axis=1)
df.insert(0, "Name", df.pop("Name"))    # move col to 0 pstn

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_selection(selection_mode="single", use_checkbox=False)
gb.configure_column("orgHierarchy", hide = "True")
gb.configure_column("Name", hide = "True")
gridOptions = gb.build()

gridOptions["autoGroupColumnDef"]= {'cellRendererParams': {'checkbox': True }}
gridOptions["treeData"]=True
gridOptions["animateRows"]=True
gridOptions["groupDefaultExpanded"]= -1   # expand all
gridOptions["getDataPath"]=JsCode("function(data){ return data.orgHierarchy.split('|'); }").js_code

dta = AgGrid(df, gridOptions=gridOptions, height=350, allow_unsafe_jscode=True, enable_enterprise_modules=True,
             update_mode=GridUpdateMode.SELECTION_CHANGED)

st.write(dta['selected_rows'])