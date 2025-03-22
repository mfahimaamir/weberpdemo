import streamlit as st 
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
import pandas as pd

df = pd.DataFrame({
        'group': [1,1,2,2],
        'x': [1,2,3,4],
        'y': [1,2,3,4],
    })

getDetailRowData = JsCode('''function(e) {
            let rowData = [
                { make: "Toyota", model: "Celica", price: 35000 },
                { make: "Ford", model: "Mondeo", price: 32000 },
                { make: "Porsche", model: "Boxter", price: 72000 }
                ];
            e.successCallback(rowData)
        };''')

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_columns('group', cellRenderer='agGroupCellRenderer')

go = gb.build()
go['masterDetail'] = True
go['detailCellRendererParams'] = {
    'detailGridOptions':{
        'columnDefs':[
            {'field':'make'},
            {'field':'model'},
            {'field':'price'}
        ]
    },
    'getDetailRowData': getDetailRowData
}

AgGrid(df, theme='streamlit', allow_unsafe_jscode=True, 
       gridOptions=go, enable_enterprise_modules=True
)