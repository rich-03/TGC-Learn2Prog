import pyglet
from pyglet import window

wn = pyglet.window.Window(width=800, height=600, caption="A Window")
Iml = pyglet.image.load('Lark Bunting.jpg')


@window.event
def on_mouse_press(x, y, button, modifiers):
    window.clear()
    Iml.blit(x, y)


pyglet.app.run()
