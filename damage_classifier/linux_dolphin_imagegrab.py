"""
Grabs up to 300 screenshots of display at rate of one screenshot per second from
start of program. Screenshots saved in same folder, named 0-x.png

Usage: open dolphin with melee, start program immediately after round starts,
kill program immediately after round ends.
"""

import time

import gtk.gdk

WIN = gtk.gdk.get_default_root_window()
W, H = WIN.get_size()
pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, W, H)

for i in xrange(300):
    pb = pb.get_from_drawable(WIN, WIN.get_colormap(), 0, 0, 0, 0, W, H)
    pb.save("%s.png" % str(i), "png")

    time.sleep(1)
