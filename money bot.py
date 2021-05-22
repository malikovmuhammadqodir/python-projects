
import telebot

token = "1592331230:AAHQP-uA0er_Ew023rnNeuQBB0jP08Od5pY"
from bs4 import BeautifulSoup
#url = "https://api.telegram.org/bot1592331230:AAHQP-uA0er_Ew023rnNeuQBB0jP08Od5pY/sendMessage?chat_id=717324646text=Salom"
import requests
from telebot import  types
bot = telebot.TeleBot(token)

user_info = {}

def course(valute):
	url = "https://bank.uz/currency"
	full_page = requests.get(url)
	soup = BeautifulSoup(full_page.content,"html.parser")
	convert = soup.findAll("span",{"class":"medium-text"})

	if valute == 'us':
		return convert[3].text.strip()
	else:
		return convert[6].text.strip()


key = types.InlineKeyboardMarkup(row_width=2)
btn = types.InlineKeyboardButton("Dollarni sumga 🇺🇸 🇺🇿", callback_data="us-uz")
btn2 = types.InlineKeyboardButton("Sumni dollarga 🇺🇿 🇺🇸", callback_data="uz-us")
btn3 = types.InlineKeyboardButton("Sumni rublga 🇺🇿 🇷🇺", callback_data="uz-ru")
btn4 = types.InlineKeyboardButton("Rublni sumga 🇷🇺 🇺🇿", callback_data="ru-uz")
key.add(btn,btn2,btn3,btn4)

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id ,"Salom men valyutalarni konvert qiluvchi botman\nKerakli funksiyani tanlang",reply_markup=key)


@bot.callback_query_handler(func = lambda call:True)
def callback_func(call):
	status = None
	if call.data == "us-uz":
		status = "us-uz"
	elif call.data == "uz-us":
		status = "uz-us"
	elif call.data == "uz-ru":
		status = "uz-ru"
	elif call.data == "ru-uz":
		status = "ru-uz"
	user_info[call.message.chat.id] = {}
	user_info[call.message.chat.id]['status'] = status
	bot.send_message(call.message.chat.id ,"Summani kiriting")
	print(user_info)	 

@bot.message_handler(content_types=['text'])
def text(message):
	summa = message.text
	if not summa.isdigit():
		bot.send_message(message.chat.id ,"Summani kiriting\n Faqat raqamlar bilan")
	
	s = user_info.get(message.chat.id)	
	status = s.get('status')
	if not status:		
		bot.send_message(message.chat.id ,"Avval birorta funksiyani tanlang",reply_markup=key)
	else:
		if status == "ru-uz":
			c = course('ru')
			print(type(c))
			print(c)
			c = int(c.split('.')[0])
			result = c * int(summa)
	
			bot.send_message(message.chat.id ,f"Natija {result} sum",reply_markup=key)

			
bot.polling()