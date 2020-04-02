import requests, bs4, telebot, datetime


bot = telebot.TeleBot('token')



@bot.message_handler(commands=['start', 'status'])
def start_message(message):
    awithvirus = open('withvirus.txt', 'r')
    ahealth = open('health.txt', 'r')
    adied = open('died.txt', 'r')
    withvirus = awithvirus.read()
    health = ahealth.read()
    died = adied.read()
    bot.send_message(message.chat.id, 'Статистика по CoViD-19 🦠 в Україні: \n' + 'Захворіли🤧: ' + withvirus + '\nВилікованно💊: ' + health + '\nПомерлих☠️: ' + died)
    now = datetime.datetime.now()
    s=requests.get('https://www.worldometers.info/coronavirus/')
    print("message send at: " + now.strftime("%d-%m-%Y %H:%M"))
    b=bs4.BeautifulSoup(s.text, "html.parser")
    p=b.select('.maincounter-number ')
    pogoda=p[0].getText()
    bot.send_message(message.chat.id, 'Статистика по CoViD-19 🦠 у Світі на момент ' + now.strftime("%d-%m-%Y %H:%M") + ' :' + '\nЗахворіли🤧: ' + pogoda.strip()  ) 
   

bot.polling()
