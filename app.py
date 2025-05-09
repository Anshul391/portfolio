import streamlit as st
import os

st.set_page_config(page_title="Anshul's GitHub Portfolio", layout="centered")

# Sidebar navigation
page = st.sidebar.selectbox("Navigate", ["Portfolio", "About Me"])

if page == "Portfolio":
    st.title("Anshul's GitHub Portfolio")
    st.markdown("Showcasing selected projects\n---")
    projects = [
        {"name": "crossfade_ML", "desc": "Machine learning project for audio crossfading.", "url": "https://github.com/Anshul3901/crossfade_ML"},
        {"name": "FantasyAgent", "desc": "Fantasy sports agent automation project.", "url": "https://github.com/Anshul3901/FantasyAgent"},
        {"name": "HardwareProjects", "desc": "Collection of hardware design and simulation projects.", "url": "https://github.com/Anshul3901/HardwareProjects"},
        {"name": "system-programming", "desc": "System programming assignments and experiments.", "url": "https://github.com/Anshul3901/system-programming"},
        {"name": "mood_music", "desc": "Music recommendation or mood-based music project.", "url": "https://github.com/Anshul391/mood_music"},
    ]
    for project in projects:
        with st.container():
            st.subheader(project["name"])
            st.write(project["desc"])
            st.markdown(f"[View on GitHub]({project['url']})", unsafe_allow_html=True)
            st.markdown("---")
    st.markdown("<div style='text-align:center; color: #888;'>© 2025 Anshul. All rights reserved.</div>", unsafe_allow_html=True)

elif page == "About Me":
    st.title("About Me")
    st.markdown("""
    **Anshul Prakash**  
    [LinkedIn](#)  
    anshul.prakash.391@gmail.com | 832-998-5051 | Redmond, WA  
    [GitHub](https://github.com/Anshul3901?tab=repositories)
    """)
    st.header("Education")
    st.markdown("""
    **The University of Washington** (March 2026)  
    Masters of Science in Innovation Technology Robotics Focus  
    Notable Coursework: Robotics Lab, Managing Data and Signal Processing

    **Washington State University** (May 2024)  
    Bachelor of Science in Computer Engineering (Minor in Computer Science and Electrical Engineering)  
    Notable Coursework: Fundamentals of Digital Systems, Operating Systems, and Computer Architecture.
    """)
    st.header("Work Experience")
    st.markdown("""
    **Software Engineering Intern: Schweitzer Engineering Laboratory**  
    October 2022 - October 2023  
    - Formulated comprehensive functional and unit tests for Test Driven Development, in C++ and Xilinx environment; achieved 75% reduction in critical software bugs, enhancing system stability and reliability.
    - Added automated documentation for all repositories triggered on release making documentation available for the Research and Development department of over 200 users.
    - Designed demos for modules utilized in the Operating System such as the General Interrupt Controller and Triple Timer Counter prototyping features for future users.
    - Resolved circular dependencies accelerating the release process and build by 50%.

    **Software Engineering Intern: Truveta**  
    May 2022 - August 2022  
    - Designed, developed, and launched an end-to-end Email Notification Service including an email template management system using the .NET framework in an Agile project management system.
    - Exposed Email Notification Service functions through RESTful APIs to be used by other services automating and speeding up the notification process.
    - Executed UX template management operations in Redux for front-end infrastructure and React.js for User Interface.
    - Created Architecture diagrams and Data Flow Diagrams in Mira for Email Notification Service.

    **Target: Tech consultant**  
    June 2019 - September 2020  
    - Asked customers diverse questions to find the best solution for their problems.
    - Troubleshooted customers' technical issues with products from major companies such as Apple, Samsung Lenovo, and Microsoft.
    """)
    st.header("Projects")
    st.markdown("""
    **FantasyEdge:**  
    - Used Yahoo fantasy and OAuth APIs to access fantasy football league for detailed information of players in the league teams and available players.
    - Built AI agent using llama index and Open AI developer APIs that uses past performance data, and player injuries to give suggestions on improving the users Fantasy Football team.

    **VGA Display Controller:**  
    - Utilized Artix FPGA to access HDMI peripherals to display information on a monitor in Verilog.
    - Formulated VGA sync IP to parse through pixels and manipulate specific pixels to show meaningful information.

    **Custom IP Blocks:**  
    - Manufactured custom IP blocks on Artix FPGA using Verilog to export and program on ARM Cortex-A9.
    - Customized algorithms for different blinking patterns on LEDs accessible from custom hardware IPs.
    """)
    st.header("Skills and Interests")
    st.markdown("""
    **Skills:** Java, C, C++, C#, Redux with Typescript, .NET, Verilog, Mira, Jenkins, Assembly coding, Operating System development, and Computer Architecture.  
    **Interests:** Robotics, Embedded Systems, Operating Systems, Guitar, Cricket, Soccer.
    """)
    # PDF download link
    if os.path.exists("Anshul Prakash-2.pdf"):
        with open("Anshul Prakash-2.pdf", "rb") as pdf_file:
            st.download_button(
                label="Download Resume (PDF)",
                data=pdf_file,
                file_name="Anshul Prakash-2.pdf",
                mime="application/pdf"
            )
    else:
        st.info("Resume PDF not found.") 