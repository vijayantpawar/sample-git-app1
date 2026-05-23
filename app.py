import streamlit as st
st.title('CampusX')

col1, col2 = st.columns(2)
with col1:
    st.image('mogli1.webp')
with col2:
    st.header('CampusX is an online Platform')

st.header('Courses')
st.subheader('DSMP')
st.subheader('DAMP')
st.subheader('DEMP')
st.subheader('DSA')

st.sidebar.title('Menu')
st.sidebar.markdown("""
- Home
- About
- Contact
- Career
- Login
""")

st.sidebar.selectbox('roles', ['teacher', 'student'])
st.sidebar.button('Select')

st.title('Hello Teacher')