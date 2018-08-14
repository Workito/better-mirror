#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
import json

class Helper:
	_webcnf = None

	@staticmethod
	def label(self, text, size, x, y, batch, window, config, useIcon = False):
		font = 'Bree Serif'
		if useIcon:
			font = 'fontello'

		return pyglet.text.Label(
			text,
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
