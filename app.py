import streamlit as st

st.set_page_config(page_title="Anshul's GitHub Portfolio", layout="centered")
st.title("Anshul's GitHub Portfolio")
st.markdown("Showcasing selected projects\n---")

projects = [
    {
        "name": "crossfade_ML",
        "desc": "Machine learning project for audio crossfading.",
        "url": "https://github.com/Anshul3901/crossfade_ML"
    },
    {
        "name": "FantasyAgent",
        "desc": "Fantasy sports agent automation project.",
        "url": "https://github.com/Anshul3901/FantasyAgent"
    },
    {
        "name": "HardwareProjects",
        "desc": "Collection of hardware design and simulation projects.",
        "url": "https://github.com/Anshul3901/HardwareProjects"
    },
    {
        "name": "system-programming",
        "desc": "System programming assignments and experiments.",
        "url": "https://github.com/Anshul3901/system-programming"
    },
    {
        "name": "mood_music",
        "desc": "Music recommendation or mood-based music project.",
        "url": "https://github.com/Anshul391/mood_music"
    },
]

for project in projects:
    with st.container():
        st.subheader(project["name"])
        st.write(project["desc"])
        st.markdown(f"[View on GitHub]({project['url']})", unsafe_allow_html=True)
        st.markdown("---")

st.markdown("<div style='text-align:center; color: #888;'>© 2025 Anshul. All rights reserved.</div>", unsafe_allow_html=True) 