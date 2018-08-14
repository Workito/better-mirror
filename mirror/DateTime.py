#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
import time
import requests
import json

from Helper import *

class DateTime:
	def __init__(self, window, config):
		self.config = config
		self.batch = pyglet.graphics.Batch()

		self.time = Helper.label(self, '', 90, -10, 125, self.batch, window, config['DATETIME'])
		self.date = Helper.label(self, '', 50, 0, 0, self.batch, window, config['DATETIME'])
		self.nameDay = Helper.label(self, '', 15, 5, -80, self.batch, window, config['DATETIME'])

		self.tick()
		self.getNameDay()


	def tick(self, *args):
		Helper.getWebConfig(self, (int(time.strftime('%S'))%5))
		self.time.text = time.strftime(self.config['DATETIME']['timeformat'])
		self.date.text = time.strftime(self.config['DATETIME']['dateformat'])


	def getNameDay(self):
		nameDay = requests.get('https://api.abalin.net/get/today?country=cz');
		name = json.loads(nameDay.text)
		self.nameDay.text = 'dnes má svátek {:s}'.format(name['data']['name_cz'])


	def draw(self):
		if Helper.getWebConfig(self)['active'] == 'True':
			self.batch.draw()