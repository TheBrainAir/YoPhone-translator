from flask import Flask, request, jsonify
import requests
import base64
import logging
from deep_translator import GoogleTranslator, exceptions

app = Flask(__name__)

YOAI_API_KEY = "yourapikeyhere"


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

default_language = "hy"  
user_languages = {}  
user_states = {}     

def send_message(chat_id, text):
    url = "https://yoai.yophone.com/api/pub/sendMessage"
    headers = {
        "Content-Type": "application/json",
        "X-YoAI-API-Key": YOAI_API_KEY
    }
    payload = {
        "to": chat_id,
        "text": text
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        logger.info(f"Message successfully sent to user {chat_id}: {response.json()}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred while sending message to {chat_id}: {http_err}")
        send_message(chat_id, "Error: Unable to send message due to server issues.")
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        send_message(chat_id, "Error: Could not connect to the server. Please try again later.")
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error: {timeout_err}")
        send_message(chat_id, "Error: The request timed out. Please try again later.")
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
        send_message(chat_id, "Error: An unexpected error occurred. Please try again.")

def get_language_code(language_name):
    try:
        translator = GoogleTranslator()
        supported_languages = translator.get_supported_languages(as_dict=True)
        return supported_languages.get(language_name.lower())
    except Exception as e:
        logger.error(f"Error fetching language code: {e}")
        return None

def translate_text(text, target_language):
    try:
        translator = GoogleTranslator(source='auto', target=target_language.lower())
        return translator.translate(text)
    except exceptions.LanguageNotSupportedException:
        logger.error(f"Language '{target_language}' is not supported.")
        return "Error: The selected language is not supported."
    except exceptions.NotValidPayload:
        logger.error("Invalid text format for translation.")
        return "Error: Invalid text format."
    except Exception as e:
        logger.error(f"Unknown translation error: {e}")
        return "Error during translation."

@app.route('/yoai:yourapikeyhere', methods=['POST'])
def webhook():
    data = request.json
    logger.info(f"Received data: {data}")

    chat_id = data.get("chatId") or data.get("chat_id") or data.get("id")
    if not chat_id:
        logger.error("chat_id not found in received data.")
        return jsonify({"error": "chat_id not found"}), 400

    encoded_text = data.get("text")
    if not encoded_text:
        logger.error(f"Text not found in received data for chat_id {chat_id}.")
        return jsonify({"error": "Invalid data"}), 400

    try:
        decoded_bytes = base64.b64decode(encoded_text)
        decoded_text = decoded_bytes.decode('utf-8').strip()
        logger.info(f"Decoded message from {chat_id}: {decoded_text}")
    except (base64.binascii.Error, UnicodeDecodeError) as e:
        logger.error(f"Decoding error for chat_id {chat_id}: {e}")
        send_message(chat_id, "Failed to decode your message. Please try again.")
        return jsonify({"error": "Decoding failed"}), 400

    if user_states.get(chat_id) == 'awaiting_language':
        language_code = get_language_code(decoded_text)
        if language_code:
            user_languages[chat_id] = language_code
            user_states.pop(chat_id)
            confirmation_message = f"Translation language set to {decoded_text.capitalize()}."
            send_message(chat_id, confirmation_message)
            logger.info(f"User {chat_id} set translation language: {language_code}.")
        else:
            error_message = "Sorry, I couldn't recognize this language. Please try again."
            send_message(chat_id, error_message)
            logger.warning(f"Unknown language '{decoded_text}' from user {chat_id}.")
        return jsonify({"status": "ok"}), 200

    if decoded_text.startswith('/'):
        command = decoded_text[1:].lower()
        logger.info(f"Command '{command}' received from user {chat_id}.")

        if command == "start":
            welcome_message = (
                "Welcome! I can translate your messages.\n\n"
                "Commands:\n"
                "/switch - Change the translation language.\n"
                "/help - Show this message.\n"
                "Just type any message, and I will translate it."
            )
            send_message(chat_id, welcome_message)
            return jsonify({"status": "ok"}), 200

        elif command == "switch":
            switch_message = (
                "Please enter the language you want to translate to (e.g., 'English', 'Spanish')."
            )
            send_message(chat_id, switch_message)
            user_states[chat_id] = 'awaiting_language'
            logger.info(f"Awaiting language input from user {chat_id}.")
            return jsonify({"status": "ok"}), 200

        elif command == "help":
            help_message = (
                "Here are the available commands:\n"
                "/start - Start using the bot and see the welcome message.\n"
                "/switch - Change the translation language.\n"
                "/help - Show this message."
            )
            send_message(chat_id, help_message)
            return jsonify({"status": "ok"}), 200

        else:
            unknown_command_message = "Unknown command. Type /help to see available commands."
            send_message(chat_id, unknown_command_message)
            logger.warning(f"Unknown command '{command}' from user {chat_id}.")
            return jsonify({"status": "ok"}), 200

    target_language = user_languages.get(chat_id, default_language)
    logger.info(f"Translating message from {chat_id} to '{target_language}'.")

    translated_text = translate_text(decoded_text, target_language)
    logger.info(f"Translated message for {chat_id}: {translated_text}")

    send_message(chat_id, translated_text)

    return jsonify({"status": "ok"}), 200

@app.route('/<path:path>', methods=['POST'])
def catch_all(path):
    data = request.json
    logger.warning(f"Unhandled path: {path}")
    logger.warning(f"Received data: {data}")
    return jsonify({"status": "Unhandled path"}), 200

if __name__ == "__main__":
    app.run()
