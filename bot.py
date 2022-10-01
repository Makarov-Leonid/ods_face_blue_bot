import os
import urllib

import telebot

from dotenv import load_dotenv

from config import result_storage_path
from init import init
from recognition import blur_image

load_dotenv(dotenv_path='.env')
TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)
detector = init()


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help" or message.text == "/start":
        bot.send_message(message.from_user.id,
                         "Чтобы воспользоваться ботом пришлите ему картинку, в ответ вы получите анонимизированное изображение.")
    else:
        bot.send_message(message.from_user.id, "Я вас не понимаю. Напиши /help.")


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    cid = message.chat.id

    image_name = save_image_from_message(message)
    bot.send_message(cid, 'Отлично, ваше изображение обрабатывается, подождите пару мнгновений')
    image_name_new = handle_image(image_name)
    bot.send_photo(message.chat.id, open('{0}/{1}'.format(result_storage_path, image_name_new), 'rb'),
                   'Ура, получилось!')
    cleanup_remove_images(image_name, image_name_new)


def save_image_from_message(message):
    image_id = get_image_id_from_message(message)
    file_path = bot.get_file(image_id).file_path
    image_url = "https://api.telegram.org/file/bot{0}/{1}".format(TOKEN, file_path)

    if not os.path.exists(result_storage_path):
        os.makedirs(result_storage_path)

    image_name = "{0}.jpg".format(image_id)
    urllib.request.urlretrieve(image_url, "{0}/{1}".format(result_storage_path, image_name))

    return image_name


def get_image_id_from_message(message):
    return message.photo[len(message.photo) - 1].file_id


def handle_image(image_name):
    return blur_image(detector=detector, filepath=os.path.join(result_storage_path, image_name), filename=image_name)


def cleanup_remove_images(image_name, image_name_new):
    os.remove('{0}/{1}'.format(result_storage_path, image_name))
    os.remove('{0}/{1}'.format(result_storage_path, image_name_new))


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
