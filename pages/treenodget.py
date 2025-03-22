import streamlit  as st

from st_ant_tree import st_ant_tree


st.set_page_config(layout="wide")


tree_data = [
  {
    "value": "parent 1",
    "title": """Test <i>  <b style="color:green"> parent HTML</b><i> test""",
    "children": [
      {
        "value": "parent 1-0",
        "title": "parent 1-0",
        "children": [
          {
            "value": "leaf1",
            "title": "leaf1",
          },
          {
            "value": "leaf2",
            "title": "leaf2",
          },
        ],
      },
      {
        "value": "parent 1-1",
        "title": "parent 1-1",
        "children": [
          {
            "value": "leaf3",
            "title": """<i> <b style="color:green">leaf3</b> </i>""",
          },
        ],
      },
    ],
  },
]



value = st_ant_tree(treeData=tree_data
)

#write streamlit version
st.write("Streamlit Version: " , st.__version__)
st.write("Selected Value: ", value)