# Gemini Pro ChatBot on Flet

## Description
This Python script is a simple chatbot application built with the [Flet library](https://flet.dev/). It allows users to enter messages and receive responses from an AI language model via an API call to Google Cloud's Generative Language API.

The main features include:

- Interactive chat interface: Users can send messages, and the bot responds using AI.
- Clipboard controls: Options to select, copy, and paste messages within the chat. 
- API integration: Securely accesses the API key from a .env file for authentication.

This script is designed for ease of use, enabling smooth, real-time conversations with an AI assistant.
## Setup

### Prerequisites
1. **Google Cloud API Key**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Navigate to **APIs & Services** > **Credentials**.
   - Click on **Create credentials** and select **API key**.
   - Copy your API key.

2. **Add the API Key to `.env`**:
   - In the project root directory, create a `.env` file.
   - Add the following line to the `.env` file:
     ```plaintext
     API_KEY=YOUR_GOOGLE_CLOUD_API_KEY_HERE
     ```

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/rafraf-porrot/gemini-on-flet
    ```
2. Navigate to the project directory:
    ```bash
    cd gemini-on-flet
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Run the application with:
```bash
python main.py

Notes
Ensure your .env file is set up with the correct API key to avoid authentication errors.
