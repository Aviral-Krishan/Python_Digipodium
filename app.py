import streamlit as st
st.image('............link.......')
st.video('............. video link.........')
st.title("String App")
message = st.text_area('Enter text')
button = st.button('process text')
if button:
    st.write(message)
if st.sidebar.checkbox("show words"):
        words = message.split()
        st.write(words)
if st.sidebar.checkbox("character count"):
    for char in message:
        st.write(f'{char} : {message.count(char)}')

        
