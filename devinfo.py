import streamlit as st

def display_dev_info():
    # Dev info
    st.divider()
    st.write("About developer...")
    b = st.link_button(label="Developer's Github", url='https://github.com/adityapradhan202', type='primary')
    a = st.link_button(label="Developer's LinkedIn", url='https://www.linkedin.com/in/adipradhan202', type='primary')
