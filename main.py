import streamlit as st

def submit():
    st.text("Thank you! Free money and other cool suff will be sent to you soon!")

num = st.slider('Enter your phone number here!!!!!', min_value=10000.0, max_value=19999.999999, step=0.000001)
subtract = st.slider('EMERGENCY FINE TUNING', min_value=0.0, max_value=1000.000, step=0.001)
subtract *= 1000000
num *= 1000000
num = int(num)
num -= int(subtract)

num = str(num)
num =  num[0] + '+ (' +num[1:4] + ') ' + num[4:7] + '-' + num[7:]
num

st.button('Submit', on_click=submit)



# 1 (xxx) xxx-xxxx
