import streamlit as st
from st_oauth import st_oauth

st.set_page_config(layout="wide", page_title='Stilson Dashboard', page_icon='styles/fwd_ico.png')

# Open css file
st.markdown('<style>' + open('./styles/style.css').read() + '</style>', unsafe_allow_html=True)

if "pages" not in st.session_state:
    pages = st.session_state["pages"] = [st.Page("pages/callback.py", title="Callback"), st.Page("pages/home.py", title="Home"), st.Page("pages/asset_allocation.py", title="Asset Allocation")]
else:
    pages = st.session_state["pages"]

if st.secrets != {}:
    id = st_oauth('fwdoauth')

nav = st.navigation(pages)
nav.run()

if ("ST_AUTH" in st.session_state or st.secrets == {}) and "CALLBACK_REMOVED" not in st.session_state:
    pages = st.session_state["pages"] = st.session_state["pages"][1:]
    st.session_state["CALLBACK_REMOVED"] = True
    nav = st.navigation(pages)