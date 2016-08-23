import gtk.gdk as gdk
import time


w = gdk.screen_width()
h = gdk.screen_height()

sg = gdk.Pixbuf(gdk.COLORSPACE_RGB, False, 8, w, h)

start = time.clock()

pb = sg.get_from_drawable(gdk.get_default_root_window(),
                          gdk.colormap_get_system(),
                          0,0,0,0,
                          w, h)

print(time.clock() - start)


