import streamlit as st
import random
st.title("おみくじアプリ")
if st. button("おみくじをひく"）:
    results=("大吉","中吉","小吉","吉","凶","大凶")
    result=ramdom.choice(results)
    st.write(f"結果:(result)")