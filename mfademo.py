import streamlit as st
from streamlit_option_menu import option_menu
from openpyxl import Workbook
import pandas as pd

st.set_page_config(page_title="Page Title", layout="wide")
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,

    unsafe_allow_html=True
)


st.markdown(
        r"""
        <style>
        .stAppDeployButton {
                visibility: hidden;
            }
        </style>
        """, unsafe_allow_html=True
    )



#url = "https://docs.google.com/spreadsheets/d/1-6-dNTXR3YLAvRIDRWf9DQsdXw3EAJWt/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true"
url = "https://docs.google.com/spreadsheets/d/1-6-dNTXR3YLAvRIDRWf9DQsdXw3EAJWt/edit?usp=sharing&ouid=105182257404870437876&rtpof=true&sd=true"
file_id = url.split("/")[-2]
path1 = "https://drive.google.com/uc?export=download&id=" + file_id
#sce = pd.read_excel(path1)
st.session_state.df = pd.read_excel(path1)
#st.write(st.session_state.df )
st.header("Web Base ERP ", divider=True)
#st.header("Sample Demo with Video ", divider=True)
#st.header("Muhammad Fahim Aamir- 03336774947 ", divider=True)
st.write("Sample Demo with Video / Muhammad Fahim Aamir-03336774947", divider=True)



Sample_video = st.Page( page = "pages/video.py",
                   title = "Sample VIdeo"
                   )


page_one = st.Page( page = "pages/page1.py",
                   title = "Drag and Drop Pivot Table with selected data export to Excel"
                   )

page_two = st.Page( page = "pages/page2.py",
                   title = "Data Filtering and Graphical Representation"
                   )


page_three = st.Page( page = "pages/page3.py",
                   title = "Organization, finding and exportation of data"
                   )
page_four = st.Page( page = "pages/page4.py",
                   title = "Data filtration and exportation"
                   )

page_five = st.Page( page = "pages/stgraph.py",
                   title = "Ploting the Graph"
                   )

page_six = st.Page( page = "pages/dataent.py",
                   title = "Data Entry with Excel Data Copy and Past"
                   )
page_seven = st.Page( page = "pages/multiselection.py",
                   title = "Master Detail selection Multi Record"
                   )

page_eight = st.Page( page = "pages/getsingerow2.py",
                   title = "Master Detail selection Single Record"
                   )

page_nine = st.Page( page = "pages/masterdetaildataentry.py",
                   title = "Master Detail Data Entry"
                   )

#pages = st.navigation([page_one,page_two,page_three])
pages = st.navigation([Sample_video,page_one,page_two,page_three, page_four,page_five,page_six,page_seven,page_eight,page_nine])

#pages = st.navigation({"Home" : [page_one],"Product" : [page_two],"Address" : [page_three]  }  )
#pages = st.navigation({"Home" : [page_one],"Address" : [page_three]  }  )
pages.run()
#py -m streamlit run c:\demo\mfademo.py

#py -m streamlit run c:\demo\loginpage.py


