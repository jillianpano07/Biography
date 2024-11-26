import streamlit as st

# Set the page title
st.set_page_config(page_title="My Biography", page_icon=":guardsman:", layout="wide")

# Add a header and bio info
st.title("Jillian Paño's Biography")
st.write("Welcome to my biography page. Below are some details about me:")

# Add an image
st.image("https://scontent-mnl1-1.xx.fbcdn.net/v/t1.15752-9/462547333_1292650638420964_1162871413909445747_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=9f807c&_nc_eui2=AeGaLepxexNvP3xzf-1fGStlz50d318-IdfPnR3fXz4h1y3gnLD5N5ptQTYf2BGYqV-1QPTR9p01S30a-HTzqZnJ&_nc_ohc=w3sCCm415e0Q7kNvgHUQLvm&_nc_zt=23&_nc_ht=scontent-mnl1-1.xx&oh=03_Q7cD1QEewRS2HyM9rBX-cKeobuw3FDoX4dp3ZGrx0p00wPKdrw&oe=676CC4FB", width=200)

# Personal Information
st.header("Personal Information")
st.write("""
- *Name*: Jillian Joy Paño
- *Date of Birth*: July 7, 2006
- *Status*: Single
- *Email*: jillianjoypano2006@gmail.com
- *Phone*: 09662690517
- *Location*: P-4 Balite, San Francisco, Surigao Del Norte
""")

# Education Section
st.header("Education")
st.write("""
- *Gen. T. De Leon Elementary School 
         A.Y(2011-2014)
- *Antonio M. Serapio Elemnentary Sschool
         A.Y(2014-2018)
- *Justice Eliezer Delos Santos National High School
         A.Y(2018-2022)
- *Balite National High School
         A.Y(2022-2024)
""")

# Project Section
st.header("Project Section")
st.write(""" 
Published Research:
 Reasons Behind Students Lack of Participation on School Activities: A comprehensive study (currently on semantic scholar)
""")

# Achievement Section
st.header(" Achievements")
st.write("""
- With Honors (2022-2023)
- With High Honors (2023-2024)
- Special Award in Work Immersion 
- Special Award in Performing Arts
""")

# Skills Section
st.header("Skills")
st.write("""
- Software & Tools: Microsoft Office
- Communication:Verbal and Written Communication
- Teamwork: Collaboration & Interpersonal Skills
- Adaptability
""")


# Hobbies & Interests Section
st.header("Hobbies & Interests")
st.write("""
- Traveling
- Numerology
- Cats
- Cooking
- Learning anything that caught my interest
""")

# Footer Section
st.write("Thanks for visiting my Biography  page. Feel free to reach out!")