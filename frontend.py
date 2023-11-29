import streamlit as st
import pandas as pd
import numpy as np


# Function to handle the chatbot response (you can integrate your chatbot model here)
def get_chatbot_response(message):
    # Placeholder for chatbot logic
    # Replace this with the actual chatbot response retrieval
    return "Chatbot response to: " + message

# Streamlit app layout
st.title("Simple Chatbot Interface")

# Text input for user message
user_message = st.text_input("Your Message")

# Button to send the message
if st.button("Send"):
    # Display the user message (optional)
    st.write("You: ", user_message)

    # Get the chatbot's response
    response = get_chatbot_response(user_message)

    # Display the chatbot's response
    st.write("Chatbot: ", response)
