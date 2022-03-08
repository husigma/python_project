#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 22:45:54 2021

@author: kurtbembridge
"""

import streamlit as st

def calculate(a, b):
    try:
        a = float(a)
        b = float(b)

        if a >40:
            above_hour = a - 40
            above_pay = above_hour * (1.5 * b)
            gross = 40 * a
            total = gross + above_pay
            return(total)
        else:
            total = a * b
            return(total)
    except:
        print("Please enter a number, thank you ")

def main():       

    hour = st.slider("Enter how much hour you work ", 1, 100, 40)
    pay = st.slider("Enter your pay ", 1, 500)
    
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Calculate Pay"): 
        result = calculate(hour, pay)
        st.write('Your pay is {}'.format(result))
     
if __name__=='__main__': 
    main()