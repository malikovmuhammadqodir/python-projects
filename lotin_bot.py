from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '1705628355:AAFCl5dLUS3fowYh08on9bT3vP3RrwGUqi0'
bot = telebot.TeleBot(token=TOKEN,parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # username = message.from_user.username
    answer = 'Salom xush kelibsiz!'
    answer += '\nMatnni kirting: '
    bot.reply_to(message,answer)


@bot.message_handler(func=lambda message:True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg) 
    bot.reply_to(message, javob)       




bot.polling()       




# matn = input("Matni kirting: ")
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))     


# import telebot
# from transliterate import to_cyrillic, to_latin

# TOKEN = "1705628355:AAFCl5dLUS3fowYh08on9bT3vP3RrwGUqi0" #<-- Tokeningizni shu yerga yozing
# bot = telebot.TeleBot(token=TOKEN)

# # \start komandasi uchun mas'ul funksiya
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     username = message.from_user.username # Bu usul bilan foydalanuvchi nomini olishimiz mumkin
#     xabar = f'Assalom alaykum, {username} Kirill-Lotin-Kirill botiga xush kelibsiz!'
#     xabar += '\nMatningizni yuboring.'
#     bot.reply_to(message, xabar)

# # matnlar uchun mas'ul funksiya
# @bot.message_handler(func=lambda msg: msg.text is not None)
# def translit(message):
#     msg = message.text
#     javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
#     bot.reply_to(message, javob(msg))
    

# bot.polling()