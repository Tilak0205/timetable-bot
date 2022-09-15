from datetime import date, timedelta
import datetime
from time import sleep
import time
from bs4 import BeautifulSoup
import json
import requests
import pytz
import json
import _thread
import random
import telegram
import urllib3
import urllib.parse
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update,ParseMode
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
import time
WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

now = time.localtime()
weekday_index = now.tm_wday
# print(WEEKDAYS[weekday_index])

# with open('data.txt','r') as f:
#     s = f.read()
#     s = s.replace('\t','')
#     s = s.replace('\n','')
#     s = s.replace(',}','}')
#     s = s.replace(',]',']')
#     s = s.replace("\'", "\"")
#     data_dict = json.loads(s)
# print(data_dict)


#with open("data.txt") as tweetfile:
#    pyresponse = json.load(tweetfile)
#    data_dict = pyresponse
#except:
total_dict={}

data_dict = {}

# print(data_dict)

#data_dict['requests_served'] = 0

def start(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about their gender."""
    m = 'Hello! I am TimeTable Bot.\n<b>Enter Your ID:</b>'
    update.message.reply_text(
        m,parse_mode=ParseMode.HTML
    )

    return StudentID


def StudentID(update: Update, context: CallbackContext) -> int:
    """Stores the selected ID"""    
    user = update.message.from_user
    print(update.message.text)
    print(update.message.chat.id)
    print(update.message.chat.first_name)
    chat_id=update.message.chat.id
    ID = update.message.text.upper()
    data_dict[str(chat_id)]=[str(ID)]
    update.message.reply_text(
        'Enter your Class Number(ex. 012):',
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    
    return StudentClass
    # return ConversationHandler.END


def StudentClass(update: Update, context: CallbackContext) -> int:
    #storing class
    data_dict1={}
    user=update.message.from_user
    clss=update.message.text
    chat_id = update.message.chat.id
    print(clss)
    ID=data_dict[str(chat_id)]
    ID=ID[0]
    lis=[ID,clss]
    data_dict.clear()
    # data_dict[str(ID)] =lis
    total_dict[str(chat_id)]=lis
    
    print(total_dict)
    update.message.reply_text(
        'Thank You',
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    return ConversationHandler.END

def find(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        '<b>Enter your friend\'s class:</b>',parse_mode=ParseMode.HTML
    )
    return getFriend

def getFriend(update,context):

    clss=update.message.text
    day=WEEKDAYS[weekday_index]

    bot = telegram.Bot("5559089138:AAHyQ9N05VFvktPYYyDIonB7SSNmGaNtDCo")
    url = "https://rgutimetable-bot.herokuapp.com/?class="+str(clss)+"&day="+str(day)+""
    
    payload={}
    response = requests.request("GET", url, data=payload,verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    text=soup.get_text()
    text=text.replace("<br>","\n")
    print(text)
    update.message.reply_text(
        text,parse_mode=ParseMode.HTML
    )
    return ConversationHandler.END

def cancel(update, context):
    # context.bot.send_message('See yaa!')
    update.message.reply_text(
        'See yaa!',
        reply_markup=ReplyKeyboardRemove(),
        parse_mode=ParseMode.HTML
    )
    return ConversationHandler.END

def stop(update, context):
    context.bot.send_message('Good Bye')
    return ConversationHandler.END

def get(update,context):
    print(total_dict)
    chat_id=update.message.chat.id
    clss = total_dict[str(chat_id)][1]
    day=WEEKDAYS[weekday_index]

    bot = telegram.Bot("5559089138:AAHyQ9N05VFvktPYYyDIonB7SSNmGaNtDCo")
    url = "https://rgutimetable-bot.herokuapp.com/?class="+str(clss)+"&day="+str(day)+""
    
    payload={}
    response = requests.request("GET", url, data=payload,verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    text=soup.get_text()
    # text=text.replace("<br>","\n")
    print(text)
    update.message.reply_text(
        text,parse_mode=ParseMode.HTML
    )

    return ConversationHandler.END

def main() -> None:
    """ Run the bot """
    # Create the Updater and pass it your bot's token.
    updater = Updater("5559089138:AAHyQ9N05VFvktPYYyDIonB7SSNmGaNtDCo")
    #updater = Updater("5055436218:AAGECy2YhUsSnDUH6boXYD04Wo2SLczJZfs") #testing
    
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start), CommandHandler('cancel',cancel),CommandHandler('find',find),CommandHandler('get',get)],
        states={
           
            StudentID: [MessageHandler(Filters.text & ~Filters.command, StudentID)],
            StudentClass: [MessageHandler(Filters.text & ~Filters.command, StudentClass)],
            getFriend: [MessageHandler(Filters.text & ~Filters.command, getFriend)],
            # friendHall: [MessageHandler(Filters.text & ~Filters.command, friendHall)],
            # announce: [MessageHandler(Filters.text & ~Filters.command, announce)],
        },
        fallbacks=[CommandHandler('stop', stop)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()
    updater.idle()
  
if __name__ == '__main__':
    main()
