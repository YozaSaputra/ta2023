from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


st.write("""
# Analisis Trend Transaksi Pembelanjaan di Istanbul Periode 2021-2023

### Kelompok Lima:
- ### Sonia Epifany Sandah
- ### Sugih Gumilar
- ### Yoza Saputra Utama

## [Dataset](https://www.kaggle.com/datasets/mehmettahiraslan/customer-shopping-dataset)

## Latar Belakang Masalah
Pada tahun 2020 tepatnya pada bulan Maret, terjadi suatu pandemi yang melanda seluruh dunia, yaitu pandemi Covid 19. Pandemi ini menyebabkan masalah yang serius karena banyak negara yang mengalami kerugian akibat adanya pandemi ini, salah satunya adalah kerugian ekonomi. Salah satu object yang terdampak dari pandemi adalah Shopping Mall. Oleh karena itu, kami ingin menganalisa tren dan kebiasaan belanja di negara Istanbul selama masa pandemi dengan menggunakan data dari 10 Mall pada periode tahun 2021-2022.
""")

st.markdown('<div style="text-align: center;">Hello World!</div>', unsafe_allow_html=True)

# Read the CSV file into a DataFrame
data = pd.read_csv("customer_shopping_data.csv")
# Display the DataFrame in the app
st.dataframe(data)
