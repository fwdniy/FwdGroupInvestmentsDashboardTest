import streamlit as st
from utils.interface.menu import menu
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(layout="wide", page_title='Stilson Dashboard', page_icon='styles/fwd_ico.png')
streamlit_js_eval(js_expressions="window.innerWidth", key='SCR')

hide_github_icon = """
#GithubIcon {
  visibility: hidden;
}
"""

st.markdown(hide_github_icon, unsafe_allow_html=True)

menu('Home')

st.write("# Welcome to the Stilson Dashboard! 👋")
st.write("For any enhancements or bugs, please contact Nicolas Au-Yeung via Teams or email (nicolas.au.yeung@fwd.com)")