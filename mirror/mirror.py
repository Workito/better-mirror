#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet                                                           
from pyglet.gl import *
import locale
import sys
import json

from DateTime import *
from Weather import *

reload(sys)
sys.setdefaultencoding('utf-8')

with open('./config.json', 'r') as f:
    config = json.load(f)

c = pyglet.gl.Config(sample_buffers=1, samples=4)
window = pyglet.window.Window(config=c, fullscreen=True)

pyglet.font.add_file('./static/font/BreeSerif-Regular.ttf')
pyglet.font.load('Bree Serif')

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
    pyglet.app.run()
