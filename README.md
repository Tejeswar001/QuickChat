# QuickChat

QuickChat is a lightweight, Python-based AI chat application powered by Google Gemini.  
It provides a clean conversational interface using Gradio and logs all conversations into Google Sheets for lightweight persistence.

The project avoids local or cloud model hosting while still delivering modern AI responses through a stable external API.

---

## Features

- AI-powered responses using Google Gemini  
- Python-only user interface built with Gradio  
- Automatic logging of chat messages to Google Sheets  
- Secure API key handling using .env  
- Quick to set up and easy to deploy  
- No local or cloud model hosting required  

---

## Architecture Overview

User Browser  
→ Gradio UI (Python)  
→ Gemini API (LLM)  
→ Google Sheets (Logging)

---

## Tech Stack

UI: Gradio  
LLM: Google Gemini API  
Backend: Python  
Storage: Google Sheets API  
Secrets: python-dotenv  

---

## Project Structure

QuickChat/
├── app.py  
├── gemini_client.py  
├── sheets_logger.py  
├── requirements.txt  
├── .env  
├── credentials.json  
└── .gitignore  

---

## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/Tejeswar001/QuickChat.git  
cd QuickChat  

---

### 2. Create Virtual Environment

python -m venv venv  
source venv/bin/activate  

(Windows)  
venv\Scripts\activate  

---

### 3. Install Dependencies

pip install -r requirements.txt  

---

### 4. Get Gemini API Key

Go to:  
https://aistudio.google.com/app/apikey  

Create a new API key.

Create a .env file in the project root:

GEMINI_API_KEY=your_gemini_key_here  

---

### 5. Set Up Google Sheets Logging

1. Create a project in Google Cloud Console  
2. Enable Google Sheets API  
3. Create a Service Account  
4. Generate a JSON key  
5. Save it as credentials.json  
6. Create a Google Sheet named QuickChatLogs  
7. Share the sheet with your service account email (Editor access)  

---

### 6. Run the Application

python3 app.py  

Open in browser:  
http://127.0.0.1:7860  

---

## Google Sheets Logging Format

Each chat exchange is stored as:

Timestamp | User Message | Bot Reply  

---

## Security Notes

- .env and credentials.json are excluded via .gitignore  
- Never commit API keys or credentials  
- Regenerate keys if exposed  

---

## Common Issues

Gemini 404 Error  
Use model name:  
models/gemini-1.5-flash-latest  

Gemini 403 Error  
Ensure Gemini API is enabled  
Check API key validity  

Google Sheets 403 Error  
Share the sheet with the service account email  
Enable Google Sheets API in Cloud Console  

---

## Future Enhancements

- Per-user session logging  
- Chat export to CSV  
- Chat history search  
- UI theming controls  
- Multi-model support  

---

## License

This project is intended for academic and demonstration purposes only.

---

## Acknowledgements

Google Gemini API  
Gradio  
Google Sheets API  
