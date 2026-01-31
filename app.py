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

df = pd.DataFrame(np.random.randn(10, 2), columns=['precios', 'ventas'])
st.line_chart(df, x_label="Posición", y_label="Valor", color= ["#B439B0","#C16B20"])
st.dataframe(df)

"__________________________________"

st.markdown("""
# hola  
```
import streamlit as st 
import pandas as pd
import numpy as np
```
""")

"""
## hola
"""
