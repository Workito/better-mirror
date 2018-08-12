#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
import time

pyglet.font.add_file('fonts/BenchNine.ttf')
BenchNine = pyglet.font.load('BenchNine')

class DateTime:
    def __init__(self):
        self.time = pyglet.text.Label('', font_name='BenchNine', font_size=90, x=1300, y=900)
        self.date = pyglet.text.Label('', font_name='BenchNine', font_size=50, x=1310, y=800)
        self.tick()

    def tick(self, *args):
        self.time.text=time.strftime('%H:%I:%S')
        self.date.text=time.strftime('%a %d.%m.%Y')

    def draw(self):
        self.time.draw()
        self.date.draw()