from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


st.write("""
# <center> Analisis Trend Transaksi Pembelanjaan di Istanbul Periode 2021-2023 </center>

### Kelompok Lima:
- ### Sonia Epifany Sandah
- ### Sugih Gumilar
- ### Yoza Saputra Utama

## [Dataset](https://www.kaggle.com/datasets/mehmettahiraslan/customer-shopping-dataset)
""")

# Read the CSV file into a DataFrame
data = pd.read_csv("customer_shopping_data.csv")
# Display the DataFrame in the app
st.dataframe(data)
