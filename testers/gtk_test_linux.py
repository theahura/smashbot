import gtk.gdk
import numpy as np

# Diagnostic
from matplotlib import pyplot as plt
import time

win = gtk.gdk.get_default_root_window()
w, h = win.get_size()
pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,w,h)

plot = None
f = plt.figure()
ax = f.gca()
f.show()
plt.ion()

start = time.clock()

for _ in xrange(1000):
    pb = pb.get_from_drawable(win,win.get_colormap(),0,0,0,0,w,h)
    pix_arr = np.fromstring(pb.get_pixels(), dtype=np.uint8)

    # Restructure the screenshot
    im_arr = np.reshape(pix_arr, (h, w, 3))
    if not plot:
        plot = plt.imshow(im_arr)
    else:
        plot.set_data(im_arr)
        f.canvas.draw()

print time.clock() - start
