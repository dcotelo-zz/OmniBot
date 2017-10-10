import os
import telebot
import re

bot = telebot.TeleBot('token')
@bot.message_handler(content_types=['text'])
def Process(message):
    print(message)   
    if re.findall("(?P<url>https?://[^\s]+)", message.text):
      URL = re.findall("(?P<url>https?://[^\s]+)", message.text)
      #bot.send_message("@get", "Url Detected", parse_mode="HTML")
      bot.reply_to(message, u"Url Detected " + URL[0])    
    elif message.text == "/quien" :
      bot.reply_to(message, u"Tu vieja! @" + message.from_user.username)
    elif message.text == "/comandos" :
      bot.reply_to(message, u"comandos disponibles /quien /ayuda /comandos")
    elif message.text == "/ayuda":
      bot.reply_to(message, u"Bot troll official H&B, originalmente destinado a salvaguardar los links compartidos. La leyenda cuenta que adquirio vida pripia y comparte cosas ya discutidas en GG solo para molestar a Enrique")
bot.polling()

