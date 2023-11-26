import streamlit as st
import helper as lch
import textwrap

st.title("🆘 YouTube Helper 🆘")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.sidebar.text_area(
            label="YouTube video URL",
            )
        query = st.sidebar.text_area(
            label="Question regarding the video?",
            key="query"
            )
        st.form_submit_button(label='Submit', type="primary")
        st.write("Takes 2-3s for 15 min video, 10-12s for a 1 hr video generally")

if query and youtube_url:
    db = lch.create_db_from_youtube_video_url(youtube_url)
    response, docs = lch.get_response_from_query(db, query)
    st.subheader("Answer:")
    st.text(textwrap.fill(response, width=85))