"""
Grabs up to 300 screenshots of display at rate of one screenshot per second from
start of program. Screenshots saved in same folder, named 0-x.png

Usage: open dolphin with melee, start program immediately after round starts,
kill program immediately after round ends.
"""

import time

import gtk.gdk
import classifier_constants as cc

WIN = gtk.gdk.get_default_root_window()

pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, cc.WIDTH, cc.HEIGHT)

for i in xrange(cc.NUM_IMAGE_GRAB):
    pb = pb.get_from_drawable(WIN, WIN.get_colormap(), 0, 0, 0, 0,
            cc.WIDTH, cc.HEIGHT)
    pb.save("%s/%s.png" % (cc.PATH_TO_DATA, str(i)), "png")

    time.sleep(1)
