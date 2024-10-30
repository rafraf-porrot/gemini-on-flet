import flet as ft
import requests
import json
import threading
import os
from datetime import datetime
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("API_KEY")

# API endpoint
url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={api_key}"

# Headers
headers = {
    'Content-Type': 'application/json'
}

# Function to make API request
def get_answer(user_input):
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": user_input}
                ]
            }
        ]
    }

    # Send POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check response status and return the result
    if response.status_code == 200:
        result = response.json()
        bot_message = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No response")
        return bot_message
    else:
        return f"Error: {response.status_code}, {response.text}"

# Flet app logic
def main(page: ft.Page):
    # Input field and chat display
    def send_message(e):
        user_message = input_field.value
        input_field.value = ""

        # Get the current time
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Display user message with timestamp
        chat_display.controls.append(ft.Text(f"{timestamp} - User: {user_message}", selectable=True))
        loading_message = ft.Text(f"{timestamp} - Bot: Loading...", color="blue", selectable=True)
        chat_display.controls.append(loading_message)

        page.update()

        # Create a new thread to handle API request without blocking the UI
        def process_response():
            api_response = get_answer(user_message)
            chat_display.controls.remove(loading_message)

            # Get the current time for bot response
            bot_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Create a bot response with a copy button
            bot_response_text = ft.Text(f"{bot_timestamp} - Bot: {api_response}", selectable=True)
            copy_button = ft.IconButton(
                icon=ft.icons.COPY,
                on_click=lambda _: page.set_clipboard(api_response)
            )
            bot_response_row = ft.Row([bot_response_text, copy_button])

            chat_display.controls.append(bot_response_row)
            page.update()

            # Scroll to the bottom of the chat display
            page.scroll_to(chat_display)

        threading.Thread(target=process_response).start()

    input_field = ft.TextField(hint_text="Enter your message", expand=True)
    send_button = ft.ElevatedButton(text="Send", on_click=send_message)

    # Make chat_display scrollable
    chat_display = ft.Column(scroll="auto", expand=True)

    page.add(
        ft.Column(
            [
                ft.Row([input_field, send_button]),
                chat_display
            ],
            expand=True
        )
    )

# Run the Flet app
if __name__ == "__main__":
    ft.app(target=main)
