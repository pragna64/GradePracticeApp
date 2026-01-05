import streamlit as st

st.title("Grade Finder")
grades = ["A","B","C","D","F"]
chosen = st.selectbox("Choose your grade:", grades)
if chosen == "A":
    st.write(f"This student got an {chosen}.")
else:
    st.write(f"This student got a {chosen}.")

#https://gradepracticeapp-lzglethe92fzhzgbjysccz.streamlit.app/
#above is the link to the website/app