#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
import time

class DateTime:
	def __init__(self, window, config):
		self.config = config
		self.batch = pyglet.graphics.Batch()
		self.time = pyglet.text.Label(
			'', 
			font_name='Bree Serif', 
			font_size=90, 
			x=window.width-config['DATETIME']['position']['x']-10, 
			y=window.height-config['DATETIME']['position']['y']+120, 
			anchor_x='left', 
			anchor_y='top', 
			align='left',
			batch=self.batch)
		self.date = pyglet.text.Label(
			'', 
			font_name='Bree Serif', 
			font_size=50, 
			x=window.width-config['DATETIME']['position']['x'], 
			y=window.height-config['DATETIME']['position']['y'], 
			anchor_x='left', 
			anchor_y='top', 
			align='left',
			batch=self.batch)

		self.tick()


	def tick(self, *args):
		self.time.text=time.strftime(self.config['DATETIME']['timeformat'])
		self.date.text=time.strftime(self.config['DATETIME']['dateformat'])


	def draw(self):
		self.batch.draw()