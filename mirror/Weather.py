#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
import requests
import json

class Weather:
	def __init__(self, *args, **kwargs):
		self.api = 'https://api.openweathermap.org/data/2.5/forecast?q=B%C3%ADlovec,CZ&appid=***&units=metric&lang=cz'
		self.getWeather()

	def getWeather(self):
		weather = requests.get(self.api)
		weather = json.loads(weather.text)
		print weather['list'][0]['main']

	def draw(self):
		return True	