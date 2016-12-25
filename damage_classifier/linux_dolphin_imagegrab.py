"""
Grabs up to 300 screenshots of display at rate of one screenshot per second from
start of program. Screenshots saved in same folder, named 0-x.png

Usage: open dolphin with melee, start program immediately after round starts,
kill program immediately after round ends.
"""

import time

import gtk.gdk
import classifier_constants as cc

START_NAME = 2639

WIN = gtk.gdk.get_default_root_window()

pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, cc.GATHER_WIDTH,
                    cc.GATHER_HEIGHT)

for i in xrange(cc.NUM_IMAGE_GRAB):
    pb = pb.get_from_drawable(WIN, WIN.get_colormap(), 0, 0, 0, 0,
            cc.GATHER_WIDTH, cc.GATHER_HEIGHT)
    pb.save("%s/%s.png" % (cc.PATH_TO_DATA, str(i + START_NAME)), "png")

    print "captured image: %s" % str(i + START_NAME)

    time.sleep(cc.SECPERFRAME)
