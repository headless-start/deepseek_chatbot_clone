# 🧠 DeepSeek Chatbot

This project demonstrates a **chatbot** built with **OpenRouter** (DeepSeek) and integrated with **Google Translator** for multi-language support using **Streamlit**. The application allows users to chat with an AI assistant that can understand and respond in multiple languages.

## 🚀 Key Features
1. **Multi-language Support**  
   - Users can chat in **English**, **Polish**, **German**, and **Hindi**.

2. **Language Translation**  
   - All user inputs and assistant responses are translated using **Google Translator** to ensure smooth interaction in the selected language.

3. **Chat History**  
   - Users can download the chat history as a `.txt` file for offline use.

4. **Interactive Chat Interface**  
   - The chatbot interface is built using **Streamlit**, allowing easy and intuitive interaction.

---

## 🔧 How It Works

1. **Language Selection**  
   - The user selects the preferred language from a dropdown menu.

2. **Chat Input**  
   - The user inputs their question or statement in the selected language.

3. **Translation & AI Response**  
   - The input is translated to English and sent to the **DeepSeek AI** for a response. The assistant's response is then translated back to the selected language and displayed.

4. **Chat History**  
   - The user can see the conversation history and download it as a `.txt` file.

---

## 🛠 System Requirements

### Dependencies
- **Python 3.8+**
- Libraries:
  - `streamlit`
  - `openai`
  - `deep_translator`
  - `dotenv`
- Hardware: **CPU** (No GPU required)

---

## 💬 Example

**User (English):**  
_"How does the weather affect airplanes?"_

**DeepSeek (English):**  
_"Weather conditions, such as wind speed and visibility, significantly impact flight safety and efficiency. Pilots rely on weather data for route planning and adjustments during flight."_

---

## 📋 Code Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/deepseek-chatbot.git
   cd deepseek-chatbot

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
