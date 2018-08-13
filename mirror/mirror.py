#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
import locale
import sys
import json

pyglet.resource.path = ['../static/weather/']
pyglet.resource.reindex()

from Helper import *
from DateTime import *
from Weather import *

reload(sys)
sys.setdefaultencoding('utf-8')

with open('./config.json', 'r') as f:
    config = json.load(f)

window = pyglet.window.Window(fullscreen=True)

pyglet.font.add_file('./static/font/BreeSerif-Regular.ttf')
pyglet.font.add_file('./static/font/fontello.ttf')
pyglet.font.load('Bree Serif')
pyglet.font.load('fontello')

@window.event
def on_draw():
    window.clear()
    dateTiem.draw()
    weather.draw()


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, 'cs_CZ.UTF-8')
    dateTiem = DateTime(window, config)
    weather = Weather(window, config)
    pyglet.clock.schedule_interval_soft(dateTiem.tick, 1)
    pyglet.clock.schedule_interval_soft(weather.getWeather, 3600)
    pyglet.app.run()
