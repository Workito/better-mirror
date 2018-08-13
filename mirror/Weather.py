#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
from pyglet.gl import *
import requests
import json
from datetime import datetime

class Weather:
	def __init__(self, window, config):
		if config['WEATHER']['api'] == "":
			return None
		self.config = config
		self.window = window
		self.batch = pyglet.graphics.Batch()
		self.api = 'https://api.openweathermap.org/data/2.5/forecast?q={:s}&appid={:s}&units=metric&lang=cz'.format(config['WEATHER']['city'], config['WEATHER']['api'])

		self.actualTemp = pyglet.text.Label(
			'', 
			font_name='Bree Serif', 
			font_size=60, 
			x=window.width-config['WEATHER']['position']['x'], 
			y=window.height-config['WEATHER']['position']['y'], 
			anchor_x='left', 
			anchor_y='top', 
			align='left',
			batch=self.batch)
		self.actualWeather = pyglet.text.Label(
			'', 
			font_name='Bree Serif', 
			font_size=20, 
			x=window.width-config['WEATHER']['position']['x']+180, 
			y=window.height-config['WEATHER']['position']['y']-55, 
			anchor_x='left', 
			anchor_y='top', 
			align='left',
			batch=self.batch)


		self.actualHumidityIcon = pyglet.text.Label(
			'd',
			font_name='fontello', 
			font_size=14, 
			x=self.window.width-self.config['WEATHER']['position']['x'],
			y=self.window.height-self.config['WEATHER']['position']['y']-98,
			anchor_x='left', 
			anchor_y='top', 
			align='left',
			batch=self.batch)

		self.actualHumidity = pyglet.text.Label(
			'', 
			font_name='Bree Serif', 
			font_size=14, 
			x=window.width-config['WEATHER']['position']['x']+20, 
			y=window.height-config['WEATHER']['position']['y']-95, 
			anchor_x='left', 
			anchor_y='top', 
			align='left',
			batch=self.batch)

		self.actualPressureIcon = pyglet.text.Label(
			'f',
			font_name='fontello', 
			font_size=14, 
			x=self.window.width-self.config['WEATHER']['position']['x']+75,
			y=self.window.height-self.config['WEATHER']['position']['y']-98,
			anchor_x='left', 
			anchor_y='top', 
			align='left',
			batch=self.batch)

		self.actualPressure = pyglet.text.Label(
			'', 
			font_name='Bree Serif', 
			font_size=14, 
			x=window.width-config['WEATHER']['position']['x']+100, 
			y=window.height-config['WEATHER']['position']['y']-95, 
			anchor_x='left', 
			anchor_y='top', 
			align='left',
			batch=self.batch)

		self.actualWindIcon = pyglet.text.Label(
			'e',
			font_name='fontello', 
			font_size=14, 
			x=self.window.width-self.config['WEATHER']['position']['x']+200,
			y=self.window.height-self.config['WEATHER']['position']['y']-98,
			anchor_x='left', 
			anchor_y='top', 
			align='left',
			batch=self.batch)

		self.actualWind = pyglet.text.Label(
			'', 
			font_name='Bree Serif', 
			font_size=14, 
			x=window.width-config['WEATHER']['position']['x']+220, 
			y=window.height-config['WEATHER']['position']['y']-95, 
			anchor_x='left', 
			anchor_y='top', 
			align='left',
			batch=self.batch)
		
		self.getWeather()


	def getWeather(self):
		weather = requests.get(self.api)
		self.weather = json.loads(weather.text)

		self.showWeather()


	def showWeather(self):
		actual=self.weather['list'][0]
		self.actualTemp.text='{:02.0f}{:s}'.format(actual['main']['temp'], '°C')
		self.actualWeather.text=str(actual['weather'][0]['description'])
		self.actualHumidity.text = '{:02.0f}{:s}'.format(actual['main']['humidity'], '%')
		self.actualPressure.text = '{:02.2f}{:s}'.format(actual['main']['pressure'], 'hPa')
		self.actualWind.text = '{:02.2f}{:s}'.format(actual['wind']['speed'], 's/m')
		
		pyglet.text.Label(
			self.getWeatherIcon(actual['weather'][0]['icon']),
			font_name='fontello', 
			font_size=36, 
			x=self.window.width-self.config['WEATHER']['position']['x']+175, 
			y=self.window.height-self.config['WEATHER']['position']['y']-15,
			anchor_x='left', 
			anchor_y='top', 
			align='left',
			batch=self.batch)

		self.showForecast()


	def showForecast(self):
		l = [1,2,3,6,10,14,20]
		index=0;
		offsetStart=100
		for item in l:
			index=index+1
			offset=23*index
			pyglet.text.Label(
				datetime.strptime(self.weather['list'][item]['dt_txt'], '%Y-%m-%d %H:%M:%S').strftime('%a %H:%M'), 
				font_name='Bree Serif', 
				font_size=16, 
				x=self.window.width-self.config['WEATHER']['position']['x'], 
				y=self.window.height-self.config['WEATHER']['position']['y']-offsetStart-offset, 
				anchor_x='left', 
				anchor_y='top', 
				align='left',
				batch=self.batch)
			pyglet.text.Label(
				'{:02.0f}{:s}'.format(self.weather['list'][item]['main']['temp'], '°C'),
				font_name='Bree Serif', 
				font_size=16, 
				x=self.window.width-self.config['WEATHER']['position']['x']+85, 
				y=self.window.height-self.config['WEATHER']['position']['y']-offsetStart-offset, 
				anchor_x='left', 
				anchor_y='top', 
				align='left',
				batch=self.batch)
			pyglet.text.Label(
				self.weather['list'][item]['weather'][0]['description'],
				font_name='Bree Serif', 
				font_size=16, 
				x=self.window.width-self.config['WEATHER']['position']['x']+150, 
				y=self.window.height-self.config['WEATHER']['position']['y']-offsetStart-offset, 
				anchor_x='left', 
				anchor_y='top', 
				align='left',
				batch=self.batch)

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