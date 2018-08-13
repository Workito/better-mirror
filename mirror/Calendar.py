#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
import requests
import time
import datetime
import icalendar
from Helper import *

class MyCalendar:
	def __init__(self, window, config):
		self.config = config
		self.window = window
		self.batch = pyglet.graphics.Batch()
		"""
		#Helper.label(self, 'test', 20, 0, 0, self.batch, self.window, self.config['CALENDAR'])
		index = 0;
		for cals in self.config['CALENDAR']['icals']:
			ics = requests.get(cals)
			cal = Calendar(ics.text)
			for event in cal.events:
				if event.begin.timestamp > time.time():
					index = index + 1
					Helper.label(self, '{:s} {:s}'.format(event.begin.humanize(), event.name), 20, 0, -index * 20, self.batch, self.window, self.config['CALENDAR'])
		"""


	def draw(self):
		self.batch.draw()