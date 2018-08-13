#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
import requests
import json

class Weather:
	def __init__(self, window, config):
		if config['WEATHER']['api'] == "":
			return None

		self.config = config
		self.api = 'https://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s&units=metric&lang=cz' % (config['WEATHER']['city'], config['WEATHER']['api'])
		self.getWeather()

	def getWeather(self):
		weather = requests.get(self.api)
		weather = json.loads(weather.text)
		print weather['list'][0]['main']

	def draw(self):
		return True	