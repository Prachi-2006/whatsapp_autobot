# WhatsApp AI Voice Responder with Gemini & Clipboard Automation

This Python project automates WhatsApp Web replies using voice commands or Gemini AI. It:
- Copies the latest message from a chat
- Speaks the message aloud
- Waits for a voice reply or generates a response using Gemini AI
- Sends the reply via WhatsApp

---

##  Features

-  Clipboard automation using PyAutoGUI
-  Voice recognition via Google Web Speech API
-  AI-powered responses using Gemini (Google Generative AI)
-  Text-to-speech (TTS) with pyttsx3
-  Cross-platform clipboard access (Windows, macOS, Linux)

---

## Requirements

Install required packages:

```bash
pip install pyautogui pyttsx3 SpeechRecognition google-generativeai
```
---

## Platform-specific clipboard tools:
- *Windows*: Uses Powershell

- *macOS*: Uses pbcopy / pbpaste

- *Linux*: Requires xclip installed
---
## Gemini API Key
Update this line with your real API key:
```
genai.configure(api_key="YOUR_API_KEY_HERE")
```
##  Key Functions Explained

### | Function    :-   Description 
- **mspeak(text)**        :-Uses pyttsx3 to speak text out loud
- **get_clipboard_text()** :-Retrieves text from the system clipboard based on OS
- **clear_clipboard()**	:- Clears the current clipboard content
- **copy_to_clipboard(text)**	:-Copies the given text to clipboard
- **ask_gemini(prompt**) :-Sends a prompt to Gemini and returns the AI response
- **send_whatsapp_message(message)**	:-Pastes the message into WhatsApp and presses Enter
- **listen_for_voice_reply(timeout=10)** :-	Listens to mic input and converts it to text using Google Speech Recognition
- **open_whatsapp()** :-	Opens WhatsApp Web in the default browser
- **get_copied_chat_message()** :-	Automates mouse and keyboard to select and copy the latest WhatsApp message
- **main()** :-Main program flow: opens WhatsApp, reads last message, listens or generates reply, and sends it
---
##  How It Works

1. Opens WhatsApp Web

2. Clicks on a chat and selects the most recent message

3. Speaks the message aloud using TTS

4. Waits for a spoken reply; if none is heard, uses Gemini AI

5. Sends the reply automatically
---
## GUI Automation Setup
Coordinates in get_copied_chat_message() are screen-specific:
```
pyautogui.click(446, 659) 
pyautogui.moveTo(674, 207)
pyautogui.dragTo(1692, 937, duration=1.5)
```
Use this to find your own:
```
pyautogui.position()
```
---
##  Running the Script
- You're logged in to https://web.whatsapp.com

- Chat positioning matches the configured screen coordinates
---

## Example Workflow
-  Message: "What time is the meeting?"

-  Bot: "You got a message: What time is the meeting? Do you want to reply?"

-  You: "It's at 3 PM."

- Script sends: "It's at 3 PM."

If no voice is detected, Gemini might reply with:

- "The meeting is at 3 PM today."
---
##  License

This project is licensed under the MIT License – see the [LICENSE](LICENSE.txt) file for details
