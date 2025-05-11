
# import pyautogui
# import time
# import platform
# import subprocess
# import webbrowser
# import google.generativeai as genai
# import speech_recognition as sr
# import pyttsx3

# # Configure Gemini API
# genai.configure(api_key  # Replace with your actual key

# # Initialize text-to-speech engine
# engine = pyttsx3.init()
# engine.setProperty('rate', 170)  # Set speaking rate

# # Speak text aloud
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# # Retrieve text from the system clipboard
# def get_clipboard_text():
#     try:
#         if platform.system() == "Windows":
#             return subprocess.check_output("powershell Get-Clipboard", universal_newlines=True).strip()
#         elif platform.system() == "Darwin":  # macOS
#             return subprocess.check_output("pbpaste", universal_newlines=True).strip()
#         else:  # Linux
#             return subprocess.check_output("xclip -selection clipboard -o", shell=True, universal_newlines=True).strip()
#     except Exception as e:
#         print(" Clipboard read error:", e)
#         return ""

# # Clear the system clipboard
# def clear_clipboard():
#     copy_to_clipboard("")

# # Copy the specified text to the clipboard
# def copy_to_clipboard(text):
#     try:
#         if platform.system() == "Windows":
#             subprocess.run("clip", universal_newlines=True, input=text, text=True)
#         elif platform.system() == "Darwin":
#             subprocess.run("pbcopy", universal_newlines=True, input=text, text=True)
#         else:
#             subprocess.run(['xclip', '-selection', 'clipboard'], input=text.encode())
#     except Exception as e:
#         print(" Clipboard copy error:", e)

# # Generate a response using Gemini AI
# def ask_gemini(prompt):
#     try:
#         model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
#         response = model.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         print(" Gemini error:", e)
#         return ""

# # Paste message in WhatsApp chat and send
# def send_whatsapp_message(message):
#     copy_to_clipboard(message)
#     time.sleep(1)
#     pyautogui.hotkey('command' if platform.system() == 'Darwin' else 'ctrl', 'v')
#     time.sleep(1)
#     pyautogui.press('enter')
#     print(" Message sent!")

# # Listen for user's voice input and convert to text
# def listen_for_voice_reply(timeout=10):
#     r = sr.Recognizer()
#     mic = sr.Microphone()
#     with mic as source:
#         print(" Listening for voice reply...")
#         r.adjust_for_ambient_noise(source)
#         try:
#             audio = r.listen(source, timeout=timeout)
#             return r.recognize_google(audio)
#         except Exception as e:
#             print(" Voice recognition error:", e)
#             return None

# # Open WhatsApp Web in browser
# def open_whatsapp():
#     speak("Opening WhatsApp, please wait.")
#     webbrowser.open("https://web.whatsapp.com")
#     time.sleep(10)  # Wait for WhatsApp to fully load

# # Use PyAutoGUI to select and copy the most recent chat message
# def get_copied_chat_message():
#     speak("Copying the latest chat message...")

#     # Step 1: Click on chat (coordinates may need adjustment per screen)
#     pyautogui.click(363, 428)
#     time.sleep(2)

#     # Step 2: Clear clipboard
#     clear_clipboard()

#     # Step 3: Drag to select latest message
#     pyautogui.moveTo(674, 207)
#     pyautogui.dragTo(1906, 925, duration=1.5, button='left')
#     # pyautogui.click(1906, 925)
#     time.sleep(0.5)

#     # Step 4: Copy the message
#     pyautogui.hotkey('command' if platform.system() == 'Darwin' else 'ctrl', 'c')
#     time.sleep(1.5)

#     # Step 5: Get new clipboard content
#     message = get_clipboard_text()
#     return message

# # Main function to run the WhatsApp automation process
# def main():
#     open_whatsapp()
#     print(" Waiting to grab message...")
#     time.sleep(2)

#     # Get message from chat
#     user_text = get_copied_chat_message()
#     if not user_text:
#         print(" No message copied.")
#         return

#     print(f" Message: {user_text}")
#     speak(f"You got a message: {user_text}. Do you want to reply?")

#     # Listen for a voice reply from the user
#     voice_reply = listen_for_voice_reply(timeout=10)
#     if voice_reply:
#         print("You said:", voice_reply)
#         send_whatsapp_message(voice_reply)
#     else:
#         # If no voice, fallback to Gemini AI
#         print("Getting AI reply...")
#         ai_reply = ask_gemini(f"Reply to this message: {user_text}")
#         if ai_reply:
#             send_whatsapp_message(ai_reply)
#         else:
#             print("Gemini returned nothing.")

# # Run the script
# if __name__ == "__main__":
#     main()

# cd "C:\Users\prach\OneDrive\Desktop\whatsapp_autobot"

# import pyautogui
# import time
# import platform
# import subprocess
# import webbrowser
# import google.generativeai as genai
# import speech_recognition as sr
# import pyttsx3

# #  Configure Gemini
# genai.configure(api_key="")  # Replace with your actual key

# #  Init TTS
# engine = pyttsx3.init()
# engine.setProperty('rate', 170)

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def get_clipboard_text():
#     try:
#         if platform.system() == "Windows":
#             return subprocess.check_output("powershell Get-Clipboard", universal_newlines=True).strip()
#         elif platform.system() == "Darwin":
#             return subprocess.check_output("pbpaste", universal_newlines=True).strip()
#         else:
#             return subprocess.check_output("xclip -selection clipboard -o", shell=True, universal_newlines=True).strip()
#     except Exception as e:
#         print(" Clipboard read error:", e)
#         return ""

# def clear_clipboard():
#     copy_to_clipboard("")

# def copy_to_clipboard(text):
#     try:
#         if platform.system() == "Windows":
#             subprocess.run("clip", universal_newlines=True, input=text, text=True)
#         elif platform.system() == "Darwin":
#             subprocess.run("pbcopy", universal_newlines=True, input=text, text=True)
#         else:
#             subprocess.run(['xclip', '-selection', 'clipboard'], input=text.encode())
#     except Exception as e:
#         print(" Clipboard copy error:", e)

# def ask_gemini(prompt):
#     try:
#         model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
#         response = model.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         print(" Gemini error:", e)
#         return ""

# def send_whatsapp_message(message):
#     copy_to_clipboard(message)
#     time.sleep(1)
#     pyautogui.hotkey('command' if platform.system() == 'Darwin' else 'ctrl', 'v')
#     time.sleep(1)
#     pyautogui.press('enter')
#     print(" Message sent!")

# def listen_for_voice_reply(timeout=10):
#     r = sr.Recognizer()
#     mic = sr.Microphone()
#     with mic as source:
#         print(" Listening for voice reply...")
#         r.adjust_for_ambient_noise(source)
#         try:
#             audio = r.listen(source, timeout=timeout)
#             return r.recognize_google(audio)
#         except Exception as e:
#             print(" Voice recognition error:", e)
#             return None

# def open_whatsapp():
#     speak("Opening WhatsApp, please wait.")
#     webbrowser.open("https://web.whatsapp.com")
#     time.sleep(10)

# def get_copied_chat_message():
#     speak("Copying the latest chat message...")

#     # Step 1: Click on chat
#     pyautogui.click(363, 428)
#     time.sleep(2)

#     # Step 2: Clear clipboard
#     clear_clipboard()

#     # Step 3: Drag to select latest message
#     pyautogui.moveTo(674, 207)
#     pyautogui.dragTo(1906, 925, duration=1.5, button='left')
#     pyautogui.click(1906, 925)
#     time.sleep(0.5)

#     # Step 4: Copy the message
#     pyautogui.hotkey('command' if platform.system() == 'Darwin' else 'ctrl', 'c')
#     time.sleep(1.5)

#     # Step 5: Get new clipboard content
#     message = get_clipboard_text()
#     return message

# def main():
#     open_whatsapp()
#     print(" Waiting to grab message...")
#     time.sleep(2)

#     user_text = get_copied_chat_message()
#     if not user_text:
#         print(" No message copied.")
#         return

#     print(f" Message: {user_text}")
#     speak(f"You got a message: {user_text}. Do you want to reply?")

#     voice_reply = listen_for_voice_reply(timeout=10)
#     if voice_reply:
#         print("You said:", voice_reply)
#         send_whatsapp_message(voice_reply)
#     else:
#         print("Getting AI reply...")
#         ai_reply = ask_gemini(f"Reply to this message: {user_text}")
#         if ai_reply:
#             send_whatsapp_message(ai_reply)
#         else:
#             print("Gemini returned nothing.")

# if __name__ == "__main__":
#     main()

import pyautogui
import time
import platform
import subprocess
import webbrowser
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

#  Configure Gemini
genai.configure(api_key="AIzaSyCd60fpmrPepGyAEsgbFpIaBEKPrHH0TEg")  # Replace with your actual key

#  Init TTS
engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_clipboard_text():
    try:
        if platform.system() == "Windows":
            return subprocess.check_output("powershell Get-Clipboard", universal_newlines=True).strip()
        elif platform.system() == "Darwin":
            return subprocess.check_output("pbpaste", universal_newlines=True).strip()
        else:
            return subprocess.check_output("xclip -selection clipboard -o", shell=True, universal_newlines=True).strip()
    except Exception as e:
        print(" Clipboard read error:", e)
        return ""

def clear_clipboard():
    copy_to_clipboard("")

def copy_to_clipboard(text):
    try:
        if platform.system() == "Windows":
            subprocess.run("clip", universal_newlines=True, input=text, text=True)
        elif platform.system() == "Darwin":
            subprocess.run("pbcopy", universal_newlines=True, input=text, text=True)
        else:
            subprocess.run(['xclip', '-selection', 'clipboard'], input=text.encode())
    except Exception as e:
        print(" Clipboard copy error:", e)

def ask_gemini(prompt):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(" Gemini error:", e)
        return ""

def send_whatsapp_message(message):
    copy_to_clipboard(message)
    time.sleep(1)
    pyautogui.hotkey('command' if platform.system() == 'Darwin' else 'ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    print(" Message sent!")

def listen_for_voice_reply(timeout=10):
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print(" Listening for voice reply...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=timeout)
            return r.recognize_google(audio)
        except Exception as e:
            print(" Voice recognition error:", e)
            return None

def open_whatsapp():
    speak("Opening WhatsApp, please wait.")
    webbrowser.open("https://web.whatsapp.com")
    time.sleep(10)

def get_copied_chat_message():
    speak("Copying the latest chat message...")

    # Step 1: Click on chat
    pyautogui.click(446, 659)
    time.sleep(2)

    # Step 2: Clear clipboard
    clear_clipboard()

    # Step 3: Drag to select latest message
    pyautogui.moveTo(674, 207)
    pyautogui.dragTo(1692, 937, duration=1.5, button='left')
    time.sleep(0.5)

    # Step 4: Copy the message
    pyautogui.hotkey('command' if platform.system() == 'Darwin' else 'ctrl', 'c')
    time.sleep(1.5)

    # Step 5: Get new clipboard content
    message = get_clipboard_text()
    return message

def main():
    open_whatsapp()
    print(" Waiting to grab message...")
    time.sleep(2)

    user_text = get_copied_chat_message()
    if not user_text:
        print(" No message copied.")
        return

    print(f" Message: {user_text}")
    speak(f"You got a message: {user_text}. Do you want to reply?")

    voice_reply = listen_for_voice_reply(timeout=10)
    if voice_reply:
        print(" You said:", voice_reply)
        send_whatsapp_message(voice_reply)
    else:
        print(" Getting AI reply...")
        ai_reply = ask_gemini(f"Reply to this message: {user_text}")
        if ai_reply:
            send_whatsapp_message(ai_reply)
        else:
            print(" Gemini returned nothing.")

if __name__ == "__main__":
    main()
