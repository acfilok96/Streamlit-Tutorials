'''
This is one demo about user interaction conversation between two user
For examle:
One User:       Human
Second User:    Machine

General script for live interaction platform.
'''

# import libraries
import os
import time
import numpy as np
import streamlit as st

# Set title
st.title("User interaction: Part 2")

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
        # Pick one random string
        answer = np.random.choice(["Hello World", 
                                   "I am fine", 
                                   "Good to see you", 
                                   "Hello World, how are you ?",
                                   "Although you can deploy multiple apps from the same repository, there can be only one configuration file.",
                                   "An app URL with a random hash is prefilled but you can change this to a custom subdomain instead."])
        message_placeholder = st.empty()
        answer = answer.split(" ")
        response_temp = " "
        for part in answer:
            response_temp += str(part)+" "
            time.sleep(0.2)
            message_placeholder.markdown(response_temp + "▌")
    
    # Append the 'response' as a 'assistant'
    st.session_state.messages.append({"question":"assistant", "answer":response_temp})