from collections import UserDict
import telebot
from telebot import types
from dotenv import load_dotenv
import os
import time
import threading
import telebot

load_dotenv()

bot=telebot.TeleBot(os.getenv("TOKEN"))
admin_chat_id=os.getenv("ADMIN_CHAT_ID")
user_states = {}
users = []
Q1=int
A1=str
n = ''
num = 1
thread_stopped = True
user_id = int
first_name =''
last_name = ''
dict_reg = {}
USER = str
PASSWORD = int
todate = int
dict_answer = {
  Q1: A1, 
} 

@bot.message_handler(commands=['start'])
def button_message(message):
 if message.chat.id not in users:
        users.append(message.chat.id)
 bot.send_message(message.chat.id,'Бот собирает Ваши персональные данные, а также проводит опрос. Сперва зарегистрируйтесь /user.')
  

@bot.message_handler(commands=['user'])
def totalreg(message):
 first_name = str(message.from_user.first_name) 
 last_name = str(message.from_user.last_name)
 user_id = int(message.from_user.id)  
 bot.reply_to(message, f"{first_name} {last_name} id:{user_id} \n")
 keyboard_markup = types.ReplyKeyboardMarkup()
 btn_today = types.KeyboardButton('/registration')
 keyboard_markup.add(btn_today)
 bot.send_message(message.chat.id, 'Нажмите кнопку регистрации ', reply_markup=keyboard_markup)
 

@bot.message_handler(commands=["registration"])
def add_user_handler(message):
  bot.send_message(message.chat.id, 'Успешно!', reply_markup=types.ReplyKeyboardRemove())
  bot.send_message(message.from_user.id, 'Приступайте к набору вопросов. Учтите, время ограничено! /interview.')
  first_name = str(message.from_user.first_name) 
  last_name = str(message.from_user.last_name)
  user_id = int(message.from_user.id)
  USER = first_name + last_name
  PASSWORD = user_id
  dict_reg[PASSWORD] = USER 
  print(dict_reg)    
 

@bot.message_handler(commands=['interview'])
def run_questions(message):
 keyboard = types.InlineKeyboardMarkup() #наша клавиатура
 key_yes = types.InlineKeyboardButton(text='Да', callback_data='question1_yes') #кнопка «Да»
 key_yes = types.InlineKeyboardButton('/answer1')
 keyboard.add(key_yes) #добавляем кнопку в клавиатуру
 key_no= types.InlineKeyboardButton(text='Нет', callback_data='question1_no')
 keyboard.add(key_no)
 bot.send_message(message.from_user.id, text="Ты сегодня гулял?", reply_markup=keyboard)

        
# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     results = call.data.split("_")
#     if results[0] == "question1":
#         if results[1] == "yes":   
#             bot.send_message(call.message.chat.id, "Ответ записан.")
#         elif results[1] == "no":
#             bot.send_message(call.message.chat.id, "Ответ записан.")
#     bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=None)    


@bot.message_handler(commands=["answer1"])
def registerAnswer1(message):
   bot.send_message(message.chat.id, 'Ответ записан!')
   Q1 = num
   A1 = 'yes'
   dict_answer[Q1]=A1
   print(dict_answer)

    

      
      
 
     

         
# def callback_worker(message):

#           first_name = str(message.from_user.first_name) 
#           last_name = str(message.from_user.last_name)
#           user_id = int(message.from_user.id)
#           USER = first_name + last_name
#           PASSWORD = user_id
#           dict_sample[PASSWORD] = USER 
#           print(dict_sample)    
    
#bot.send_message(message.from_user.id, text="Успешно! Приступайте к набору вопросов.", reply_markup=keyboard)

# @bot.message_handler(commands=['chat_id'])
# def get_chat_id(message):
#     bot.send_message(message.chat.id,"Твой chat id: {0}".format(message.chat.id))

# @bot.message_handler(commands=['run_thread'])
# def run_thread(message):
#     global thread_stopped
#     thread_stopped = False
#     bot.send_message(message.chat.id,"Поток запущен")

# @bot.message_handler(commands=['stop_thread'])
# def stop_thread(message):
#     global thread_stopped
#     thread_stopped = True
#     bot.send_message(message.chat.id,"Поток остановлен")

# @bot.message_handler(commands=['send_to_users'])
# def send_to_users(message):
#     if message.chat.id != admin_chat_id:
#         bot.send_message(message.chat.id, "Ты не админ")
#         return

#     text_for_users = message.text.split("send_to_users")[1:]
#     for user in users:
#         # if user != admin_chat_id:
#         bot.send_message(user,text_for_users)

# @bot.message_handler(commands=['questions'])

# def sendTimer():
#     while True:
#         if not thread_stopped:
#             bot.send_message(admin_chat_id, text="Бот запущен, сейчас timestamp: {0}".format(time.time_ns()))
#         time.sleep(10)

# threading.Thread(target=sendTimer).start()

bot.infinity_polling()

  
