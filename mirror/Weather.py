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
		self.api = 'https://api.openweathermap.org/data/2.5/forecast?q={:s}&appid={:s}&units=metric&lang=cz'.format(config['WEATHER']['city'], config['WEATHER']['api'])

		self.actualTemp = pyglet.text.Label(
            '', 
            font_name='Bree Serif', 
            font_size=60, 
            x=window.width-config['WEATHER']['position']['x'], 
            y=window.height-config['WEATHER']['position']['y'], 
            anchor_x='left', 
            anchor_y='top', 
            align='left')
		self.actualWeather = pyglet.text.Label(
            '', 
            font_name='Bree Serif', 
            font_size=20, 
            x=window.width-config['WEATHER']['position']['x']+180, 
            y=window.height-config['WEATHER']['position']['y']-55, 
            anchor_x='left', 
            anchor_y='top', 
            align='left')
		self.forecastTime = []
		self.forecastTemp = []
		self.forecastCloud = []
		
		self.getWeather()


	def getWeather(self):
		weather = requests.get(self.api)
		self.weather = json.loads(weather.text)

		self.showWeather()


	def showWeather(self):
		actual=self.weather['list'][0]
		self.actualTemp.text='{:02.0f}{:s}'.format(actual['main']['temp'], '°C')
		self.actualWeather.text=str(actual['weather'][0]['description'])
		pic = pyglet.image.load('./static/weather/{:s}.png'.format(actual['weather'][0]['icon']))
		self.pic = pic.get_texture()
		self.pic.width=50;
		self.pic.height=50;

		pic=pyglet.image.load('./static/weather/humidity.png')
		self.picHumidity=pic.get_texture()
		self.picHumidity.width=20;
		self.picHumidity.height=20;

		self.showForecast()


	def showForecast(self):
		l = [1,2,3,6,10,14,20]
		index=0;
		offsetStart=100
		for item in l:
			index=index+1
			offset=23*index
			self.forecastTime.append(pyglet.text.Label(
				datetime.strptime(self.weather['list'][item]['dt_txt'], '%Y-%m-%d %H:%M:%S').strftime('%a %H:%M'), 
				font_name='Bree Serif', 
				font_size=16, 
				x=self.window.width-self.config['WEATHER']['position']['x'], 
				y=self.window.height-self.config['WEATHER']['position']['y']-offsetStart-offset, 
				anchor_x='left', 
				anchor_y='top', 
				align='left'))
			self.forecastTemp.append(pyglet.text.Label(
				'{:02.0f}{:s}'.format(self.weather['list'][item]['main']['temp'], '°C'),
				font_name='Bree Serif', 
				font_size=16, 
				x=self.window.width-self.config['WEATHER']['position']['x']+85, 
				y=self.window.height-self.config['WEATHER']['position']['y']-offsetStart-offset, 
				anchor_x='left', 
				anchor_y='top', 
				align='left'))
			self.forecastCloud.append(pyglet.text.Label(
				self.weather['list'][item]['weather'][0]['description'],
				font_name='Bree Serif', 
				font_size=16, 
				x=self.window.width-self.config['WEATHER']['position']['x']+150, 
				y=self.window.height-self.config['WEATHER']['position']['y']-offsetStart-offset, 
				anchor_x='left', 
				anchor_y='top', 
				align='left'))


	def draw(self):
		self.actualTemp.draw()
		self.actualWeather.draw()
		self.pic.blit(self.window.width-self.config['WEATHER']['position']['x']+175,self.window.height-self.config['WEATHER']['position']['y']-65)
		self.picHumidity.blit(self.window.width-self.config['WEATHER']['position']['x'],self.window.height-self.config['WEATHER']['position']['y']-115)
		for i in self.forecastTime:
			i.draw()
		for i in self.forecastTemp:
			i.draw()
		for i in self.forecastCloud:
			i.draw()