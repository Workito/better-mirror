#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyglet
import locale
import sys

from DateTime import *
from Weather import *

reload(sys)
sys.setdefaultencoding('utf-8')

window = pyglet.window.Window(fullscreen=True)

@window.event
def on_draw():
    window.clear()
    dateTiem.draw()


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, 'cs_CZ.UTF-8')
    dateTiem = DateTime()
    weather = Weather()
    pyglet.clock.schedule_interval_soft(dateTiem.tick, 1)
    pyglet.app.run()
