import telebot
from PIL import Image
import io

BOT_TOKEN = "7321337959:AAHM8nTNagxjoEva5I6Yg6eLijZV1daiDj4"

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start'])

def handler_message(message):
    bot.reply_to(message, "This bot can resize image to 3x4")

@bot.message_handler(content_types=['photo'])

def handle_photo(message):
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        image = Image.open(io.BytesIO(downloaded_file))

        resized_image = image.resize((300, 400))

        bio = io.BytesIO()
        bio_name = "resized_image_jpg"
        resized_image.save(bio, "JPEG")
        bio.seek(0)

        bot.send_photo(message.chat.id, bio)
    except Exception as q:
        bot.reply_to(message, "An error occurred while processing the image.")

bot.polling()