import streamlit as st

def main():
    st.title("Hello, Worlds!")
    st.write("This is a super cool Streamlit app.")

if __name__ == '__main__':
    main()
import streamlit as st
valor = st.slider('Choose a value:', 0, 10, 6)
st.write('este es tu valor', valor, 'y este es tu valor +10', valor+10)
if valor > 5:
    st.write('este valor es mayor que 5')
