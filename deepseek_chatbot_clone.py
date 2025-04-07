import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from deep_translator import GoogleTranslator  # Use deep_translator for translation

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client with OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Initialize the translator (deep_translator)
def translate_text(text, target_language):
    translated = GoogleTranslator(source='auto', target=target_language).translate(text)
    return translated

# Language mapping
language_map = {
    'pl': 'Polish',
    'de': 'German',
    'hi': 'Hindi'
}

# Initialize session state for chat history and selected language
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
if "selected_language" not in st.session_state:
    st.session_state.selected_language = 'en'  # Default to English

# Function to get response
def get_response(messages, language):
    try:
        response = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://your-site-url.com",
                "X-Title": "DeepSeek Chatbot",
            },
            model="deepseek/deepseek-chat:free",
            messages=messages,
        )
        if response and response.choices:
            answer = response.choices[0].message.content
            # Translate the answer to the selected language
            translated_answer = translate_text(answer, language)
            return translated_answer
        else:
            st.error("API returned an invalid response.")
            return None
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Streamlit UI
def main():
    st.set_page_config(page_title="DeepSeek Chatbot", page_icon="🧠")
    st.title("🧠 DeepSeek Chatbot")
    st.markdown("Chat with DeepSeek AI using [OpenRouter](https://openrouter.ai).")

    # Language selection
    language_choice = st.selectbox(
        "Select Language",
        options=["English", "Polish", "German", "Hindi"],
        index=0
    )

    # Map language choice to language code
    language_code = {'English': 'en', 'Polish': 'pl', 'German': 'de', 'Hindi': 'hi'}[language_choice]
    st.session_state.selected_language = language_code

    # User input and Send button
    user_input = st.text_input(f"You ({language_choice}):", placeholder="Ask anything...", key="input")

    if st.button('Send', key="send_button"):  # Send button similar to Enter button
        if user_input:
            # Translate user input to English
            translated_input = translate_text(user_input, language_code)
            # Append user message
            st.session_state.messages.append({"role": "user", "content": translated_input})

            # Get the assistant response
            with st.spinner("Thinking..."):
                reply = get_response(st.session_state.messages, language_code)
                if reply:
                    # Append assistant message
                    st.session_state.messages.append({"role": "assistant", "content": reply})

    # Show conversation
    st.markdown("### 💬 Conversation:")
    for msg in st.session_state.messages[1:]:
        if msg["role"] == "user":
            st.markdown(f"**You ({language_choice}):** {msg['content']}")
        elif msg["role"] == "assistant":
            assistant_message = msg['content']
            # Translate assistant message to the selected language
            translated_message = translate_text(assistant_message, language_code)
            st.markdown(f"**DeepSeek ({language_choice}):** {translated_message}")

    # Reset button with a unique key
    if st.button("🔄 Reset Chat", key="reset_chat_button"):
        st.session_state.messages = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
        st.session_state.selected_language = 'en'

    # Reset and Download buttons with unique keys
    if st.session_state.messages[1:]:
        chat_history = "\n".join(
            f"You ({language_choice}): {m['content']}" if m["role"] == "user" else f"DeepSeek ({language_choice}): {m['content']}"
            for m in st.session_state.messages[1:]
        )
        st.download_button(
            label="💾 Download Chat",
            data=chat_history,
            file_name="deepseek_chat.txt",
            mime="text/plain",
            key="download_chat_button"
        )

if __name__ == "__main__":
    main()
