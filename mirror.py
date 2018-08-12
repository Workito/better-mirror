import pyglet
import time
import locale
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

window = pyglet.window.Window(fullscreen=True)

@window.event
def on_draw():
    window.clear()
    t.time.draw()
    t.date.draw()


class T:
    def __init__(self, *args, **kwargs):
        self.time = pyglet.text.Label('', font_name='Times New Roman', font_size=90, x=1300, y=900)
        self.date = pyglet.text.Label('', font_name='Times New Roman', font_size=50, x=1310, y=800)
        self.tick()

    def tick(self, *args):
        self.time.text=time.strftime('%H:%I:%S')
        self.date.text=time.strftime('%a %d.%m.%Y')

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, 'cs_CZ.UTF-8')
    t = T()
    pyglet.clock.schedule_interval_soft(t.tick, 1)
    pyglet.app.run()
