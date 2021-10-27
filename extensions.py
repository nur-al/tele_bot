import requests
import json
import config


class ConvertionException(Exception):
	pass

class CriptoConverter:
	@staticmethod
	def convert(values):
		try:
			base, quote, amount = values
		except ValueError:
			raise ConvertionException('Неверное количество параметров.')

		try:
			quote_ticker = config.keys[quote]
		except KeyError:
			raise ConvertionException(f'Не удалось обработать валюту {quote}')

		try:
			base_ticker = config.keys[base]
		except KeyError:
			raise ConvertionException(f'Не удалось обработать валюту {base}')

		try:
			amount = float(amount)
		except ValueError:
			raise ConvertionException(f'Не удалось обработать количество {amount}')
		
		r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
		return json.loads(r.content)[config.keys[quote]]*amount