import streamlit as st
 
# ---- Custom CSS ----
st.markdown("""
<style>
    .stApp {
        background-color: #f0f8ff;
    }
 
    h1 {
        color: #2E75B6;
        text-align: center;
    }
 
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
    }
 
    .stButton>button:hover {
        background-color: #cc3333;
    }
 
    [data-testid="stSidebar"] {
        background-color: #1a1a2e;
    }
 
    [data-testid="stSidebar"] * {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)
 
# ---- Normal app below ----
st.title("Styled BMI Calculator")
 
st.sidebar.header("Your Details")
name = st.sidebar.text_input("Your name")
weight = st.sidebar.number_input("Weight (kg)", min_value=1.0, value=70.0)
height = st.sidebar.number_input("Height (cm)", min_value=50.0, value=170.0)
 
if st.sidebar.button("Calculate BMI"):
    bmi = round(weight / (height / 100) ** 2, 1)
    if bmi < 25:
        category = "Normal weight"
    else:
        category = "Above normal"
 
    if name:
        st.header(f"Results for {name}")
    col1, col2 = st.columns(2)
    col1.metric("BMI", bmi)
    col2.metric("Category", category)
