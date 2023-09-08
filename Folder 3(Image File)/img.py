import streamlit as st

# Initialize a streamlit file uploader widget.
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    st.write(uploaded_file.type)

# If user attempts to upload a file.
if uploaded_file is not None:
    if uploaded_file.type.split("/")[0] == str("image"):
        bytes_data = uploaded_file.getvalue()

        # Show the image filename and image.
        st.write(f'filename: {uploaded_file.name}')
        st.image(bytes_data)