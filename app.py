import streamlit as st
st.title('CampusX')

col1, col2 = st.columns(2)
with col1:
    st.image('mogli.jpg')
with col2:
    st.header('CampusX is an online Platform')

st.header('Courses')
st.subheader('DSMP')
st.subheader('DAMP')
st.subheader('DEMP')