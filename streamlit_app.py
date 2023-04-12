from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


st.write("""
# MY first app ubah
Hello *world!*
""")

# Read the CSV file into a DataFrame
data = pd.read_csv("customer_shopping_data.csv")
# Display the DataFrame in the app
st.dataframe(data)
