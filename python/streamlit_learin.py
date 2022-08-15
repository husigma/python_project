import streamlit as st


def addition(a = 4, b = 5):
    try:
        a = float(a)
        b = float(b)
        return(a+b)
    except:
        err()
        continue

def err():
    print('Please enter a number, what you ener was not a number')


st.write("Hello ,let's learn how to build a streamlit app together")

