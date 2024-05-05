import streamlit as st
from mess_data import mayuri_mess_data as mmd
import time

st.header("Welcome to VBMESS :pizza:")
st.caption("Note - Data for the other mess of VITB will be added soon!")
st.markdown("##### Select the day and the meal type and get the respective food items :smile:")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "None"]
meals = ["Breakfast", "Lunch", "Snacks", "Dinner", "None"]

selected_day = st.selectbox(label="Select day", options=days, index=days.index("None"))
selected_meal = st.selectbox(label="Select meal type", options=meals, index=meals.index("None"))

if selected_day != "None" and selected_meal != "None":
    st.write(f"Here are the food items of {selected_day}-{selected_meal}")
    for ind, item in enumerate(mmd[selected_day][selected_meal]):
        st.write(f"{ind+1}) {item}")
        time.sleep(0.25)


    
    st.divider()
    st.write("About developer...")
    b = st.link_button(label="Developer's Github", url='https://github.com/adityapradhan202', type='primary')
    a = st.link_button(label="Developer's LinkedIn", url='https://www.linkedin.com/in/adipradhan202', type='primary')


            
