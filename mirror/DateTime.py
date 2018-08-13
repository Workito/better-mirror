#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
import time

from Helper import *

class DateTime:
	def __init__(self, window, config):
		self.config = config
		self.batch = pyglet.graphics.Batch()

		self.time = Helper.label(self, '', 90, -10, 120, self.batch, window, config['DATETIME'])
		self.date = Helper.label(self, '', 50, 0, 0, self.batch, window, config['DATETIME'])

		self.tick()


	def tick(self, *args):
		self.time.text = time.strftime(self.config['DATETIME']['timeformat'])
		self.date.text = time.strftime(self.config['DATETIME']['dateformat'])


	def draw(self):
		self.batch.draw()