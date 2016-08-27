import win32gui
import win32ui
import win32con

import time


windowname = 'Google Chrome (32 bit)'
w = 1000
h = 1000

hwnd = win32gui.FindWindow(None, windowname)
wDC = win32gui.GetWindowDC(hwnd)
dcObj = win32ui.CreateDCFromHandle(wDC)
cDC = dcObj.CreateCompatibleDC()
dataBitMap = win32ui.CreateBitmap()
dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
cDC.SelectObject(dataBitMap)

start = time.clock()

cDC.BitBlt((0,0), (w,h), dcObj, (0,0), win32con.SRCCOPY)
dataBitMap.SaveBitmapFile(cDC, 'test.bmp')

print time.clock() - start

dcObj.DeleteDC()
cDC.DeleteDC()
win32gui.ReleaseDC(hwnd, wDC)
win32gui.DeleteObject(dataBitMap.GetHandle())

