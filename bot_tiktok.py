import requests,json,telebot,random
from telebot import *
tok=""#توكن بوتك
bot=telebot.TeleBot(tok)
@bot.message_handler(commands=['start'])
def run(message):
	key = types.InlineKeyboardMarkup()
	back=types.InlineKeyboardButton(text='قـنـاة الـبـوت </>', url='https://t.me/YRWSYY')
	key.row_width = 1
	key.add(back)
	first_name = message.from_user.first_name
	bot.send_message(message.chat.id,text=f"<strong>Hi, {first_name}! Sire\nBot View Tiktok Free\nPlease Send \nExample: LinkYou Only</strong>",parse_mode='html',reply_markup=key)
@bot.message_handler(func= lambda m: True)
def mess(message):
	
	user = message.from_user.username
	id = message.from_user.id
	link = message.text
	
	if '//' in link:
		try:
			with open('prox.txt', "r") as filena:
				allText = filena.read()
				words = list(map(str, allText.split()))
				proxies1 = random.choice(words)
				proxies = {'http': f'https://{proxies1}','http': f'https://{proxies1}'}
				url = "https://api.likesjet.com/freeboost/3"
		
				payload = json.dumps({
				  "link": link,
				  "tiktok_username": user+'12',
				  "email": user+"102@gmail.com"
				})
			
				headers = {
				  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
				  'Accept': "application/json, text/plain, */*",
				  'Content-Type': "application/json",
				  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
				  'sec-ch-ua-mobile': "?1",
				  'sec-ch-ua-platform': "\"Android\"",
				  'origin': "https://likesjet.com",
				  'sec-fetch-site': "same-site",
				  'sec-fetch-mode': "cors",
				  'sec-fetch-dest': "empty",
				  'referer': "https://likesjet.com/",
				  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"
				}
				
				r = requests.post(url, data=payload, headers=headers,proxies=proxies).text
				print(r)
				if 'Success!' in r:
					bot.send_message(message.chat.id,text=f"<strong>Done Send 1.5K View 😈🔥</strong>",parse_mode='html')
					
				elif 'time' in r or 'wait' in r:
					bot.send_message(message.chat.id,text=f"<strong>Please Wait 3 minute a Try Again</strong>",parse_mode='html')
					
					
				else:
					bot.send_message(message.chat.id,text=f"<strong>Sorry Come Tomorrow</strong>",parse_mode='html')
					
		
		except:
				bot.send_message(message.chat.id,text=f"<strong>Error Send Format Link And User</strong>",parse_mode='html')	
	else:
		bot.send_message(message.chat.id,text=f"<strong>Error Link Send Link Work</strong>",parse_mode='html')	
bot.polling(True)