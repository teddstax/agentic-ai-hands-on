import streamlit as st
from flow import run_flow, FLOW_ID, TWEAKS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the page
st.set_page_config(
    page_title="Customer Support Agent",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .stTextInput > div > div > input {
        background-color: #f0f2f6;
    }
    .stMarkdown {
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .stChatMessage[data-testid="stChatMessage"] {
        background-color: #f0f2f6;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🤖 Customer Support Agent")
st.markdown("""
    Welcome to our AI-powered customer support agent! I can help you with:
    - Order status and details
    - Product information
    - Shipping and delivery times
    - Returns and cancellations
    - General FAQs
    """)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("How can I help you today?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant message placeholder
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Run the flow with the user's message
            response = run_flow(
                message=prompt,
                endpoint=FLOW_ID,
                output_type="chat",
                input_type="chat",
                tweaks=TWEAKS
            )

            # Extract the result from the response
            if isinstance(response, dict):
                result = response['outputs'][0]['outputs'][0]['results']['message']['text']
            else:
                result = response.get("result", "I apologize, but I couldn't process your request. Please try again.")
            
            message_placeholder.markdown(result)
                
        except Exception as e:
            message_placeholder.markdown(f"I apologize, but I encountered an error: {str(e)}")
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": message_placeholder.markdown})

# Add a sidebar with information
with st.sidebar:
    st.header("About")
    st.markdown("""
    This customer support agent is powered by:
    - Langflow for Agentic orchestration
    - OpenAI for natural language understanding
    - Astra DB for knowledge storage and retrieval
    - Streamlit for the user interface
    """)
    
    st.header("Example Questions")
    st.markdown("""
    Try asking:
    - What's the shipping status of order 1001?
    - What was ordered with 1003?
    - What date will order 1004 arrive?
    - How can I cancel order 1001?
    - What is your shipping policy?
    """)
    
    # Add a clear chat button
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun() 