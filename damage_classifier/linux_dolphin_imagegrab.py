"""
Grabs up to 300 screenshots of display at rate of one screenshot per second from
start of program. Screenshots saved in same folder, named 0-x.png

Usage: open dolphin with melee, start program immediately after round starts,
kill program immediately after round ends.
"""

import gtk.gdk
import numpy as np
import time

win = gtk.gdk.get_default_root_window()
w, h = win.get_size()
pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,w,h)

for i in xrange(300):
    pb = pb.get_from_drawable(win,win.get_colormap(),0,0,0,0,w,h)
    pb.save("%s.png" % str(i), "png")

    time.sleep(1)
