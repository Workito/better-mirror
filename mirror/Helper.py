#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
import json

class Helper:
	_webcnf = None

	@staticmethod
	def label(self, text, size, x, y, batch, window, config, useIcon = False, shadow = False):
		font = 'Bree Serif'
		if useIcon:
			font = 'fontello'

		color = (255, 255, 255, 255)
		if shadow:
			color = (155, 155, 155, 155)

		return pyglet.text.Label(
			text,
			color = color,
			font_name = font,
			font_size = size,
			x = window.width - config['position']['x'] + x,
			y = window.height - config['position']['y'] + y,
			anchor_x = 'left',
			anchor_y = 'top',
			align = 'left',
			batch = self.batch)


	@staticmethod
	def getWebConfig(self, refresh = False):
		if refresh or Helper._webcnf == None:
			with open('./web-config.json', 'r') as f:
				Helper._webcnf = json.load(f)

		return Helper._webcnf
