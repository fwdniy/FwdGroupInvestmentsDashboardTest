import streamlit as st
from utils.interface.menu import menu
from streamlit_js_eval import streamlit_js_eval
from streamlit import session_state as ss

st.set_page_config(layout="wide", page_title='Stilson Dashboard', page_icon='styles/fwd_ico.png')
streamlit_js_eval(js_expressions="window.innerWidth", key='SCR')

menu('streamlit_app.py')

st.write(f'# Stilson Dashboard')
st.write(f'## Welcome {ss["nickname"]}! 👋')
st.write(f'For any enhancements or bugs, please contact {st.secrets["admin"]["name"]} via Teams or email ({st.secrets["admin"]["email"]})')

with st.expander("Change Notes", True):
    st.write("2025/01/02")
    st.write(" - Add user permissions to restrict access to certain pages")
    st.write("2024/12/21")
    st.write(" - Curves: added implied forward rates")
    st.write(" - Funnelweb Pivot Table: enhanced interface and added weighted average metrics")
    st.write("2024/12/20")
    st.write(" - Hong Kong - Asset Allocation: Changed WARF table to exclude repos and bond forwards")