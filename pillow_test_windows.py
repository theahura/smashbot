from PIL import ImageGrab
import numpy as np
import cProfile

cProfile.run('np.asarray(ImageGrab.grab())')

#im = ImageGrab.grab()
#im.show()
