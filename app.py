import streamlit as st 
import pandas as pd
import numpy as np

st.title("App de streamlit")
st.header("Este es un encabezado")
st.subheader("Este es un subencabezado")
st.write("Este es un parrafo")
st.write("Este es un segundo parrafo")
st.write("Este es un tercer parrafo")
"_________________________________"

df = pd.dataframe(np.random.randn(10, 2), colums=['precios', 'ventas'])
st.dataframe(df)
