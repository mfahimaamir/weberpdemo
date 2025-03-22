import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from pivottablejs import pivot_ui
st.header("Drag and Drop Pivot Table with selected data export to Excel")
t = pivot_ui(st.session_state.df)
with open(t.src) as t:
     components.html(t.read(), width=900, height=1000, scrolling=True)
    
    


mdf = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "F": ['AA01', 'AAA2', 'AAA2', 'DDD3', 'DDD3', 'FFF4', 'FFF5', 'TTT6', 'RRR7'],
                   "G": ['ADDA01', 'ADDAA2', 'AFFAA2', 'DFFDD3', 'DFFDD3', 'FDDFF4', 'FFFFF5', 'TDDTT6', 'RRR7'],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})

LL= ['C','G' ]
table = pd.pivot_table(mdf, values='E', index=['A', 'B'],
                       columns=LL, aggfunc="count")
st.write(table)


df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',
                           'two'],
                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'baz': [1, 2, 3, 4, 5, 6],
                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})


l1 = ['baz', 'zoo']




l11= ["SIMESTER","COURSE","TECHER"]
l22= ["ROOM","TIME"]
l33= ["SGRNO"]

#st.write(st.session_state.df)
mfadf = pd.DataFrame(st.session_state.df)

#df10=  df.pivot(index='foo', columns='bar',values= 'baz', aggfunc='sum', fill_value=0)
#df.pivot_table(index='Account_number', columns='Product', aggfunc='count')v
#df10=  mfadf.pivot(index=l11, columns=l22, values=l33)

st.write(mfadf )
#table2 = mfadf.pivot_table(mfadf, values='ROOM', index='COURSE', columns='TECHER' )
#st.write(table2)

#, aggfunc="count")


df1 =  df.pivot(index='foo', columns='bar', values=l1)
#df1 =  df.pivot(index='foo', columns='bar', values=['baz', 'zoo'])
st.write(df1)
st.write(l1)
#df.pivot(index='foo', columns='bar', values='baz')


df2 = pd.DataFrame({
       "lev1": [1, 1, 1, 2, 2, 2],
       "lev2": [1, 1, 2, 1, 1, 2],
       "lev3": [1, 2, 1, 2, 1, 2],
       "lev4": [1, 2, 3, 4, 5, 6],
       "values": [0, 1, 2, 3, 4, 5]})

l2 = ["lev2", "lev3"]
df3 = df2.pivot(index="lev1", columns=l2 ,values="values")
st.write(df3)

print("muhammad is the best ")
l3 = ["values"]
df5 = df2.pivot(index="lev1", columns=l2 ,values=l3)
st.write("muhammad is the best ")
#st.write(df5)
st.dataframe(df5)
st.dataframe(df5.style.set_properties(**{'font-size': '50pt'}))


st.write(st.session_state.df9)



