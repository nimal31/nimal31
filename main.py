import telebot,os
import tele
import re,json
import requests
import telebot,time,random
import random
import string
from telebot import types
from gatet import *
from file import *
from reg import reg
from datetime import datetime, timedelta
from faker import Faker
from multiprocessing import Process
import threading
from bs4 import BeautifulSoup
stopuser = {}
token = 'tok'
bot=telebot.TeleBot(token,parse_mode="HTML")
admin=id
command_usage = {}
def reset_command_usage():
	for user_id in command_usage:
		command_usage[user_id] = {'count': 0, 'last_time': None}	
@bot.message_handler(commands=["start"])
def start(message):
	def my_function():
		gate=''
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
		if BL == '𝗙𝗥𝗘𝗘':	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/@X_V_V0")
			keyboard.add(contact_button)
			random_number = random.randint(33, 82)
			photo_url = f'https://t.me/@f_k4f/2'
			bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=f'''<b>🤖 𝗕𝗼𝘁 𝗦𝘁𝗮𝘁𝘂𝘀: 𝗔𝗰𝘁𝗶𝘃𝗲 ✅ 𝗝𝗼𝗶𝗻   <a href="t.me/@X_V_V0">𝗛𝗲𝗿𝗲</a> 𝘁𝗼 𝗚𝗲𝘁 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 𝗔𝗻𝗱 𝗞𝗲𝘆𝘀 𝗙𝗼𝗿 𝗧𝗵𝗲 𝗕𝗼𝘁. 𝗦𝗲𝗻𝗱 /cmds 𝗕𝘆 <a href="t.me/@X_V_V0">@X_V_V0</a>. 𝗜𝗳 𝗬𝗼𝘂 𝗪𝗮𝗻𝘁 𝘁𝗼 𝗥𝘂𝗻 𝗮 𝗕𝗼𝘁 𝗜𝗻 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽, 𝗠𝗮𝗸𝗲 𝗦𝘂𝗿𝗲 𝗧𝗵𝗲 𝗕𝗼𝘁 𝗶𝘀 𝗧𝗵𝗲 𝗔𝗱𝗺𝗶𝗻  /plan   🎁</b>
	''',reply_markup=keyboard)
			return
		keyboard = types.InlineKeyboardMarkup()
		contact_button = types.InlineKeyboardButton(text="✨ 𝗝𝗢𝗜𝗡 ✨", url="https://t.me/@X_V_V0")
		keyboard.add(contact_button)
		username = message.from_user.first_name
		random_number = random.randint(33, 82)
		photo_url = f'https://t.me/recbo@X_V_V0/2'
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption='''𝗡𝗼𝘄 𝗦𝗲𝗻𝗱 𝗧𝗵𝗲 /cmds 𝗖𝗼𝗺𝗺𝗮𝗻𝗱

𝗧𝗼 𝗦𝗲𝗲 𝗧𝗵𝗲 𝗚𝗮𝘁𝗲𝘀 𝗔𝗻𝗱 𝗖𝗵𝗼𝗼𝘀𝗲 𝗔 𝗖𝗵𝗲𝗰𝗸 𝗖𝗰 𝗧𝗼 𝗚𝗮𝘁𝗲 𝗜𝘁  ✅


<a href="t.me/@X_V_V0">@X_V_V0</a>''',reply_markup=keyboard)
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["cmds"])
def start(message):
	with open('data.json', 'r') as file:
		json_data = json.load(file)
	id=message.from_user.id
	try:BL=(json_data[str(id)]['plan'])
	except:
		BL='𝗙𝗥𝗘𝗘'
	name = message.from_user.first_name
	keyboard = types.InlineKeyboardMarkup()
	contact_button = types.InlineKeyboardButton(text=f"✨ {BL}  ✨",callback_data='plan')
	keyboard.add(contact_button)
	bot.send_message(chat_id=message.chat.id, text=f'''<b> 
━━━━━━━━━━━━━━━━━━━

[Ϟ] 𝗡𝗮𝗺𝗲: 𝗕𝗿𝗮𝗶𝗻𝘁𝗿𝗲𝗲 𝗔𝘂𝘁𝗵
[Ϟ] 𝗦𝘁𝗮𝘁𝘂𝘀: 𝗢𝗻! ✅
[Ϟ] 𝗧𝘆𝗽𝗲: 𝗩𝗜𝗣

━━━━━━━━━━━━━━━━━━━

[Ϟ] 𝗡𝗮𝗺𝗲: 𝟯𝗗 𝗟𝗼𝗼𝗸𝗨𝗣
[Ϟ] 𝗦𝘁𝗮𝘁𝘂𝘀: 𝗢𝗻! ✅
[Ϟ] 𝗧𝘆𝗽𝗲: 𝗩𝗜𝗣

━━━━━━━━━━━━━━━━━━━

𝐖𝐞 𝐖𝐢𝐥𝐥 𝐀𝐝𝐝𝐢𝐧𝐠 𝐌𝐨𝐫𝐞 𝐆𝐚𝐭𝐞𝐬</b>
''',reply_markup=keyboard)
@bot.message_handler(content_types=["document"])
def main(message):
		name = message.from_user.first_name
		with open('data.json', 'r') as file:
			json_data = json.load(file)
		id=message.from_user.id
		
		try:BL=(json_data[str(id)]['plan'])
		except:
			BL='𝗙𝗥𝗘𝗘'
		if BL == '𝗙𝗥𝗘𝗘':
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				id : {
	  "plan": "𝗙𝗥𝗘𝗘",
	  "timer": "none",
				}
			}
	
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/@f_k4f")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>🤖 𝗕𝗼𝘁 𝗦𝘁𝗮𝘁𝘂𝘀: 𝗔𝗰𝘁𝗶𝘃𝗲 ✅ 𝗝𝗼𝗶𝗻   <a href="t.me/@X_V_V0">𝗛𝗲𝗿𝗲</a> 𝘁𝗼 𝗚𝗲𝘁 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 𝗔𝗻𝗱 𝗞𝗲𝘆𝘀 𝗙𝗼𝗿 𝗧𝗵𝗲 𝗕𝗼𝘁. 𝗦𝗲𝗻𝗱 /cmds 𝗕𝘆 <a href="t.me/@X_V_V0">@X_V_V0</a>. 𝗜𝗳 𝗬𝗼𝘂 𝗪𝗮𝗻𝘁 𝘁𝗼 𝗥𝘂𝗻 𝗮 𝗕𝗼𝘁 𝗜𝗻 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽, 𝗠𝗮𝗸𝗲 𝗦𝘂𝗿𝗲 𝗧𝗵𝗲 𝗕𝗼𝘁 𝗶𝘀 𝗧𝗵𝗲 𝗔𝗱𝗺𝗶𝗻  /plan   🎁</b>
''',reply_markup=keyboard)
			return
		with open('data.json', 'r') as file:
			json_data = json.load(file)
			date_str=json_data[str(id)]['timer'].split('.')[0]
		try:
			provided_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
		except Exception as e:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/@X_V_V0")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>🤖 𝗕𝗼𝘁 𝗦𝘁𝗮𝘁𝘂𝘀: 𝗔𝗰𝘁𝗶𝘃𝗲 ✅ 𝗝𝗼𝗶𝗻   <a href="t.me/@X_V_V0">𝗛𝗲𝗿𝗲</a> 𝘁𝗼 𝗚𝗲𝘁 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 𝗔𝗻𝗱 𝗞𝗲𝘆𝘀 𝗙𝗼𝗿 𝗧𝗵𝗲 𝗕𝗼𝘁. 𝗦𝗲𝗻𝗱 /cmds 𝗕𝘆 <a href="t.me/@X_V_V0">@X_V_V0</a>. 𝗜𝗳 𝗬𝗼𝘂 𝗪𝗮𝗻𝘁 𝘁𝗼 𝗥𝘂𝗻 𝗮 𝗕𝗼𝘁 𝗜𝗻 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽, 𝗠𝗮𝗸𝗲 𝗦𝘂𝗿𝗲 𝗧𝗵𝗲 𝗕𝗼𝘁 𝗶𝘀 𝗧𝗵𝗲 𝗔𝗱𝗺𝗶𝗻  /plan   🎁</b>
''',reply_markup=keyboard)
			return
		current_time = datetime.now()
		required_duration = timedelta(hours=0)
		if current_time - provided_time > required_duration:
			keyboard = types.InlineKeyboardMarkup()
			contact_button = types.InlineKeyboardButton(text="✨ 𝗢𝗪𝗡𝗘𝗥  ✨", url="https://t.me/X_V_V0")
			keyboard.add(contact_button)
			bot.send_message(chat_id=message.chat.id, text=f'''<b>𝙔𝙤𝙪 𝘾𝙖𝙣𝙣𝙤𝙩 𝙐𝙨𝙚 𝙏𝙝𝙚 𝘽𝙤𝙩 𝘽𝙚𝙘𝙖𝙪𝙨𝙚 𝙔𝙤𝙪𝙧 𝙎𝙪𝙗𝙨𝙘𝙧𝙞𝙥𝙩𝙞𝙤𝙣 𝙃𝙖𝙨 𝙀𝙭𝙥𝙞𝙧𝙚𝙙</b>
		''',reply_markup=keyboard)
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			json_data[str(id)]['timer'] = 'none'
			json_data[str(id)]['paln'] = '𝗙𝗥𝗘𝗘'
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			return
		keyboard = types.InlineKeyboardMarkup()
		sw = types.InlineKeyboardButton(text=f"⚜️ 𝟯𝗗 𝗟𝗼𝗼𝗸𝗨𝗣 ⛔",callback_data='sq')
		keyboard.add(sw)
		bot.reply_to(message, text=f'𝘾𝙝𝙤𝙤𝙨𝙚 𝙏𝙝𝙚 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝙔𝙤𝙪 𝙒𝙖𝙣𝙩 𝙏𝙤 𝙐𝙨𝙚',reply_markup=keyboard)
		ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open("combo.txt", "wb") as w:
			w.write(ee)

@bot.callback_query_handler(func=lambda call: call.data == 'sq')
def menu_callback(call):
	def my_function():
		id=call.from_user.id
		gate='𝟑𝐃 𝐋𝐎𝐎𝐊𝐔𝐏'
		dd = 0
		live = 0
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗖𝗮𝗿𝗱...⌛️")
		try:
			with open("combo.txt", 'r') as file:
				lino = file.readlines()
				total = len(lino)
				try:
					stopuser[f'{id}']['status'] = 'start'
				except:
					stopuser[f'{id}'] = {
				'status': 'start'
			}
				for cc in lino:
					if stopuser[f'{id}']['status'] == 'stop':
						bot.edit_message_text(chat_id=call.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜『@X_V_V0』')
						return
					try:
						data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
						
					except:
						pass
					try:
						bank=(data['bank']['name'])
					except:
						bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country_flag=(data['country']['emoji'])
					except:
						country_flag=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						country=(data['country']['name'])
					except:
						country=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						brand=(data['scheme'])
					except:
						brand=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						card_type=(data['type'])
					except:
						card_type=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					try:
						url=(data['bank']['url'])
					except:
						url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
					
					start_time = time.time()
					try:
						last = str(vbv(cc))
					except Exception as e:
						print(e)
						last = "ERROR"
					mes = types.InlineKeyboardMarkup(row_width=1)
					cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
					status = types.InlineKeyboardButton(f"• 𝙎𝙏𝘼𝙏𝙐𝙎 ➜ {last} •", callback_data='u8')
					cm3 = types.InlineKeyboardButton(f"• 𝗢𝘁𝗽 ⛔ ➜ [ {live} ] •", callback_data='x')
			
					cm4 = types.InlineKeyboardButton(f"• 𝐃𝐄𝐂𝐋𝐈𝐍𝐄𝐃 ❌ ➜ [ {dd} ] •", callback_data='x')
					cm5 = types.InlineKeyboardButton(f"• 𝙏𝙊𝙏𝘼𝙇 👻 ➜ [ {total} ] •", callback_data='x')
					stop=types.InlineKeyboardButton(f"[ 𝙎𝙏𝙊𝙋 ]", callback_data='stop')
					mes.add(cm1,status, cm3, cm4, cm5, stop)
					end_time = time.time()
					execution_time = end_time - start_time
					bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text=f'''Wait, I\'M Checking Your Cards file Now On The Gateway Braintree Lookup. To Stop The Check, Send /Stop or Press The Stop Button''', reply_markup=mes)
					
					
					
					msg=f'''<b>𝗢𝘁𝗽 ⛔
			
[↯] 𝗖𝗖 ⇾<code>{cc}</code>
[↯] 𝗚𝗔𝗧𝗘𝗦 ⇾ {gate}
[↯] 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 →{last}
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗜𝗡 → <code>{cc[:6]} - {card_type} - {brand}</code>
[↯] 𝗕𝗮𝗻𝗸  → {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 → <code>{country} - {country_flag}</code> 
━━━━━━━━━━━━━━━━
[↯] 𝗧𝗶𝗺𝗲 𝗧𝗮𝗸𝗲𝗻 ⇾{"{:.1f}".format(execution_time)} secounds .
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗼𝘁 𝗕𝘆 ⇾『@X_V_V0』</b>'''
					
					if "3DS Challenge Required ❌" in last:
						live += 1
						bot.send_message(call.from_user.id, msg)
					else:
						dd += 1
					time.sleep(5)
		except Exception as e:
			print(e)
		stopuser[f'{id}']['status'] = 'start'
		bot.edit_message_text(chat_id=call.message.chat.id, 
					  message_id=call.message.message_id, 
					  text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜『@X_V_V0』')
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
	

		
def generate_credit_card(message, bot, ko):
    try:
        # البحث عن رقم البطاقة والبيانات الأخرى في الرسالة
        match = re.search(r'(\d{6,16})\D*(\d{1,2}|xx)?\D*(\d{2,4}|xx)?\D*(\d{3,4}|xxx)?', message.text)
        if match:
            card_number = match.group(1)
            
            # التحقق من صحة BIN
            if len(card_number) < 6 or card_number[0] not in ['4', '5', '3', '6']:
                bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>BIN not recognized. Please enter a valid BIN ❌</b>''', parse_mode="HTML")
                return

            bin = card_number[:6]
            response_message = ""

            # توليد 10 بطاقات ائتمان
            for _ in range(10):
                month = int(match.group(2)) if match.group(2) and match.group(2) != 'xx' else random.randint(1, 12)
                year = int(match.group(3)) if match.group(3) and match.group(3) != 'xx' else random.randint(2025, 2029)

                # تحديد طول الـ CVV بناءً على نوع البطاقة
                if card_number[:1] == "3":
                    cvv = int(match.group(4)) if match.group(4) and match.group(4) != 'xxx' else random.randint(1000, 9999)
                else:
                    cvv = int(match.group(4)) if match.group(4) and match.group(4) != 'xxx' else random.randint(100, 999)

                # توليد بطاقة ائتمان مع الشهر، السنة، والـ CVV
                credit_card_info = generate_credit_card_info(card_number, month, year, cvv)
                response_message += f"<code>{credit_card_info}</code>\n"

            # جلب معلومات الـ BIN
            try:
                data = requests.get(f'https://bins.antipublic.cc/bins/{bin}').json()
                brand = data.get('brand', 'Unknown')
                card_type = data.get('type', 'Unknown')
                country = data.get('country_name', 'Unknown')
                country_flag = data.get('country_flag', 'Unknown')
                bank = data.get('bank', 'Unknown')
            except:
                brand = 'Unknown'
                card_type = 'Unknown'
                country = 'Unknown'
                country_flag = 'Unknown'
                bank = 'Unknown'

            # إرسال النتيجة إلى المستخدم
            bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f"𝐁𝐈𝐍 ➜  {bin}\n\n{response_message}\n𝐁𝐈𝐍 𝐈𝐧𝐟𝐨 ➜ {brand} - {card_type}\n𝐁𝐚𝐧𝐤 ➜  {bank}\n𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➜ {country} - {country_flag}", parse_mode="HTML")
        else:
            # في حالة الإدخال غير الصحيح
            bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''<b>Invalid input. Please provide a BIN (Bank Identification Number) that is at least 6 digits but not exceeding 16 digits. 
Example: <code>/gen 412236xxxx |xx|2023|xxx</code></b>''', parse_mode="HTML")
    
    except IndexError:
        # معالجة الخطأ إذا كانت القائمة فارغة أو بها مشكلة
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text="<b>BIN not recognized. Please enter a valid BIN ❌</b>")
    
    except Exception as e:
        # معالجة أي أخطاء غير متوقعة
        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=f"An error occurred: {str(e)}")

def generate_credit_card_info(card_number, expiry_month, expiry_year, cvv):
    generated_num = str(card_number)
    if card_number[:1] == "5" or card_number[:1] == "4" or card_number[:1] == "6":
        while len(generated_num) < 15:
            generated_num += str(random.randint(0, 9))
        check_digit = generate_check_digit(generated_num)
        credit_card_number = generated_num + str(check_digit)
        return f"{credit_card_number}|{str(expiry_month).zfill(2)}|{str(expiry_year)[-2:]}|{cvv}"
    elif card_number[:1] == "3":
        while len(generated_num) < 14:
            generated_num += str(random.randint(0, 9))
        check_digit = generate_check_digit(generated_num)
        credit_card_number = generated_num + str(check_digit)
        return f"{credit_card_number}|{str(expiry_month).zfill(2)}|{str(expiry_year)[-2:]}|{cvv}"

def generate_check_digit(num):
    num_list = [int(x) for x in num]
    for i in range(len(num_list) - 1, -1, -2):
        num_list[i] *= 2
        if num_list[i] > 9:
            num_list[i] -= 9
    return (10 - sum(num_list) % 10) % 10

def luhn_checksum(card_number):
    digits = [int(x) for x in card_number]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for digit in even_digits:
        checksum += sum(divmod(digit * 2, 10))
    return checksum % 10




def gen(bin):
	remaining_digits = 16 - len(bin)
	card_number = bin + ''.join([str(random.randint(0, 9)) for _ in range(remaining_digits - 1)])
	digits = [int(digit) for digit in card_number]
	for i in range(len(digits)):
		if i % 2 == 0:
			digits[i] *= 2
			if digits[i] > 9:
				digits[i] -= 9
	
	checksum = sum(digits)
	checksum %= 10
	checksum = 10 - checksum
	if checksum == 10:
		checksum = 0
	card_number += str(checksum)
	return card_number
import requests

@bot.message_handler(func=lambda message: message.text.lower().startswith('.bin') or message.text.lower().startswith('/bin'))
def respond_to_vbv(message):
    try:
        # محاولة قراءة النص الذي تم الرد عليه إذا كان موجودًا
        bm = message.reply_to_message.text
    except:
        # إذا لم يكن هناك رسالة تم الرد عليها، استخدم النص الحالي
        bm = message.text
    
    # استخراج الأرقام من الرسالة
    regex = r'\d+'
    try:
        matches = re.findall(regex, bm)
    except:
        bot.reply_to(message, '<b>🚫 Incorrect input. Please provide a 6-digit BIN number.</b>', parse_mode="HTML")
        return

    # الحصول على أول 6 أرقام من BIN
    bin = ''.join(matches)[:6]
    ko = bot.reply_to(message, "<b>Checking Your bin...⌛</b>", parse_mode="HTML").message_id

    # التحقق من أن الـ BIN يتكون من 6 أرقام على الأقل
    if len(bin) >= 6:
        try:
            # طلب معلومات الـ BIN من API
            data = requests.get(f'https://bins.antipublic.cc/bins/{bin}').json()
            brand = data.get('brand', 'Unknown')
            card_type = data.get('type', 'Unknown')
            country = data.get('country_name', 'Unknown')
            country_flag = data.get('country_flag', '🏳️')
            bank = data.get('bank', 'Unknown')
            
            # تكوين الرسالة النهائية
            msg = f'''<b>
𝐕𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ✅
    
𝐁𝐈𝐍 ➜ <code>{bin}</code>
    
𝐁𝐈𝐍 𝐈𝐧𝐟𝐨 ➜ {card_type} - {brand}  
𝐁𝐚𝐧𝐤 ➜ {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ➜ {country} - {country_flag}
</b> '''
        except:
            # في حال حدوث خطأ أثناء طلب البيانات
            msg = '<b>𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐁𝐈𝐍 ❌</b>'
    else:
        msg = '<b>🚫 Incorrect input. Please provide a 6-digit BIN number.</b>'
    
    # تعديل الرسالة الأصلية مع النتيجة
    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=msg, parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text.lower().startswith('.gen') or message.text.lower().startswith('/gen'))
def respond_to_vbv(message):
	ko = (bot.reply_to(message, "<b>Generating cards...⌛</b>",parse_mode="HTML").message_id)
	generate_credit_card(message,bot,ko)



@bot.message_handler(func=lambda message: message.text.lower().startswith('.redeem') or message.text.lower().startswith('/redeem'))
def respond_to_vbv(message):
	def my_function():
		global stop
		try:
			re=message.text.split(' ')[1]
			with open('data.json', 'r') as file:
				json_data = json.load(file)
			timer=(json_data[re]['time'])
			typ=(json_data[f"{re}"]["plan"])
			json_data[f"{message.from_user.id}"]['timer'] = timer
			json_data[f"{message.from_user.id}"]['plan'] = typ
			with open('data.json', 'w') as file:
				json.dump(json_data, file, indent=2)
			with open('data.json', 'r') as json_file:
				data = json.load(json_file)
			del data[re]
			with open('data.json', 'w') as json_file:
				json.dump(data, json_file, ensure_ascii=False, indent=4)
			msg=f'''<b>𓆩𝗞𝗲𝘆 𝗥𝗲𝗱𝗲𝗲𝗺𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆𓆪! 🎉🐥   𝐃ev : 『@X_V_V0』  »»{timer}
🐥»»{typ}</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,'<b>Incorrect code or it has already been redeemed </b>',parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()
@bot.message_handler(commands=["code"])
def start(message):
	def my_function():
		id=message.from_user.id
		if not id ==admin:
			return
		try:
			h=float(message.text.split(' ')[1])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			characters = string.ascii_uppercase + string.digits
			pas ='saiccchk-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))+'-'+''.join(random.choices(characters, k=4))
			current_time = datetime.now()
			ig = current_time + timedelta(hours=h)
			plan='𝗩𝗜𝗣'
			parts = str(ig).split(':')
			ig = ':'.join(parts[:2])
			with open('data.json', 'r') as json_file:
				existing_data = json.load(json_file)
			new_data = {
				pas : {
	  "plan": plan,
	  "time": ig,
			}
			}
			existing_data.update(new_data)
			with open('data.json', 'w') as json_file:
				json.dump(existing_data, json_file, ensure_ascii=False, indent=4)	
			msg=f'''<b>╠═══════════════════════════╣
𓆩𝐊𝐞𝐲 𝐂𝐫𝐞𝐚𝐭𝐞𝐝𓆪
                       🌹💸	
✿├𝗦𝗧𝗔𝗧𝗨𝗦»»»{plan}
✿├𝗘𝘅𝗽𝗶𝗿𝗲𝘀 𝗼𝗻»»»{ig}
✿├『@X_V_V0』
✿├𝑲𝒆𝒚 »»»<code>{pas}</code>	
✿├𝙐𝙨𝙖𝙜𝙚»»»/redeem [𝗞𝗘𝗬]
╠════════════════════════════╣
</b>'''
			bot.reply_to(message,msg,parse_mode="HTML")
		except Exception as e:
			print('ERROR : ',e)
			bot.reply_to(message,e,parse_mode="HTML")
	my_thread = threading.Thread(target=my_function)
	my_thread.start()

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	id=call.from_user.id
	stopuser[f'{id}']['status'] = 'stop'
print("Bot Start On ✅ ")
while True:
	try:
		bot.polling(none_stop=True)
	except Exception as e:
		print(f"حدث خطأ: {e}")