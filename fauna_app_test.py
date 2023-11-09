import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.title('Fauna Classification Demo with 10Animal Dataset')

st.sidebar.title('Please choose some animals:')

sidebar = st.sidebar

whether_pressed = 'Not submitted'


side_button = sidebar.button('I want this one!', key= 1)
side_button2 = sidebar.button('I want this one!', key=2)
side_button3 = sidebar.button('I want this one!', key=3)
if side_button:
    wait_check = sidebar.checkbox("Wait! I don't want that one", value = False)
    whether_pressed = 'Submitted'
    sidebar.write(whether_pressed)

elif side_button2:
    wait_check = sidebar.checkbox("Wait! I don't want that one", value = False)
    whether_pressed = 'Submitted'
    sidebar.write(whether_pressed)

elif side_button3:
    wait_check = sidebar.checkbox("Wait! I don't want that one", value = False)
    whether_pressed = 'Submitted'
    sidebar.write(whether_pressed)

else:
    sidebar.write(whether_pressed)


