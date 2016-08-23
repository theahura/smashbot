from PIL import ImageGrab
import time
import numpy as np

start = time.clock()
im = np.asarray(ImageGrab.grab())
print time.clock() - start
