import pyscreenshot as ImageGrab
import numpy as np
import cProfile

if __name__ == '__main__':
    cProfile.run('np.asarray(ImageGrab.grab())')
