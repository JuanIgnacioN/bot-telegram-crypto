import requests
import json
from datetime import datetime
from telegram.ext import Updater, CommandHandler
import token

# API COINGECKO
url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
res = requests.get(url)
response = json.loads(res.content)
today = datetime.today().strftime('%d-%m-%Y %H:%M')


# FUNCIONES
def get_key(val):
    lst = []
    for item in response:
        for key, value in item.items():
            if key == val:
                lst.append(value)
    return lst


def help_message():
    message_help = f"Hi! I'm @CriptGeckBot. To know information about a crypto you have to send the command /coin + abbreviation: \n"
    for i in response:
        message_help += f"{i['symbol']} : {i['name']} \n"
    message_help += f"\n/social: Social media of my creator \n"
    return message_help


def social_message():
    return f"Thanks! \n" \
           f"Linkedin: linkedin.com/in/juanignacio \n" \
           f"GitHub: github.com/JuanIgnacioN \n" \


def coin_message(input_user):
    #Tomamos la respuesta del usuario luego del /coin' 'moneda elegida
    coin = input_user[6:]
    myList = get_key('symbol')
    if coin in myList:
        for elem in response:
            if coin == elem['symbol']:
                return f"Name: {elem['name']} \n" \
                    f"Rank: #{elem['market_cap_rank']} \n" \
                    f"Date: {today} HS. \n" \
                    f"Price: US$ {elem['current_price']}. \n" \
                    f"Price change 24h: US$ {elem['price_change_24h']}. \n" \
                    f"Change percentage 24h: % {elem['price_change_percentage_24h']}"
    else:
        return f"Command not found"


# FUNCIONES A LAS CUALES RESPONDE EL BOT
def start(update, context):
    update.message.reply_text('Welcome to @CriptGeckBot! by Juan Ignacio')


def help(update, context):
    update.message.reply_text(help_message())


def coin(update, context):
    user_input = update.message.text
    update.message.reply_text(coin_message(user_input))


def social(update, context):
    update.message.reply_text(social_message())


# FUNCION PRINCIPAL DEL BOT
def main(): 
    #reemplazar token.my_token por el que da telegram a la hora de crear tu propio bot   
    updater = Updater(token= token.my_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('social', social))
    dp.add_handler(CommandHandler('coin', coin))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()