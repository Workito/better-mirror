#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
from pyglet.gl import *
import requests
import json
from datetime import datetime

from Helper import *

class Weather:
	def __init__(self, window, config):
		if config['WEATHER']['api'] == "":
			return None

		self.config = config
		self.window = window
		self.batch = pyglet.graphics.Batch()
		self.api = 'https://api.openweathermap.org/data/2.5/forecast?q={:s}&appid={:s}&units=metric&lang=cz'.format(config['WEATHER']['city'], config['WEATHER']['api'])

		self.actualTemp = Helper.label(self, '', 60, 0, 0, self.batch, window, config['WEATHER'])
		self.actualWeather = Helper.label(self, '', 20, 180, -55, self.batch, window, config['WEATHER'])
		self.actualHumidityIcon = Helper.label(self, 'd', 14, 0, -98, self.batch, window, config['WEATHER'], True)
		self.actualHumidity = Helper.label(self, '', 14, 20, -95, self.batch, window, config['WEATHER'])
		self.actualPressureIcon = Helper.label(self, 'f', 14, 75, -98, self.batch, window, config['WEATHER'], True)
		self.actualPressure = Helper.label(self, '', 14, 100, -95, self.batch, window, config['WEATHER'])
		self.actualWindIcon = Helper.label(self, 'e', 14, 200, -98, self.batch, window, config['WEATHER'], True)
		self.actualWind = Helper.label(self, '', 14, 220, -95, self.batch, window, config['WEATHER'])
		
		self.getWeather()


	def getWeather(self):
		weather = requests.get(self.api)
		self.weather = json.loads(weather.text)

		self.showWeather()


	def showWeather(self):
		actual = self.weather['list'][0]
		self.actualTemp.text = '{:02.0f}{:s}'.format(actual['main']['temp'], '°C')
		self.actualWeather.text = str(actual['weather'][0]['description'])
		self.actualHumidity.text = '{:02.0f}{:s}'.format(actual['main']['humidity'], '%')
		self.actualPressure.text = '{:02.2f}{:s}'.format(actual['main']['pressure'], 'hPa')
		self.actualWind.text = '{:02.2f}{:s}'.format(actual['wind']['speed'], 's/m')
		
		Helper.label(self, self.getWeatherIcon(actual['weather'][0]['icon']), 36, 175, -15, self.batch, self.window, self.config['WEATHER'], True)

		self.showForecast()


	def showForecast(self):
		l = [1,2,3,6,10,14,20]
		index = 0;
		offsetStart = 100
		for item in l:
			index = index + 1
			offset = 23 * index

			Helper.label(
				self,
				datetime.strptime(self.weather['list'][item]['dt_txt'], '%Y-%m-%d %H:%M:%S').strftime('%a %H:%M'),
				16,
				0,
				-offsetStart-offset,
				self.batch, self.window, self.config['WEATHER'])

			Helper.label(
				self,
				'{:02.0f}{:s}'.format(self.weather['list'][item]['main']['temp'], '°C'),
				16,
				85,
				-offsetStart-offset,
				self.batch, self.window, self.config['WEATHER'])

			Helper.label(
				self,
				self.getWeatherIcon(self.weather['list'][item]['weather'][0]['icon']),
				14,
				140,
				-offsetStart-offset-8,
				self.batch, self.window, self.config['WEATHER'], True)

			Helper.label(
				self,
				self.weather['list'][item]['weather'][0]['description'],
				16,
				170,
				-offsetStart-offset,
				self.batch, self.window, self.config['WEATHER'])


	def getWeatherIcon(self, iconName):
		icons = {
			'01d': '1', '01n': '1',
			'02d': '2', '02n': '2',
			'03d': '3', '03n': '3',
			'04d': '4', '04n': '4',
			'09d': '9', '09n': '9',
			'10d': 'a', '10n': 'a',
			'11d': 'b', '11n': 'b',
			'13d': 'c', '13n': 'c',
			'50d': 'd', '50n': 'd'
		}

		return icons[iconName]


	def draw(self):
		self.batch.draw()