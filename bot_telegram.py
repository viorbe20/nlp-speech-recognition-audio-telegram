import os
from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters
from dotenv import load_dotenv
from pydub import AudioSegment

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# check if token
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("No se encontró el token del bot de Telegram. Asegúrate de configurarlo en el archivo .env.")

def get_voice(update: Update, context: CallbackContext) -> None:
    new_file = context.bot.get_file(update.message.voice.file_id)

    # Get original file number
    original_file_name = new_file.file_path.split("/")[-1]

    # Path configuration and download
    audios_directory = os.path.join(os.path.dirname(__file__), 'audios')
    os.makedirs(audios_directory, exist_ok=True)
    file_path = os.path.join(audios_directory, original_file_name)
    new_file.download(file_path)

    # Conversion to WAV format
    wav_file_path = os.path.splitext(file_path)[0] + '.wav'
    audio = AudioSegment.from_file(file_path)
    audio.export(wav_file_path, format='wav')

    update.message.reply_text(f'Se ha guardado la nota de voz {original_file_name})')

# Represents the main interface for the bot  
updater = Updater(TELEGRAM_BOT_TOKEN)

#  Adds a message handler to the Telegram bot's dispatcher
updater.dispatcher.add_handler(MessageHandler(Filters.voice , get_voice))

# Establishes a connection with Telegram servers and starts receiving updates. 
# # The bot will be waiting for new messages and events
updater.start_polling()

# Puts the bot in a continuous loop, listening and handling Telegram updates. 
updater.idle()