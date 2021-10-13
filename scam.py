import telebot
from telebot import types

bot = telebot.TeleBot('1600467870:AAEP0kO8etZdETF2gMCbHd87Ocq_C7mx_68')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🖥️Добро пожаловать в AntiVac. Для продолжения выберите пункт ниже.🖥️")
    bot.send_message(message.chat.id, "💲Тут вы сможете снять блокировку VAC с вашего аккаунта Steam недорого💲")
    bot.send_message(message.chat.id, "💬Для покупки разблокировки введите /buyunlock💬")
    bot.send_message(message.chat.id, "🤔Для получения подробной информации введите команду /info🤔")


@bot.message_handler(commands=['buyunlock'])
def buyunlock(message):
    bot.send_message(message.chat.id, "🖥️Стоимость разблокировки 400 Рублей.🖥️")
    bot.send_message(message.chat.id, "💬Что-бы осуществить разблокировку вам нужно перевести данную сумму на указаный ниже Qiwi Кошелёк с комментарием вашей ссылки для связи💬")
    bot.send_message(message.chat.id, "💲Qiwi - https://qiwi.com/n/TWOAT382💲")
    bot.send_message(message.chat.id, "😏Приятного пользования!😏")


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, "🤔Как же мы работаем?🤔")
    bot.send_message(message.chat.id, "🤔Наша команда взламывает сервера Valve🤔")
    bot.send_message(message.chat.id, "🤔Мы получаем доступ к списку пользователей с VAC🤔")
    bot.send_message(message.chat.id, "🤔После мы ищем вас и удаляем из списка.🤔")




bot.polling(none_stop=True)