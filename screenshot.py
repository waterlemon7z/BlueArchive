import win32gui
import win32ui
import win32con
import pygetwindow
import numpy as np

def background_screenshot(hwnd, width, height):
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(width, height) , dcObj, (0,0), win32con.SRCCOPY)
    dataBitMap.SaveBitmapFile(cDC, 'screenshot.bmp')
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

if __name__ == "__main__":
    hwnd = win32gui.FindWindow(None, 'BlueStacks 3')
    x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
    win32gui.MoveWindow(hwnd, x0, y0, 992, 572, True)
    background_screenshot(hwnd, 960, 572)