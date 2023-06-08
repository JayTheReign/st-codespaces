import streamlit as st

def main():
    st.title("Hello, Worlds!")
    st.write("This is a super cool Streamlit app.")

if __name__ == '__main__':
    main()
import streamlit as st
valor = st.sidebar.slider('Choose a value:', 0, 10, 6)
st.write('este es tu valor', valor, 'y este es tu valor +10', valor+10)

mayor = st.sidebar.checkbox('El valor es mayor que 5')
if valor > 5 and mayor:
    st.write('este valor es mayor que 5')
import pandas as pd

BigMac = pd.read_csv('big mac.csv')
st.write(BigMac)

st.markdown("## Pais")
name_data = BigMac['name'].unique().tolist()

pais = st.sidebar.selectbox(
    'Which country?',
    (name_data)
)

st.write ("Pais", pais)

df_pais = BigMac.loc[BigMac['name'] == pais]
st.write(df_pais)

import numpy as np
st.line_chart(df_pais, x="date", y="dollar_price")

multipais = st.sidebar.multiselect(
    'Selecciona varios paises',
    name_data)
import altair as alt

df_pais_multi = BigMac[BigMac['name'].isin(multipais)]

import altair as alt

chart = alt.Chart(df_pais_multi).mark_line().encode(
    x='date:T',
    y='dollar_price:Q',
    color='name:N'
)
st.altair_chart(chart)