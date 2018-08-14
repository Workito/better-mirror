#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
import requests

import datetime
import time
import icalendar

from Helper import *


class MyCalendar:
	def __init__(self, window, config):
		self.config = config
		self.window = window
		self.batch = pyglet.graphics.Batch()
		self.calc = []
		
		self.getEventsFromCalendars()


	def getEventsFromCalendars(self):
		now = time.time()
		for calendar in self.config['CALENDAR']['icals']:
			icalfile = requests.get(calendar)
			cal = icalendar.Calendar.from_ical(icalfile.text)
			for component in cal.walk():
				if component.name == "VEVENT":
					summary = component.get('summary')
					description = component.get('description')
					location = component.get('location')
					startdt = component.get('dtstart').dt
					if time.mktime(startdt.timetuple()) >= now:
						if location == None:
							location = ""
						self.calc.append([time.mktime(startdt.timetuple()), startdt, summary, description, location])

		self.calc = sorted(self.calc, key=lambda x: x[0])
		self.drawCalendar()


	def drawCalendar(self):
		index = 0;
		for item in self.calc[0:10]:

			Helper.label(self, item[1].strftime('%d.%m.%Y'), 12, -90, -index * 40, self.batch, self.window, self.config['CALENDAR'])
			Helper.label(self, item[2], 12, 0, -index * 40, self.batch, self.window, self.config['CALENDAR'])
			Helper.label(self, item[4], 10, 0, -index * 40 - 18, self.batch, self.window, self.config['CALENDAR'])

			index = index + 1


	def draw(self):
		if Helper.getWebConfig(self)['active'] == 'True':
			self.batch.draw()