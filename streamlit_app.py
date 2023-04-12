from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


st.write("""
# MY first app
Hello *world!*
""")

df = pd.read_csv("my_data.csv")
st.line_chart(df)
