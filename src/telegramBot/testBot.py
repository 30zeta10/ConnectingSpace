import telegram.ext
from telegram.ext import Updater

tk = '429693526:AAHEIzq1yT5mK8DV1ngve2DbfAP3kKL_psM'
bot = telegram.Bot(token=tk)
chat_id = bot.getUpdates()[-1].message.chat_id

print(chat_id)
bot.sendAudio(chat_id=chat_id, audio=open('testsound.mp3'))

update = Updater(token=tk)
dispatcher = update.dispatcher


