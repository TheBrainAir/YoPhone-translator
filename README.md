# YoAI Translation Bot

The YoAI Translation Bot is a Flask-based application that integrates with the YoAI messaging platform to translate user messages into their preferred language. It decodes base64-encoded messages, translates them using the Deep Translator library, and sends the translated text back to the user. The bot supports various commands to start the interaction, switch languages, and request help.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Error Handling](#error-handling)
- [Logging](#logging)
- [Contact](#contact)

---

## Features

- **Real-time Translation**  
  Automatically translates incoming base64-encoded messages into the user’s chosen language (default is Armenian, code `hy`).

- **Dynamic Language Switching**  
  Users can switch their translation language on the fly using the `/switch` command.

- **Command Support**  
  - `/start` – Starts the bot and displays a welcome message with instructions.
  - `/switch` – Prompts the user to change the translation language.
  - `/help` – Provides a list of available commands and usage details.

- **Robust Error Handling**  
  Gracefully handles decoding errors, unsupported languages, and connection issues with clear error messages.

- **Detailed Logging**  
  Logs every step of the process, including incoming messages, translation results, and errors for easier debugging.

---

## Requirements

- Python 3.8 or later
- Flask
- Requests
- Deep Translator

Install the required packages using:

```bash
pip install -r requirements.txt
```

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/yoai-translation-bot.git
   cd yoai-translation-bot
   ```

2. **Configure Your API Key**  
   Open the source code (`app.py`) and replace `yourapikeyhere` with your actual YoAI API key:
   ```python
   YOAI_API_KEY = "yourapikeyhere"
   ```

3. **Run the Application**  
   Start the Flask server by running:
   ```bash
   python app.py
   ```

---

## Usage

After launching the bot and integrating it with the YoAI messaging platform, you can interact with it as follows:

- **Message Translation**  
  Send a base64-encoded message to the bot. The bot will decode and translate the text into your set language (default is Armenian `hy` or the language you have specified).

- **Switching Languages**  
  - Send the `/switch` command.  
  - The bot will ask you to enter the desired language (e.g., "English", "Spanish").  
  - After receiving a valid language name, the bot updates your translation preferences.

- **Commands**
  - `/start` – Displays a welcome message with a brief description of the bot’s functionality.
  - `/switch` – Initiates the language change process.
  - `/help` – Lists all available commands with a short description of each.

---

## API Endpoints

1. **Webhook Endpoint**  
   Handles incoming messages:
   ```plaintext
   /yoai:yourapikeyhere
   ```

   Processes incoming POST requests by decoding, translating, and responding to the message.

2. **Catch-All Endpoint**  
   Handles all undefined POST routes:
   ```plaintext
   /<path:path>
   ```

   Logs any unhandled paths and returns a generic response.

---

## Error Handling

The bot includes comprehensive error handling for various scenarios:

- **Decoding Errors**  
  If the bot fails to decode the base64-encoded message, it sends an error message to the user and logs the error.

- **Unsupported Language**  
  When a user enters an unsupported or unrecognized language during the switch process, the bot prompts them to try again with a valid language.

- **Connection and HTTP Errors**  
  The bot handles timeouts, connection issues, and other HTTP errors gracefully by notifying the user of the issue and logging the error details.

---

## Logging

Logging is configured at the INFO level by default. The logs include:

- All incoming messages and user commands.
- Translation processing and results.
- Any errors or exceptions that occur during runtime.

These logs help monitor the bot’s performance and troubleshoot issues.

---

## Contact

For questions, suggestions, or feedback, please contact:

- **GitHub:** [TheBrainAir](https://github.com/TheBrainAir)  
- **Telegram:** [@TheBrainA1r](https://t.me/TheBrainA1r)  
