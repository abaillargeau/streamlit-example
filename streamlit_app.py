import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
"""
# Analysis steps

Let's try!

"""
# Bouton
if st.button("Push!"):
    st.success(f"You pushed: {'Good boy!'}")

# Select date
start_date = st.date_input("Select beginning day and time")
end_date = st.date_input("Select end day and time")


