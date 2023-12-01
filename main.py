import pandas as pd
import streamlit as st

# Load your custom CSS file
with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)