import streamlit as st

# Page configuration
st.set_page_config(page_title="User Insights Dashboard", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
pages = {
    "User Overview Analysis": "pages/user_overview.py",
    "User Engagement Analysis": "pages/engagement_analysis.py",
    "Experience Analysis": "pages/experience_analysis.py",
    "Satisfaction Analysis": "pages/satisfaction_analysis.py"
}

# Select page
page = st.sidebar.radio("Go to:", list(pages.keys()))

# Render the selected page
exec(open(pages[page]).read())
