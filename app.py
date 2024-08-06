import streamlit as st
from mess_data import mayuri_mess_data as mmd
import time
from night_canteen_data import nc_data
import devinfo

st.header("Welcome to VBMESS :pizza:")
st.caption("Note - Data for the other mess of VITB will be added soon!")
st.markdown("##### Select the place/meal-type to see respective food items(with/without price) :smile:")

mess_canteen_type = [
    "Mayuri mess", "Mayuri mess night canteen", "Under belly AB", "None"
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "None"]
meals = ["Breakfast", "Lunch", "Snacks", "Dinner", "None"]


selected_place = st.selectbox(label="Select mess or canteen type", options=mess_canteen_type, index=mess_canteen_type.index("None"))

if selected_place == "Mayuri mess":

    selected_day = st.selectbox(label="Select day", options=days, index=days.index("None"))
    selected_meal = st.selectbox(label="Select meal type", options=meals, index=meals.index("None"))

    if selected_day != "None" and selected_meal != "None":
        st.write(f"Here are the food items of {selected_day}-{selected_meal}")
        for ind, item in enumerate(mmd[selected_day][selected_meal]):
            st.write(f"{ind+1}) {item}")
            time.sleep(0.25)

        devinfo.display_dev_info()

elif selected_place == "Mayuri mess night canteen":
    for cat in nc_data:
        st.markdown(f"▶️ :orange[{cat}]")
        for ind, item in enumerate(nc_data[cat]):
            st.write(f"{ind + 1}. {item} - {nc_data[cat][item]} rupees")
            time.sleep(0.1)
    st.caption("WITH EXTRA 5 PERCENT GST")

    devinfo.display_dev_info()

elif selected_place == "Under belly AB":
    st.write("This part is under maintenance! It will get update soon!")
