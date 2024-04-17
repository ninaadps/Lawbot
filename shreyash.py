import streamlit as st
import anthropic

# Set the API key
ANTHROPIC_API_KEY = "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"

# Initialize the anthropic client
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

# Create a Streamlit web application
st.title('Law Related Query Bot')

# Create a text input for user to enter the prompt
user_prompt = st.text_area('Enter your law-related query here', height=200)

# Create a button to trigger the API request and display the response
if st.button('Get Response'):
    # Send the user prompt to the API
    message = client.messages.create(
       
        model="claude-3-haiku-20240307",
        system="You are a law expert who answers questions using the Indian Constitution.",
        max_tokens=1024,
        messages=[{"role": "user", "content": user_prompt}]
        
    )
    
    # Display the response
    st.write('**Response:**')
    st.write(message.content[0].text)
