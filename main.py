import streamlit as st
import pandas

st.set_page_config(page_title='Portfolio')
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title("Santhakumar")

    contents = """Hi, I'm santhakumar. i'm learning python now, expecting a python programmer, thats
                all about myself, any problem reach out to me"""
    
    st.info(contents)

content2 =  """ Below you can find some of the apps, feel free to reach me"""
st.write(content2)

df = pandas.read_csv("data.csv", sep=';')

col3, emptycol, col4 = st.columns([2,0.5,2])
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code:] ({row['url']})")

with col4:
    for index, row in df[11:].iterrows():
        st.header(row["title"]) 
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code:] ({row['url']})")   