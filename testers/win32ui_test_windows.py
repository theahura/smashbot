import win32gui
import win32ui
import win32con
import numpy as np
np.set_printoptions(threshold=1000)

# Diagnostic imports.
from matplotlib import pyplot as plt
import time

windowname = 'doesntmatter'

w = 650
h = 480

plot = None
f = plt.figure()
ax = f.gca()
f.show()
plt.ion()


hwnd = win32gui.FindWindow(None, windowname)
wDC = win32gui.GetWindowDC(hwnd)
dcObj = win32ui.CreateDCFromHandle(wDC)
cDC = dcObj.CreateCompatibleDC()

start = time.clock()

for _ in xrange(100):
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0), (w,h), dcObj, (0,0), win32con.SRCCOPY)
    data_arr = np.fromstring(dataBitMap.GetBitmapBits(True), dtype=np.uint8)
    # 3 => index to start splice, alpha of first pixel; 4 => step.
    # Removes all alpha.
    data_arr = np.absolute(np.delete(data_arr, slice(3, None, 4)))
    #data_arr = np.flipud(data_arr)

    win32gui.DeleteObject(dataBitMap.GetHandle())


    # Restructure the screenshot
    data_arr = np.reshape(data_arr, (h, w, 3))
    if not plot:
        plot = plt.imshow(data_arr)
    else:
        plot.set_data(data_arr)
        f.canvas.draw()

tot_time = time.clock() - start
print tot_time

dcObj.DeleteDC()
cDC.DeleteDC()
win32gui.ReleaseDC(hwnd, wDC)
