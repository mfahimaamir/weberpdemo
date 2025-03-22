import numpy as np
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
from collections import defaultdict
#from st_aggrid.shared import getAllColumnProps, getAllGridOptions
#from st_aggrid import getAllColumnProps, getAllGridOptions
from st_aggrid import AgGrid, GridOptionsBuilder



with st.expander("Pivot Table"): 

        
        url12 = "https://docs.google.com/spreadsheets/d/1TrljfQUEw2cEiYUOyXXfH7u0VF0IDARZ/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true"
        file_id122 = url12.split("/")[-2]
        path1122 = "https://drive.google.com/uc?export=download&id=" + file_id122
            #sce = pd.read_excel(path1)
        st.session_state.df922 = pd.read_excel(path1122)
        #st.write(st.session_state.df92 )
        #datag = st.session_state.df92




        @st.cache_data()
        def load_data():
            #data = pd.read_excel("C:/mfa/exportpv.xlsx")
            data = st.session_state.df922
            
            
            
            #data = pd.read_csv("./data.csv", parse_dates=["referenceDate"])
            #st.write(data)
            return data

        data = load_data()

        shouldDisplayPivoted = st.checkbox("Pivot data on Reference Date",True)

        gb = GridOptionsBuilder()

        gb.configure_default_column(
            resizable=True,
            filterable=True,
            sortable=True,
            editable=False,
        )
        gb.configure_column(
            field="State", header_name="State", width=80, rowGroup=shouldDisplayPivoted
        )

        gb.configure_column(
            field="PowerPlant",
            header_name="Power Plant",
            flex=1,
            tooltipField="powerPlant",
            rowGroup=True if shouldDisplayPivoted else False,
        )
        gb.configure_column(
            field="RecordType",
            header_name="Record Type",
            width=110,
            rowGroup=shouldDisplayPivoted,
        )

        gb.configure_column(
            field="Buyer",
            header_name="Buyer",
            width=150,
            tooltipField="buyer",
            rowGroup=shouldDisplayPivoted,
        )


        gb.configure_column(
            field="mfat",
            header_name="local/import",
            width=50,
            tooltipField="buyer",
            rowGroup=shouldDisplayPivoted,
            #pivot=True,
            #hide=True,
        #    type=["numericColumn"],
        )


        #field="dat32 ReferenceDate",
        gb.configure_column(
            field="dat32",
            header_name="Reference Date",
            width=100,
            valueFormatter="value != undefined ? new Date(value).toLocaleString('en-US', {dateStyle:'medium'}): ''",
            pivot=False,
        )
        #valueGetter="new Date(data.referenceDate).getFullYear()",

        gb.configure_column(
            field="mfat",
            header_name="local/import",
            width=50,
            tooltipField="localimport",
        #    rowGroup=shouldDisplayPivoted,
            pivot=True,
            hide=True,
        #    type=["numericColumn"],
        )

        gb.configure_column(
            field="VirtualYear",
            header_name="Reference Date Year",
            valueGetter="new Date(data.dat32).getFullYear()",
            pivot=True,
            hide=True,
        )
        #valueGetter="new Date(data.referenceDate).toLocaleDateString('en-US',options={year:'numeric', month:'2-digit'})",
        gb.configure_column(
            field="VirtualMonth",
            header_name="Reference Date Month",
            valueGetter="new Date(data.dat32).toLocaleDateString('en-US',options={year:'numeric', month:'2-digit'})",
            pivot=True,
            hide=True,
        )

        gb.configure_column(
            field="hoursInMonth",
            header_name="Hours in Month",
            width=50,
            type=["numericColumn"],
        )

        gb.configure_column(
            field="VolumeMWh",
            header_name="Volume [MWh]",
            width=100,
            type=["numericColumn"],
            aggFunc="sum",
            valueFormatter="value.toLocaleString()",
        )

        gb.configure_grid_options(
            tooltipShowDelay=0,
            pivotMode=shouldDisplayPivoted,
        )

        gb.configure_grid_options(
            autoGroupColumnDef=dict(
                minWidth=300, 
                pinned="left", 
                cellRendererParams=dict(suppressCount=True)
            )
        )
        go = gb.build()

        mfatt = AgGrid(data, gridOptions=go, height=400)


        filterbtm = st.button('Get filred data')
        if filterbtm:
            st.table(mfatt['data'])

    
with st.expander("Pivot with both side total / Grand and Subtotal"): 
    
        url12 = "https://docs.google.com/spreadsheets/d/1eUFk3UyL1663rv6SrGD43IoNnwULg1yW/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true"
        file_id122 = url12.split("/")[-2]
        path1122 = "https://drive.google.com/uc?export=download&id=" + file_id122
            #sce = pd.read_excel(path1)
        st.session_state.df922 = pd.read_excel(path1122)



        #df = pd.read_excel('c:/iqra/ff1.xlsx')
        df = st.session_state.df922
        dd=df

        table = pd.pivot_table(dd, index=['State'],columns = ['City'],values=['SalesToday'],\
                            aggfunc=np.sum, margins=True)
        st.write(table)



        table1 = pd.pivot_table(dd, index=['State'],columns = ['City'],values=['SalesToday', 'SalesMTD','SalesYTD'],\
                            aggfunc=np.sum, margins=True)
        st.write(table1)
        #st.write(table)




        #---------------------------
                #print(tab_tots)








    
with st.expander("Group by Tree"): 
    
    np.random.seed(0)

    #https://docs.google.com/spreadsheets/d/1y8JdrYbZkoH9DrcUMYRTWTVgW0DyE6s-/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true

    url123 = "https://docs.google.com/spreadsheets/d/1y8JdrYbZkoH9DrcUMYRTWTVgW0DyE6s-/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true"
    file_id1223 = url123.split("/")[-2]
    path11223 = "https://drive.google.com/uc?export=download&id=" + file_id1223
        #sce = pd.read_excel(path1)
    st.session_state.df9223 = pd.read_excel(path11223)


    #df = pd.read_excel("mfa1.xlsx"  )
    dfg = st.session_state.df9223 
    mfa = pd.concat([
            dfg.assign(
                **{x: 'Total' for x in 'abcdef'[i:]}
            ).groupby(list('abcdef')).sum() for i in range(7)
        ]).sort_index()

    st.write(mfa)
    #st.area_chart(mfa)

    mfa2 = pd.concat([
            dfg.assign(
                **{x: '' for x in 'abcdef'[i:]}
            ).groupby(list('abcdef')).sum() for i in range(1, 7)
        ]).sort_index()



    #sprint(mfa)
    st.write(mfa2)
    #st.bar_chart(mfa2)

with st.expander("Cross Tab Balance"): 
    # create a sample dataset
    df = pd.DataFrame({
        'gender': ['male', 'male', 'female', 'female', 'male', 'female', 'male', 'female'],
        'education_level': ['high school', 'college', 'college', 'graduate', 'high school', 'graduate', 'college', 'graduate'],
        'score': [75, 82, 88, 95, 69, 92, 78, 85]
    })

    st.write(df)
    # create a crosstab table of gender and education level
    ct = pd.crosstab(df['gender'], df['education_level'])

    ct_mean = pd.crosstab(df['gender'], df['education_level'], 
                        values=df['score'], aggfunc='sum')
    st.write(ct_mean)
    st.bar_chart(ct_mean)


    ct_margins = pd.crosstab(df['gender'], df['education_level'], margins=True)
    st.write(ct_margins)
    st.area_chart(ct_margins)


    # create a crosstab table of gender and education level with visualization
    ct_viz = pd.crosstab(df['gender'], df['education_level'])
    st.write(ct_viz)
    st.line_chart(ct_viz)

#------------------------------------------------
with st.expander("Group by on multi column"): 
    def generate_sales_data():
        """Generate dataset simulating sales data."""
        np.random.seed(42)
        rows = 50

        # Create a more complex dataset
        df = pd.DataFrame({
            'Product ID': range(1, rows + 1),
            'City': np.random.choice(['Karachi', 'Islamabad', 'Quata', 'Pishawar'], rows),
            'Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Sports'], rows),
            'Base Price': np.random.uniform(10, 500, rows).round(2),
            'Quantity Sold': np.random.randint(1, 100, rows),
        })

        return df


    def configure_grid_options(df):
        """Configure advanced grid options with multiple features."""
        gb = GridOptionsBuilder.from_dataframe(df)
        # Configure row grouping and aggregation
        gb.configure_default_column(
                    groupable=True,
                    value=True,
                    enableRowGroup=True,
                    aggFunc='sum'
                )

                # Add filter and sort options
        gb.configure_grid_options(
                    enableRangeSelection=True,
                    enableRangeHandle=True,
                    suppressColumnMoveAnimation=False,
                    suppressRowClickSelection=False
                )
        # Make some columns editable
        gb.configure_columns(['Base Price', 'Quantity Sold'], editable=True)

        # Add a virtual column (This will be calculated on the client side)
        gb.configure_column(
            'Total Revenue',
            valueGetter="Number(data['Base Price']) * Number(data['Quantity Sold'])",
            cellRenderer="agAnimateShowChangeCellRenderer",
            type=["numericColumn"],
            editable=False,
            valueFormatter="x.toLocaleString('en-US', {style: 'currency', currency: 'USD'})"
        )
        
        return gb.build()


    # Generate data
    sales_data = generate_sales_data()




    #testing 



    # Configure grid options
    grid_options = configure_grid_options(sales_data)
    gb = GridOptionsBuilder()
    gb.configure_default_column(
                    groupable=True,
                    value=True,
                    enableRowGroup=True,
                    aggFunc='sum'
                )

                # Add filter and sort options
    gb.configure_grid_options(
                    enableRangeSelection=True,
                    enableRangeHandle=True,
                    suppressColumnMoveAnimation=False,
                    suppressRowClickSelection=False)
    gb.build()

        

    #st.subheader('Interactive Sales Data Grid')
    st.markdown("""
    **Features:**
    - Edit Base Price and Quantity Sold
    - Automatic Total Revenue calculation
    """)





    # AgGrid with custom options
    ag_return = AgGrid(
        sales_data,
        gridOptions=grid_options,
        height=500,
        theme='alpine',
        allow_unsafe_jscode=True,
        fit_columns_on_grid_load=True,
        reload_data=False
    )



