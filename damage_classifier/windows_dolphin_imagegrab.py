import win32gui
import win32ui
import win32con
import numpy as np
np.set_printoptions(threshold=1000)

import time

windowname = 'doesntmatter'

w = 960
h = 510

hwnd = win32gui.FindWindow(None, windowname)
wDC = win32gui.GetWindowDC(hwnd)
dcObj = win32ui.CreateDCFromHandle(wDC)
cDC = dcObj.CreateCompatibleDC()

start = time.clock()

for i in xrange(300):
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0), (w,h), dcObj, (0,0), win32con.SRCCOPY)
    dataBitMap.SaveBitmapFile(cDC, str(i) + '.bmp')
    win32gui.DeleteObject(dataBitMap.GetHandle())
    time.sleep(1)

tot_time = time.clock() - start
print tot_time

dcObj.DeleteDC()
cDC.DeleteDC()
win32gui.ReleaseDC(hwnd, wDC)
