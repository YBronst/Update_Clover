import datetime
import json
import os
from config import LOGFILE, RED, GREEN, YELLOW, NC, SCRIPT_DIR
import locale

translations = {}  # Global dictionary to store translations

def get_system_language():
    """Gets the preferred language of the operating system."""
    try:
        # Gets the system locale and encoding
        system_locale = locale.getdefaultlocale()
        if system_locale[0]:
            # Returns the language code (e.g., 'ru_RU', 'en_US')
            return system_locale[0].split('_')[0]  # Returns only the main code (ru, en, pt, etc.)
        else:
            # Returns None if unable to detect the language
            return None
    except Exception as e:
        logger("error_getting_system_language", RED, error=e)
        return None

def load_translations(language=None):
    """Loads translations from a JSON file."""
    global translations
    if not language:
        language = get_system_language() or "en"  # Uses English as default if detection fails

    translations_path = os.path.join(SCRIPT_DIR, "translations")
    print(f"Trying to load translations from: {translations_path}/{language}.json")
    try:
        with open(f"{translations_path}/{language}.json", "r", encoding="utf-8") as f:
            translations = json.load(f)
        logger(f"Translations successfully loaded for language: {language}", GREEN)
    except FileNotFoundError:
        logger("translation_file_not_found", RED, language=language)
        # Loads the default language (English) if translation file is missing
        if language != "en":
            load_translations("en")
    except json.JSONDecodeError:
        logger("json_decode_error", RED, language=language)

def logger(message_key, color=None, return_message=False, **kwargs):
    """Logs messages to console and to a file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    color_prefix = color if color else ""
    color_suffix = NC if color else ""

    # Gets the translated message or uses the key as fallback
    message = translations.get(message_key, message_key)

    # Formats the message with named parameters, if any
    try:
        message = message.format(**kwargs)
    except KeyError as e:
        logger("formatting_key_not_found", RED, key=e, message_key=message_key)
        return None

    log_message = f"[{timestamp}] {color_prefix}{message}{color_suffix}"

    if not return_message:
        print(log_message)
        with open(LOGFILE, "a", encoding="utf-8") as log_file:
            log_file.write(log_message + "\n")

    return message if return_message else log_message
