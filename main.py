import streamlit as st
from langchain_helper import generate_restaurant_name_and_items

st.set_page_config(page_title="Restaurant Name Generator", page_icon="🍽️")
st.title("🍽️ Restaurant Name Generator")

# Sidebar input
cuisine = st.sidebar.selectbox(
    "Pick a Cuisine",
    (
        "Indian", "Italian", "Mexican", "Chinese", "Thai", "Japanese",
        "French", "Greek", "Spanish", "Moroccan", "Turkish",
        "Vietnamese", "Lebanese", "Korean", "Ethiopian"
    )
)

theme = st.text_input("Restaurant Theme", "Modern Fusion")
location = st.text_input("Location", "Delhi")

if st.button("Generate Restaurant Name"):
    with st.spinner("Generating..."):
        response = generate_restaurant_name_and_items(cuisine, theme, location)

        st.header(f"✨ {response['restaurant_name']}")
        st.subheader("Menu Suggestions:")
        for item in response["menu_items"].split(","):
            st.write(f"- {item.strip()}")
