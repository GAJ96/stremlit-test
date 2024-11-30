# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 10:36:49 2024

@author: gaabr
"""

import streamlit as st
from streamlit_lottie import st_lottie
import requests




st.set_page_config(
    page_title="Home",
    page_icon=":dromedary_camel:",
    layout="wide"
    )





st.title("Are YOU worthy of the")
st.title("CHALLENGE")


st.write("")
st.write("or are you a n00b?")
st.write("")
st.write("")

url_pro_camel = "https://lottie.host/4bb410be-4a52-4617-9173-4a017f134adc/6P3uhl4JW6.json"
url_noob_cat = "https://lottie.host/ca2d3131-a007-4580-bdfa-c3a369c390f3/wdQyB9lDVs.json"





def get_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        # error
        pass
    else:
        # success
        return r.json()



with st.container():

    left_column1, right_column1 = st.columns(2)
    
    with left_column1:
        st_lottie(get_lottie(url_pro_camel), height=225)
    
    #left_column, right_column = st.columns(2)
    
    with right_column1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("This is a pro camel")


    left_column2, right_column2 = st.columns(2)
    
    with left_column2:
        st_lottie(get_lottie(url_noob_cat), height=125)
    
    #left_column, right_column = st.columns(2)
    
    with right_column2:
        st.write("")
        st.write("")
        st.write("")
        st.write("and this is a noob cat.")

st.write("")
st.subheader("Don't be a noob cat,")
st.subheader("be a pro camel")

#lottie_noob_cat = get_lottie(url_noob_cat)
