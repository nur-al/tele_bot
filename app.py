import telebot
import config
from extensions import ConvertionException, CriptoConverter

bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands = ['start', 'help'])
def help(message: telebot.types.Message):
	text = 'Чтобы начать работу, введите команду боту в следующем формате:\n \
<имя валюты, цену на которую надо узнать> <имя валюты, цену в которой надо узнать> \
<количество переводимой валюты>\n \
Увидеть список всех доступных валют: /values'
	bot.reply_to(message, text)

@bot.message_handler(commands = ['values'])
def values(message: telebot.types.Message):
	text = 'Доступные валюты:'
	for key in config.keys.keys():
		text = '\n'.join((text, key))
	bot.reply_to(message, text)

@bot.message_handler(content_types = ['text', ])
def convert(message: telebot.types.Message):
	values = message.text.split()

	try:
		total_cost = CriptoConverter.convert(values)
	except ConvertionException as e:
		bot.reply_to(message, f'Ошибка ввода\n{e}')
	except Exception as e:
		bot.reply_to(message, f'Не удалось обработать команду\n{e}')
	else:
		base, quote, amount = values
		text = f'Цена {amount} {base} в {quote} = {total_cost}'
		bot.send_message(message.chat.id, text)


bot.polling(none_stop = True) # bot.polling launches the bot, (none_stop=True) не выключает бота даже при возникновении исключения

#cryprocompare api key e598b1b4e1147b795d007a9688368f923af2367eb9e95ea01e376cf87aa0ff71
