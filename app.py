import streamlit as st
from mess_data import mayuri_mess_data as mmd
import time
from day_time import wday_dict
from day_time import current_weekday
from day_time import current_hour

current_meal = ""
if current_hour <= 9:
    current_meal = "Breakfast"
elif current_hour <= 14:
    current_meal = "Lunch"
elif current_hour <= 18:
    current_meal = "Snacks"
elif current_hour <= 21:
    current_meal = "Dinner"
elif current_hour > 21:
    current_meal = "Breakfast"


st.header("Welcome to VBMESS :pizza:")

st.markdown("##### Select the day and the meal type and get the respective food items of the menu. Whether you're in the mood for a hearty lunch or a light snack, we've got you covered.")
st.write("##### So go ahead, explore the menus, and satisfy your taste buds!")
st.write("##### Happy eating! :smile:")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
meals = ["Breakfast", "Lunch", "Snacks", "Dinner"]

c1,c2 = st.columns(2)
with c1:
    selected_day = st.selectbox(label="Select day", options=days, index=days.index(wday_dict[current_weekday]))
with c2:
    selected_meal = st.selectbox(label="Select meal", options=meals, index=meals.index(current_meal))


if selected_meal != None and selected_day != None:
    st.markdown(f"##### Here are your food items for {selected_meal} of {selected_day}")
    for x, i in enumerate(mmd[selected_day][selected_meal]):
        st.write(f"{x+1}) {i}")
        time.sleep(0.25)
    
    
    st.divider()
    st.write("Some information about the developer...")
    b = st.link_button(label="Developer's Github", url='https://github.com/adityapradhan202', type='primary')
    a = st.link_button(label="Developer's LinkedIn", url='https://www.linkedin.com/in/adipradhan202', type='primary')


            
