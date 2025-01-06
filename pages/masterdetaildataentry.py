import streamlit as st
from streamlit import session_state as ss
import pandas as pd
video_file = open("mdde.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)
st.header("Master Detail Date Entery")

def mpg_change():
    
    edited_rows: dict = ss.mpg['edited_rows']
#    st.write(edited_rows)
    ss.selected_row_index = next(iter(edited_rows))
    #ss.df = ss.df.assign(selected=False)
    ss.df1.loc[ss.df1['selected'], 'selected'] = False
    update_dict = {idx: values for idx, values in edited_rows.items()}
    ss.df1.update(pd.DataFrame.from_dict(update_dict, orient='index'))



if 'selected_row_index' not in ss:
    ss.selected_row_index = None


@st.cache_data
def get_data(nrows):
    url = 'https://raw.githubusercontent.com/Munees11/Auto-MPG-prediction/master/Scripts/auto_mpg_dataset.csv'
    return pd.read_csv(url, nrows=nrows)


if 'df1' not in ss:
    ss.df1 = get_data(10)
    ss.df1['selected'] = [False] * len(ss.df1)
    ss.df1 = ss.df1[['cylinders', 'car_name', 'mpg', 'selected']]
    #st.write(ss.df1)
    #df2 = ss.df[['cylinders', 'car_name', 'mpg', 'selected']]



st.markdown('### Master Table  ')
with st.container(border=True):
        edf = st.data_editor(
            ss.df1,
             num_rows="dynamic",
            hide_index=True,
            on_change=mpg_change,
            key='mpg',
            use_container_width=True
        )
st.subheader(f'Detail Table ')
selected_indices = ss.selected_row_index

if selected_indices == None:
        st.write("muhammad is the best ")
else :
        #st.write(selected_indices)
        #mfatt= st.dataframe(ss.df.loc[selected_indices]) 
        #selected_rows = ss.df.loc[selected_indices]
        #st.write(mfatt)
        #st.write(edf)
        df3 = pd.DataFrame(edf)
        dfm = df3.iloc[[selected_indices]]
        #st.dataframe(dfm)
        st.data_editor(dfm,
             num_rows="dynamic", hide_index=True)

        #st.write(mfatt)
        
    
    
    #mfat =  int( ss.selected_row_index)
    #selected_rows = ss.df.loc[ss.selected_row_index]
    #selected_rows = edf
    #selected_rows = selected_rows.loc[selected_indices]
    #st.write(selected_rows)
    #st.write(edf)
    #df3 = pd.DataFrame(edf)
    #selected_indices1  = int(selected_indices)
    #st.write(selected_indices)
    #dfm = df3.iloc[[selected_indices]]
    #st.write(dfm)
    #df1 =  df.iloc[[2]]
    #print(dfm)

    #if ss.selected_row_index is not None:
        #st.write(f'car name: {ss.df.at[ss.selected_row_index, "car_name"]}')
    


    

    

# event = st.dataframe(    st.session_state.df,    key="data",    on_select="rerun",    selection_mode=["multi-row", "multi-column"],)
#event.selection


#selected_indices = st.multiselect('Select rows:', df.index)
# Subset the dataframe with the selected indices
#selected_rows = df.loc[selected_indices]
# Display the selected data
#st.write('Selected Rows:')
#st.dataframe(selected_rows)

