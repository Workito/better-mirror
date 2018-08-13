#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
import locale
import sys
import json

from DateTime import *
from Weather import *

reload(sys)
sys.setdefaultencoding('utf-8')

with open('./config.json', 'r') as f:
    config = json.load(f)

window = pyglet.window.Window(fullscreen=True)

pyglet.font.add_file('./static/font/BenchNine.ttf')
BenchNine = pyglet.font.load('BenchNine')

@window.event
def on_draw():
    window.clear()
    dateTiem.draw()


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, 'cs_CZ.UTF-8')
    dateTiem = DateTime(window, config)
    weather = Weather(window, config)
    pyglet.clock.schedule_interval_soft(dateTiem.tick, 1)
    pyglet.app.run()
