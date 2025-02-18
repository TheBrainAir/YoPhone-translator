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
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Real-time Translation:**  
  Automatically translates incoming base64-encoded messages into the user’s chosen language (default is Armenian, code `hy`).

- **Dynamic Language Switching:**  
  Users can switch their translation language on the fly using the `/switch` command.

- **Command Support:**  
  - `/start` – Starts the bot and displays a welcome message with instructions.
  - `/switch` – Prompts the user to change the translation language.
  - `/help` – Provides a list of available commands and usage details.

- **Robust Error Handling:**  
  Gracefully handles issues such as decoding errors, unsupported languages, and connection problems by providing clear error messages.

- **Detailed Logging:**  
  Logs every step of the process including incoming messages, translation results, and errors for easier debugging and monitoring.

## Requirements

- Python 3.8 or later
- [Flask](https://flask.palletsprojects.com/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [Deep Translator](https://github.com/nidhaloff/deep-translator)

Install the required packages using:

```bash
pip install -r requirements.txt

Installation
	1.	Clone the Repository:

git clone https://github.com/your-username/yoai-translation-bot.git
cd yoai-translation-bot


	2.	Configure Your API Key:
Open the source code and replace yourapikeyhere with your actual YoAI API key:

YOAI_API_KEY = "yourapikeyhere"  # Replace with your real API key


	3.	Run the Application:
Start the Flask server by running:

python app.py



Usage

After launching the bot and integrating it with the YoAI messaging platform, you can interact with it as follows:
	•	Message Translation:
	•	Send a base64-encoded message to the bot. The bot will decode and translate the text into your set language (default is Armenian hy or the language you have specified).
	•	Switching Languages:
	•	Send the /switch command. The bot will ask you to enter the desired language (e.g., “English”, “Spanish”).
	•	After receiving a valid language name, the bot updates your translation preferences.
	•	Commands:
	•	/start – Displays a welcome message along with a brief description of the bot’s functionality.
	•	/switch – Initiates the language change process.
	•	/help – Lists all available commands with a short description of each.

API Endpoints
	•	Webhook Endpoint:
The primary endpoint to handle incoming messages:

/yoai:yourapikeyhere

This endpoint processes incoming POST requests by decoding, translating, and responding to the message.

	•	Catch-All Endpoint:
Handles all other undefined POST routes:

/<path:path>

This endpoint logs any unhandled paths and returns a generic response.

Error Handling

The bot includes comprehensive error handling for various scenarios:
	•	Decoding Errors:
If the bot fails to decode the base64-encoded message, it sends an error message to the user and logs the error.
	•	Unsupported Language:
When a user enters an unsupported or unrecognized language during the switch process, the bot prompts them to try again with a valid language.
	•	Connection and HTTP Errors:
The bot handles timeouts, connection issues, and other HTTP errors gracefully by notifying the user of the issue and logging the error details.

Logging

Logging is configured at the INFO level by default. The logs include:
	•	All incoming messages and user commands.
	•	Translation processing and results.
	•	Any errors or exceptions that occur during runtime.

These logs help with monitoring the bot’s performance and troubleshooting issues.

Contributing

Contributions are welcome! To contribute:
	1.	Fork the Repository:
Click the “Fork” button on GitHub to create your own copy of the repository.
	2.	Create a New Branch:
Create a branch for your feature or bug fix:

git checkout -b feature/your-feature-name


	3.	Commit Your Changes:
Write clear and descriptive commit messages.
	4.	Submit a Pull Request:
Once your changes are complete, submit a pull request to the main repository with a detailed description of your changes.
