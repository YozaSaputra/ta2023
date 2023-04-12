from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


st.write("""
# MY first app ubah
Hello *world!*
""")

df = pd.read_csv("./ta2023/customer_shopping_data.csv")
st.line_chart(df)
