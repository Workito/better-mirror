#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
import feedparser

from Helper import *

class News:
	def __init__(self, window, config):
		self.config = config
		self.window = window
		self.batch = pyglet.graphics.Batch()

		self.getNews()


	def getNews(self):
		feed = feedparser.parse(self.config['NEWS']['feed'])

		index = 0
		for post in feed.entries[1:6]:
			Helper.label(self, post.title, 12, 0, -index * 17, self.batch, self.window, self.config['NEWS'])
			index = index + 1


	def draw(self):
		self.batch.draw()