# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 10:36:49 2024

@author: gaabr
"""

import streamlit as st
from streamlit_lottie import st_lottie
import requests



st.set_page_config(
    page_title="Pro or n00b?",
    page_icon=":dromedary_camel:",
    layout="wide")





st.subheader("Are you a noob or a pro?")
pro = st.checkbox("I am a pro!")
noob = st.checkbox("I am a noob!")








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





if pro and not noob:
   
    left_column1, right_column1 = st.columns(2)
    with left_column1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.title("GONGRATULATIONS!:tada:")
        st_lottie(get_lottie(url_pro_camel), height=350)
        st.title("YOU ARE AS PRO AS THIS CAMEL! :tada:")

elif noob and not pro:
   
    left_column1, right_column1 = st.columns(2)
    with left_column1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.title("HaHaHahaHAAA")
        st_lottie(get_lottie(url_noob_cat), height=300)
        st.title("You are such a n00b XD XD XD")

elif pro and noob:
    
    left_column1, right_column1 = st.columns(2)
    with left_column1:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.title("HaHaHahaHAAA")
        st_lottie(get_lottie(url_noob_cat), height=300)
        st.title("You cant be both pro and noob at the same time, you are such a f\*cking uber n00b, go shit your pants")
        st.write("")
        st.write("(Obviously Im just joking so dont be an offended pussy ass bitch)")
else:
    pass
