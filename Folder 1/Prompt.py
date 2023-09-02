'''
This is one demo about user interaction conversation between two user
For examle:
One User:       Human
Second User:    Machine

General script for live interaction platform.
'''

# import libraries
import os
import numpy as np
import streamlit as st

# Set title
st.title("User interaction")

# Make a list of dictionary, namely 'messages'
if 'messages' not in st.session_state:
    st.session_state.messages = []


# To continue the loop of conversation
for message in st.session_state.messages:
    with st.chat_message(message["question"]):
        st.markdown(message["answer"])

# Run the live conversation
# Enter prompt
if prompt := st.chat_input("What's up?..."):
    
    # Append the 'prompt' as a 'user'
    st.session_state.messages.append({"question":"user","answer":prompt})
    
    # Show user's prompt
    with st.chat_message("user"):
        st.markdown(prompt)
        
    # Show assistant's response
    with st.chat_message("assistant"):
        answer = np.random.choice(["Hello World", "I am fine", "Good to see you"])
        st.markdown(answer)
    
    # Append the 'response' as a 'assistant'
    st.session_state.messages.append({"question":"assistant", "answer":answer})