import pandas as pd
import streamlit as st

video_file = open("dent.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)
data = {
    'Department': ['Department 1', 'Department 2', 'Department 3', 'Department 4', 'Department 5'],
    'Number': [10, 20, 30, 40, 50],
    'Student': ['andsf', 'lkjlkjsf', 'jflkdfjgfd', 'jjerljt', 'jlkdjfgd'],
    'Subject': ['C++', 'JAVA', 'DBMS', 'DWHS', 'a-i']
}
st.header("Data Entry with imort Excel data")
df = pd.DataFrame(data)
#st.data_editor(df, key="dept_tbl",     on_change=validate_cnt())
edited_df = st.data_editor(df, num_rows="dynamic")

#df_join = pd.merge(df_left, df_right, left_index=True, right_index=True)
#st.dataframe(df_join)





