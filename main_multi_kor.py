# Blue Archive Reset Marathon (Multi Barrack, Korean)
# Github : Dark-Lemon7z
# Arcalive : 몰루라이브
# Tistory : lemon7z.tistory.com/
# Last Edited 2021-11-09

#import
from ppadb.client import Client as AdbClient
from PIL import Image
import pyautogui
import time
import win32gui
import win32ui
import win32con
import random
import sys
import os

deviceport = sys.argv[1]
devnum = sys.argv[2]
print("###############################")
print("# Blue Archive Reset Marathon #")
print("# 2021-11-10 #  Korea Server  #")
print("# Arcalive : 몰루라이브       #")
print("###############################")
print("Device : " + devnum +'\n'+ "Port : " + deviceport)

# adb settings
client = AdbClient(host="127.0.0.1", port=5037)
client.remote_connect("localhost", int(deviceport))
adbdevice = client.device("localhost:"+str(deviceport))
if adbdevice is not None:
    print("Adb detected")
else:
    print("Adb not detected")
    exit(0)

#defines
def click(x, y, dx, dy):
    newy = y - 32
    xx = random.randint(x, x + dx)
    yy = random.randint(newy, newy + dy)
    cmd = "input touchscreen tap " + str(xx) + " " + str(yy)
    adbdevice.shell(cmd)
def clickd(x1, y1, x2, y2):
    newy1 = y1 - 32
    newy2 = y2 - 32
    x = random.randint(x1, x2)
    y = random.randint(newy1, newy2)
    cmd = "input touchscreen tap " + str(x) + " " + str(y)
    adbdevice.shell(cmd)
def background_screenshot(hwnd, width, height):
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(width, height) , dcObj, (0,0), win32con.SRCCOPY)
    bmpinfo = dataBitMap.GetInfo()
    bmpstr = dataBitMap.GetBitmapBits(True)
    im = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    return im
def onlyclickhere(img):
    while 1:
        randsleep(0.15,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.1,0.3)
            click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
            randsleep(0.1,0.3)
            print("OK")
            break
def randsleep(x,y):
    dx = x * 1000
    dy = y * 1000
    timed = random.randint(dx,dy) / 1000
    time.sleep(timed)
def scriptskip():
    # time.sleep(0.3)
    while 1:
        randsleep(0.05,0.15)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_menu, scr_img, confidence=0.8)
        if clickhere is not None:
            break
    while 1:  # skip button
        randsleep(0.1,0.15)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_skip, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.05,0.1)
            click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
            while 1:  # OK
                randsleep(0.15,0.3)
                scr_img = background_screenshot(bluestackhw, 960, 572)
                clickhere = pyautogui.locate(img_ok, scr_img, confidence=0.8)
                if clickhere is not None:
                    randsleep(0.2,0.4)
                    clickd(500, 400, 630, 430)
                    randsleep(0.1,0.3)
                    clickd(500, 400, 630, 430)
                    randsleep(0.1,0.3)
                    break
                clickhere = pyautogui.locate(img_menu, scr_img, confidence=0.8)
                if clickhere is not None:
                    scriptskip()
                    break
            break
        elif clickhere is None:
            clickd(857,48,926,61)
            randsleep(0.1,0.2)
def stagefine():
    while 1:  # stage fine
        randsleep(0.15,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_stageok, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(1,1.3)
            click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
            randsleep(0.1,0.3)
            click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
            randsleep(0.1,0.3)
            click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
            randsleep(0.1,0.3)
            click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
            randsleep(0.1,0.3)
            break
def init():
    x0, y0, x1, y1 = win32gui.GetWindowRect(bluestackhw)
    win32gui.MoveWindow(bluestackhw, x0, y0, 992, 572, True)
    print("reset")
    print("waiting...")

#variables
cycle = 1
img_menumain = Image.open("menumain.bmp")
# img_networkerr = Image.open("networkerr.bmp")
img_menu = Image.open("menu.bmp")
img_cancle = Image.open("cancle.bmp")
img_guest = Image.open("guest.bmp")
img_ok = Image.open("ok.bmp")
img_senseiok = Image.open("senseiok.bmp")
img_yeondong = Image.open("yeondong.bmp")
img_stageok = Image.open("stageok.bmp")
img_onamae = Image.open("onamae.bmp")
img_systemsay = Image.open("systemsay.bmp")
img_playstore = Image.open("playstore.bmp")
img_skip = Image.open("skip.bmp")
img_skillexp = Image.open("skillcard_exp.bmp")
img_skillexp2 = Image.open("skillcard_exp2.bmp")
img_skillexp3 = Image.open("skillcard_exp3.bmp")
img_skill1 = Image.open("skill1.bmp")
img_skill2 = Image.open("skill2.bmp")
img_freegyacha = Image.open("freegyacha.bmp")
img_ingyacha = Image.open("ingyacha.bmp")
img_tutogyachaok = Image.open("tutogyachaok.bmp")
img_gachafine = Image.open("gachafine.bmp")
img_darkok = Image.open("darkok.bmp")
img_darkmain = Image.open("darkmainchar.bmp")
img_kanji = Image.open("kanji.bmp")
img_darkent = Image.open("darkent.bmp")
img_prepare = Image.open("prepare.bmp")
img_darkgogo = Image.open("darkgogo.bmp")
img_darkteam = Image.open("darkteam.bmp")
img_start = Image.open("start.bmp")
img_boss = Image.open("boss.bmp")
img_auto = Image.open("auto.bmp")
img_yellowok = Image.open("yellowok.bmp")
img_robihe = Image.open("robihe.bmp")
img_append = Image.open("append.bmp")
img_momotalk = Image.open("momotalk.bmp")
img_momotalkclose = Image.open("momotalkclose.bmp")
img_allreciv = Image.open("allreciv.bmp")
img_allrecivfine = Image.open("allrecivfine.bmp")
img_account = Image.open("account.bmp")
img_instudent = Image.open("instudent.bmp")
img_accountsetting = Image.open("accountsetting.bmp")
img_bluearchive = Image.open("bluearchive.bmp")
img_2roundsay = Image.open("2roundsay.bmp")
img_2roundsay2 = Image.open("2roundsay2.bmp")
img_news = Image.open("news.bmp")
img_missionok = Image.open("missionok.bmp")
img_mainchar = Image.open("mainchar.bmp")
img_everyday = Image.open("everyday.bmp")
img_devicecode = Image.open("devicecode.bmp")
img_codegen = Image.open("codegen.bmp")
img_point = Image.open("point.bmp")
img_pointfront = Image.open("pointfront.bmp")
img_prepareCode = Image.open("prepareCode.bmp")
# devnum = int(input())
bluestackhw = win32gui.FindWindow(None, "BlueStacks " + str(devnum))

def gacha(tm, rst):
    gachacycle = 2
    merged = Image.new('RGBA', (960 * gachacycle, 572))
    merged.paste(rst, (0,0))
    while 1:
        temp = Image.new('RGBA', (960 * gachacycle, 572))
        temp.paste(merged, (0,0))
        merged = temp
        print("Touch Everyday Gacha", end="....")
        while 1:
            randsleep(0.1, 0.3)
            scr_img = background_screenshot(bluestackhw, 960, 572)
            clickhere = pyautogui.locate(img_everyday, scr_img, confidence=0.8)
            clickd(620, 140, 710, 160)
            if clickhere is not None:
                randsleep(0.4, 0.5)
                # clickd(536,397,639,434)
                clickd(737, 400, 888, 444)
                print("OK")
                break
        print("Touch gacha ok", end="....")
        while 1:  # touch gacha ok
            randsleep(0.15, 0.3)
            scr_img = background_screenshot(bluestackhw, 960, 572)
            clickhere = pyautogui.locate(img_tutogyachaok, scr_img, confidence=0.8)
            if clickhere is not None:
                time.sleep(0.1)
                scr_img = background_screenshot(bluestackhw, 960, 572)
                clickhere = pyautogui.locate(img_gachafine, scr_img, confidence=0.8)
                if clickhere is not None:
                    clickd(319, 391, 440, 420)
                    randsleep(0.1, 0.3)
                    clickd(319, 391, 440, 420)
                    cmd = 'Codes\\' + str(tm.tm_hour) + str(tm.tm_min) + str(tm.tm_sec) + '_' + str(devnum) + 'gacha.png'
                    merged.save(cmd)
                    return
                randsleep(0.5, 0.7)
                randsleep(1, 1.3)
                clickd(500, 380, 640, 420)
                randsleep(0.1, 0.3)
                clickd(500, 380, 640, 420)
                randsleep(0.1, 0.3)
                clickd(500, 380, 640, 420)
                randsleep(0.1, 0.3)
                clickd(500, 380, 640, 420)
                randsleep(0.1, 0.3)
                print("OK")
                break
        print("Sign", end="....")
        while 1:  # sign
            randsleep(0.15, 0.3)
            clickd(324, 367, 647, 500)
            scr_img = background_screenshot(bluestackhw, 960, 572)
            clickhere = pyautogui.locate(img_ingyacha, scr_img, confidence=0.8)
            if clickhere is not None:
                randsleep(0.5, 0.7)
                clickd(324, 367, 647, 500)
                randsleep(0.1, 0.2)
                clickd(324, 367, 647, 500)
                randsleep(0.1, 0.2)
                print("OK")
                break
        while 1:
            randsleep(0.1, 0.3)
            clickd(849, 55, 920, 75)
            scr_img = background_screenshot(bluestackhw, 960, 572)
            clickhere = pyautogui.locate(img_point, scr_img, confidence=0.8)
            if clickhere is not None:
                time.sleep(0.7)
                print("Screen captured")
                scr_gacha_img = background_screenshot(bluestackhw, 960, 572)
                merged.paste(scr_gacha_img, (960*(gachacycle-1), 0))
                break

        print("In gacha", end="....")
        while 1:
            randsleep(0.1, 0.3)
            clickd(849, 55, 920, 75)
            scr_img = background_screenshot(bluestackhw, 960, 572)
            clickhere = pyautogui.locate(img_ok, scr_img, confidence=0.8)
            if clickhere is not None:
                randsleep(0.1, 0.3)
                clickd(418, 483, 460, 523)
                randsleep(0.1, 0.3)
                clickd(418, 483, 460, 523)
                randsleep(0.1, 0.3)
                clickd(418, 483, 460, 523)
                randsleep(0.1, 0.3)
                clickd(418, 483, 460, 523)
                randsleep(0.1, 0.3)
                print("OK")
                break
        print("Fine gacha", end="....")
        while 1:
            randsleep(0.1, 0.3)
            clickd(418, 483, 460, 523)
            scr_img = background_screenshot(bluestackhw, 960, 572)
            clickhere = pyautogui.locate(img_everyday, scr_img, confidence=0.8)
            if clickhere is not None:
                print("OK")
                break
        gachacycle += 1

#main activity
def resetmara():
    # init
    init()
    tm = time.localtime(time.time())
    print("Account manage", end="....")
    while 1:  # TOUCH TO START
        clickd(920, 53,921,66)
        randsleep(0.3,0.4)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_account, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.1, 0.3)
            clickd(495, 270, 634,301)
            randsleep(0.1, 0.3)
            print("OK")
            break

    while 1:
        randsleep(0.1,0.15)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_accountsetting, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.1, 0.3)
            clickd(641, 289, 644,311)
            randsleep(0.1, 0.3)
            clickd(641, 289, 644,311)
            randsleep(0.1, 0.3)
            clickd(641, 289, 644,311)
            randsleep(0.1, 0.3)
            print("OK")
            break
    while 1:
        randsleep(0.1,0.15)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_bluearchive, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.1, 0.3)
            clickd(427, 274, 521,286)
            randsleep(0.1, 0.3)
            adbdevice.shell("input text \"BlueArchive\"")
            randsleep(0.1, 0.3)
            clickd(500, 383, 515,413)
            randsleep(0.1, 0.3)
            clickd(500, 383, 515,413)
            print("OK")
            break
    while 1:
        randsleep(0.1,0.15)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_ok, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.3, 0.4)
            clickd(500, 383, 515,413)
            randsleep(0.1, 0.15)
            clickd(500, 383, 515,413)
            randsleep(0.1, 0.15)
            clickd(500, 383, 515,413)
            print("OK")
            break






    print("Touch start", end="....")
    while 1:  # TOUCH TO START
        randsleep(0.15,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_menumain, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.5,0.7)
            clickd(100, 200,700,400)
            print("OK")
            break
        clickhere = pyautogui.locate(img_playstore, scr_img, confidence=0.7)
        if clickhere is not None:
            randsleep(0.15, 0.3)
            adbdevice.shell("am start -n com.nexon.bluearchive/com.nexon.bluearchive.MxUnityPlayerActivity")
            print("Force Quited Restart")
            continue
    print("Touch Hazimemashite ok", end="....")
    while 1:  # touch hazimemashite's ok
        randsleep(0.15,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_ok, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.3,0.5)
            clickd(406, 388,530,430)
            randsleep(0.1,0.3)
            clickd(406, 388,530,430)
            randsleep(0.1,0.3)
            print("OK")
            break
        clickhere = pyautogui.locate(img_playstore, scr_img, confidence=0.9)
        if clickhere is not None:
            randsleep(0.15, 0.3)
            adbdevice.shell("am start -n com.nexon.bluearchive/com.nexon.bluearchive.MxUnityPlayerActivity")
            print("Force Quited Restart")
            while 1:  # TOUCH TO START
                randsleep(0.15, 0.3)
                scr_img = background_screenshot(bluestackhw, 960, 572)
                clickhere = pyautogui.locate(img_menumain, scr_img, confidence=0.8)
                if clickhere is not None:
                    randsleep(0.5, 0.7)
                    clickd(100, 200, 700, 400)
                    print("MOK")
                    break
    print("Write name", end="....")

    while 1:  # write name
        randsleep(0.15,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_onamae, scr_img, confidence=0.8)
        if clickhere is not None:
            clickd(405, 297, 524, 320)
            randsleep(0.1,0.3)
            adbdevice.shell("input text \"a\"")
            randsleep(0.1,0.3)
            clickd(800, 480,801,481)  # typing end
            randsleep(0.3,0.6)
            clickd(400, 380,533,419)  # OK
            randsleep(0.1,0.3)
            clickd(400, 380,533,419)  # OK
            randsleep(0.1,0.3)
            print("OK")
            break
    print("Passing sensei name confirm", end="....")
    while 1:   # touch sensei voice ok
        randsleep(0.4,0.45)
        clickd(418, 395,540,430)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_senseiok, scr_img, confidence=0.8)
        if clickhere is not None:
            clickd(418, 395,540,430)
            randsleep(0.1,0.3)
            clickd(418, 395,540,430)
            randsleep(0.1,0.3)
            clickd(418, 395,540,430)
            randsleep(0.1,0.3)
            print("OK")
            break

    print("Read 1st chat", end="....")
    while 1:  # touch systemsay (1st chat)
        randsleep(0.15,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_systemsay, scr_img, confidence=0.7)
        if clickhere is not None:
            for i in range(0, 10):
                clickd(855, 500,900,546)
                randsleep(0.1,0.3)
            print("OK")
            break

    print("Skip script", end="....")
    scriptskip()  # skip script

    print("-Started 1st stage-")

    print("Skip TMT", end="....")
    while 1:  # touch skill exp (1st chat)
        randsleep(0.15,0.2)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_skillexp, scr_img, confidence=0.9)
        if clickhere is not None:
            for i in range(0, 9):
                clickd(400, 200,700,400)
                randsleep(0.1,0.18)
            print("OK")
            break
    print("Skip TMT2", end="....")
    while 1:  # touch skill exp (2nd chat)
        randsleep(0.15,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_skillexp, scr_img, confidence=0.9)
        if clickhere is not None:
            for i in range(0, 4):
                clickd(400, 200,700,400)
                randsleep(0.1,0.18)
            break
    print("OK")
    print("Touch skill", end="....")
    while 1:  # touch skill2
        randsleep(0.15,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_skill2, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.1,0.3)
            click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
            randsleep(0.1,0.3)
            for i in range(0,random.randint(2,3)):
                clickd(700, 140,900,300)
                randsleep(0.1,0.3)
            break
    print("OK")
    print("Skip TMT3", end="....")
    while 1:  # touch skill exp (3rd chat)
        randsleep(0.15,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_skillexp, scr_img, confidence=0.9)
        if clickhere is not None:
            for i in range(0, 2):
                clickd(400, 200,700,400)
                randsleep(0.1,0.18)
            break
    print("OK")
    print("Touch skill", end="....")
    while 1:  # touch skill1
        randsleep(0.15,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_skill1, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.1,0.3)
            click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
            randsleep(0.1,0.3)
            for i in range(0,random.randint(2,3)):
                clickd(700, 140,900,300)
                randsleep(0.1,0.3)
                clickd(700, 140,900,300)
                randsleep(0.1,0.3)
            break
    print("OK")
    stagefine()
    print("-Stage Finished-")

    # 1st stage clear#
    print("Skip script", end="....")
    scriptskip()
    print("Skip script", end="....")
    scriptskip()
    print("OK")
    print("-2nd stage start-")
    # 2nd stage start#
    print("Skip TMT", end="....")
    while 1:  # touch tmt exp (1st chat)
        randsleep(0.15,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_skillexp, scr_img, confidence=0.9)
        if clickhere is not None:
            for i in range(0, 6):
                clickd(400, 200,700,400)
                randsleep(0.1,0.18)
            break
    print("OK")
    print("Skip Hasumi chat", end="....")
    scriptskip()
    print("OK")
    print("Touch skill", end="....")
    while 1:  # touch skill2
        randsleep(0.15,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_skill2, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.2,0.35)
            click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
            randsleep(0.1,0.3)
            click(clickhere[0], clickhere[1] - 100, clickhere[2], clickhere[3])
            randsleep(0.3,0.5)
            for i in range(0,random.randint(2,3)):
                click(clickhere[0], clickhere[1] - 100, clickhere[2], clickhere[3])
                randsleep(0.3,0.5)
                click(clickhere[0], clickhere[1] - 100, clickhere[2], clickhere[3])
                randsleep(0.3,0.5)
            break
    print("OK")
    print("Skip wokamo chat", end="....")
    # wokamo chat
    scriptskip()
    print("Touch skill", end="....")
    while 1:  # touch skill1
        randsleep(0.15,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_skill1, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.2,0.35)
            click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
            randsleep(0.1,0.3)
            click(clickhere[0], clickhere[1] - 100, clickhere[2], clickhere[3])
            randsleep(0.3,0.5)
            for i in range(0,random.randint(2,3)):
                click(clickhere[0], clickhere[1] - 100, clickhere[2], clickhere[3])
                randsleep(0.3,0.5)
                click(clickhere[0], clickhere[1] - 100, clickhere[2], clickhere[3])
                randsleep(0.3,0.5)
            break
    print("OK")
    print("Skip script", end="....")
    scriptskip()
    randsleep(0.3,0.5)
    print("Skip script", end="....")
    scriptskip()
    print("Skip TMT", end="....")
    while 1:  # touch tmt exp (2nd chat)
        randsleep(0.15,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_skillexp, scr_img, confidence=0.9)
        if clickhere is not None:
            for i in range(0, 4):
                clickd(400, 200,700,400)
                randsleep(0.1,0.18)
            clickd(639,472, 672,516)
            randsleep(0.2,0.3)
            clickd(600,80, 900,300)
            randsleep(0.2,0.3)
            clickd(600,80, 900,300)
            randsleep(0.2,0.3)
            break
    print("OK")
    print("Touch skill", end="....")
    while 1:  # touch skill2
        randsleep(0.15,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_skill2, scr_img, confidence=0.8)
        if clickhere is None:
            clickhere = pyautogui.locate(img_skill1, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.1,0.3)
            clickd(465, 98, 804, 335)
            randsleep(0.1,0.3)
            clickd(465, 98, 804, 335)
            randsleep(0.3,0.5)
            for i in range(0,random.randint(2,4)):
                clickd(465, 98, 804, 335)
                randsleep(0.3,0.5)
            break
    print("OK")
    # insert one more pic
    stagefine()
    print("-Stage finished-")
    # 2nd stage clear#

    scriptskip()
    randsleep(1,1.3)
    scriptskip()
    randsleep(1,1.3)
    randsleep(1,1.3)
    print("Skip anime", end="....")
    while 1:  # Skip anime
        randsleep(0.1, 0.2)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_darkmain, scr_img, confidence=0.8)
        clickd(517, 390,632,420)
        if clickhere is not None:
            clickd(517, 390,632,420)
            print("OK")
            break
    # tuto fine

    # lobby
    print("Touch gacha", end="....")
    while 1:  # touch gyacha
        randsleep(0.1,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_freegyacha, scr_img, confidence=0.8)
        clickd(670,490, 700,520)
        if clickhere is not None:
            randsleep(0.5,0.7)
            click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
            randsleep(0.1,0.3)
            break
    print("OK")
    print("Touch gacha ok", end="....")
    while 1:  # touch gacha ok
        randsleep(0.15,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_tutogyachaok, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(1,1.3)
            clickd(500, 380,640,420)
            randsleep(0.1,0.2)
            clickd(500, 380,640,420)
            randsleep(0.1,0.2)
            for i in range(0,random.randint(2,3)):
                clickd(500, 380,640,420)
                randsleep(0.1,0.2)
            print("OK")
            break
    print("Sign", end="....")
    while 1:  # sign
        randsleep(0.15,0.3)
        clickd(500, 380,640,420)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_ingyacha, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.5,0.7)
            for i in range(0,random.randint(2,3)):
                clickd(324, 367,647,500)
                randsleep(0.1,0.3)
            print("OK")
            break
    print("Capture gacha", end="....")
    while 1:
        randsleep(0.1,0.2)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_point, scr_img, confidence=0.8)
        clickd(849,55, 920,75)
        if clickhere is not None:
            time.sleep(0.7)
            gacha_result = background_screenshot(bluestackhw, 960, 572)
            print("OK")
            break
    print("In gacha", end="....")
    while 1:
        randsleep(0.1,0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_darkok, scr_img, confidence=0.8) #retake
        clickd(849,55, 920,75)
        if clickhere is not None:
            randsleep(0.1,0.3)
            clickd(420,482, 541,523)
            randsleep(0.1,0.3)
            for i in range(0,random.randint(3,5)):
                clickd(420,482, 541,523)
                randsleep(0.1,0.3)
            break
    print("OK")
    randsleep(2,2.3)
    print("Touch entrance", end="....")
    while 1:  # touch entrance
        randsleep(0.1, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_darkent, scr_img, confidence=0.85)
        if clickhere is not None:
            randsleep(1.5, 1.7)
            clickd(800, 196, 860, 228)
            randsleep(0.1, 0.3)
            for i in range(0,random.randint(2,3)):
                clickd(800, 196, 860, 228)
                randsleep(0.1, 0.3)
            break
    print("OK")
    print("Touch prepare", end="....")
    while 1:  # touch prepare
        randsleep(0.15, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_prepare, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.3, 0.6)
            clickd(617, 414, 747, 454)
            randsleep(0.1, 0.3)
            for i in range(0,random.randint(2,3)):
                clickd(617, 414, 747, 454)
                randsleep(0.1, 0.3)
            break
        clickd(800, 196, 860, 228)
    print("OK")
    print("Touch start", end="....")
    while 1:  # touch start
        randsleep(0.15, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_darkgogo, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.2, 0.35)
            clickd(361, 367, 408, 400)
            randsleep(0.1, 0.3)
            for i in range(0,random.randint(3,4)):
                clickd(361, 367, 408, 400)
                randsleep(0.1, 0.3)
            print("OK")
            break
    print("Touch team", end="....")
    print("OK")
    print("Close team window", end="....")
    while 1:  # wait to kanji window
        randsleep(0.1, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_kanji, scr_img, confidence=0.8)
        clickd(880, 167, 907, 168)
        if clickhere is not None:
            break
    while 1:
        randsleep(0.1, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_darkteam, scr_img, confidence=0.8)
        clickd(300, 40, 700, 80)
        if clickhere is not None:
            randsleep(0.1, 0.3)
            clickd(800, 500, 900, 553)
            randsleep(0.1, 0.3)
            for i in range(0,random.randint(2,3)):
                clickd(800, 500, 900, 553)
                randsleep(0.1, 0.3)
            break
    print("OK")
    print("Touch boss", end="....")
    while 1:  # touch start
        randsleep(0.15, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_boss, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(1, 1.3)
            for i in range(0,random.randint(2,3)):
                clickd(818, 509, 913, 540)
                randsleep(0.1, 0.3)
            break
    print("OK")
    print("Touch start", end="....")
    while 1:  # touch start
        randsleep(0.15, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_start, scr_img, confidence=0.7)
        if clickhere is not None:
            randsleep(0.1, 0.3)
            clickd(490, 358, 510, 376)
            randsleep(0.1, 0.3)
            clickd(490, 358, 510, 376)
            for i in range(0,random.randint(3,4)):
                randsleep(0.1, 0.3)
                clickd(490, 358, 510, 376)
            break
    print("OK")
    print("-Battle phase 1 started-")
    # battle phase 1
    print("Touch auto", end="....")
    while 1:  # touch auto
        randsleep(0.15, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_auto, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(2, 2.3)
            clickd(872, 527, 924, 544)
            randsleep(0.1, 0.3)
            break
    print("OK")
    stagefine()
    print("-Stage finished-")
    # battle phase 1 ended
    print("Touch ok", end="....")
    while 1:  # touch yellow ok
        randsleep(0.15, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_yellowok, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.1, 0.3)
            clickd(425, 509, 536, 538)
            randsleep(0.1, 0.3)
            break
    print("OK")
    print("Touch phase end", end="....")
    while 1:  # touch phase end
        randsleep(0.15, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_2roundsay, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.1, 0.3)
            for i in range(0,random.randint(3,4)):
                clickd(830, 514, 917, 544)
                randsleep(0.1, 0.3)
            break
    print("OK")
    print("Touch Boss", end="....")
    while 1:  # touch Boss
        randsleep(0.15, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_2roundsay2, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.1, 0.3)
            for i in range(0,random.randint(3,4)):
                clickd(562, 319, 582, 330)
                randsleep(0.1, 0.3)
            break
    print("OK")
    print("-Battle phase 2-")
    # battle phase 2
    stagefine()
    # # battel phase 2 ended
    # print("Touch yellow ok", end="....")
    # while 1:  # touch yellow ok
    #     randsleep(0.15, 0.3)
    #     scr_img = background_screenshot(bluestackhw, 960, 572)
    #     clickhere = pyautogui.locate(img_missionok, scr_img, confidence=0.8)
    #     if clickhere is not None:
    #         randsleep(0.7, 1)
    #         randsleep(0.7, 1)
    #         for i in range(0,random.randint(3,4)):
    #             click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
    #             randsleep(0.1, 0.3)
    #         break
    # print("OK")
    print("Touch robihe", end="....")
    while 1:  # touch robi he
        randsleep(0.1, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_robihe, scr_img, confidence=0.8)
        clickd(687, 446, 869, 517)
        if clickhere is not None:
            randsleep(0.5, 0.7)
            for i in range(0,random.randint(5,7)):
                clickd(342, 510, 442, 539)
                randsleep(0.1, 0.3)
            break
    print("OK")
    print("Wait append table", end="....")
    # append table
    while 1:
        randsleep(0.15, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_append, scr_img, confidence=0.8)
        if clickhere is not None:
            break
    print("OK")
    # print("Close notice", end="....")
    # while 1:
    #     randsleep(0.1, 0.3)
    #     scr_img = background_screenshot(bluestackhw, 960, 572)
    #     clickhere = pyautogui.locate(img_news, scr_img, confidence=0.8)
    #     clickd(840, 100, 856, 116)
    #     if clickhere is not None:
    #         randsleep(0.3, 0.5)
    #         clickd(840, 100, 856, 116)
    #         break
    # print("OK")
    print("Touch momotalk", end="....")
    randsleep(0.5, 0.7)
    while 1:  # touch momotalk
        randsleep(0.1, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_momotalk, scr_img, confidence=0.8)
        clickd(119, 114, 134, 154)
        if clickhere is not None:
            randsleep(0.1, 0.3)
            clickd(119, 114, 134, 154)
            randsleep(0.1, 0.3)
            clickd(119, 114, 134, 154)
            randsleep(0.1, 0.3)
            break
    print("OK")
    print("Touch momotalk close", end="....")
    while 1:  # touch momotalk close
        randsleep(0.1, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_momotalkclose, scr_img, confidence=0.8)
        clickd(110, 223, 141, 246)
        if clickhere is not None:
            randsleep(0.1, 0.3)
            clickd(110, 223, 141, 246)
            randsleep(0.1, 0.3)
            clickd(110, 223, 141, 246)
            randsleep(0.1, 0.3)
            clickd(824, 110, 842, 129)
            randsleep(0.1, 0.3)
            break
    print("OK")
    print("Touch mailbox", end="....")
    while 1:  # touch mailbox
        randsleep(0.15, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_mainchar, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.1, 0.3)
            clickd(836, 54, 866, 69)
            randsleep(0.1, 0.3)
            print("OK")
            break  # touch mail box
    print("OK")
    print("Touch allreciv", end="....")
    while 1:  # touch guest
        randsleep(0.15, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_allreciv, scr_img, confidence=0.8)
        if clickhere is not None:
            randsleep(0.5, 0.7)
            click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
            randsleep(0.1, 0.3)
            click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
            randsleep(0.1, 0.3)
            print("OK")
            break
    print("OK")
    print("Go home", end="....")
    while 1:  # touch go home
        randsleep(0.15, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_allrecivfine, scr_img, confidence=0.8)
        clickd(621, 115, 827, 444)
        if clickhere is not None:
            randsleep(0.4, 0.65)
            clickd(902, 39, 930, 60)
            randsleep(0.1, 0.2)
            clickd(902, 39, 930, 60)
            randsleep(0.1, 0.2)
            clickd(902, 39, 930, 60)
            randsleep(0.1, 0.2)
            break
    print("OK")
    print("Touch Student", end="....")
    while 1:
        randsleep(0.1, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_instudent, scr_img, confidence=0.8)
        clickd(241, 501, 269, 534)
        if clickhere is not None:
            randsleep(0.1, 0.2)
            click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
            randsleep(0.1, 0.2)
            click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
            randsleep(0.1, 0.2)
            click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
            randsleep(0.1, 0.2)
            click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
            break

    print("Touch Home", end="....")
    while 1:
        randsleep(0.07, 0.15)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_darkmain, scr_img, confidence=0.8)
        clickd(902, 39, 930, 60)
        if clickhere is not None:
            break

    print("Touch account", end="....")
    while 1:
        randsleep(0.1, 0.3)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_account, scr_img, confidence=0.8)
        clickd(890, 50, 920, 70)
        if clickhere is not None:
            randsleep(0.1, 0.3)
            clickd(495, 270, 634,301)
            randsleep(0.1, 0.3)
            break
    print("OK")
    # print("Touch mission", end="....")
    # while 1:  # touch mission
    #     randsleep(0.1, 0.2)
    #     scr_img = background_screenshot(bluestackhw, 960, 572)
    #     clickhere = pyautogui.locate(img_mainchar, scr_img, confidence=0.8)
    #     clickd(35, 192, 56, 225)
    #     if clickhere is not None:
    #         randsleep(0.1, 0.2)
    #         clickd(35, 192, 56, 225)
    #         randsleep(0.1, 0.3)
    #         print("OK")
    #         break
    # print("OK")
    # print("Touch allreciv", end="....")
    # while 1:  # touch allreciv
    #     randsleep(0.15, 0.3)
    #     scr_img = background_screenshot(bluestackhw, 960, 572)
    #     clickhere = pyautogui.locate(img_allreciv, scr_img, confidence=0.8)
    #     if clickhere is not None:
    #         randsleep(0.5, 0.7)
    #         click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
    #         randsleep(0.1, 0.3)
    #         click(clickhere[0], clickhere[1], clickhere[2], clickhere[3])
    #         randsleep(0.1, 0.3)
    #         print("OK")
    #         break
    print("Touch gacha", end="....")
    while 1:  # touch gacha
        randsleep(0.15, 0.3)
        clickd(902, 39, 930, 60)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_mainchar, scr_img, confidence=0.8)
        if clickhere is not None:
            clickd(902, 39, 930, 60)
            randsleep(0.3, 0.6)
            clickd(688, 500, 710, 532)
            randsleep(0.1, 0.3)
            clickd(688, 500, 710, 532)
            randsleep(0.1, 0.3)
            break
    while 1:  # touch gacha
        randsleep(0.15, 0.2)
        clickd(688, 500, 710, 532)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_pointfront, scr_img, confidence=0.8)
        if clickhere is not None:
            break
    gacha(tm, gacha_result)
    print("Touch Home", end="....")
    while 1:
        randsleep(0.07, 0.15)
        scr_img = background_screenshot(bluestackhw, 960, 572)
        clickhere = pyautogui.locate(img_mainchar, scr_img, confidence=0.8)
        clickd(902, 39, 930, 60)
        if clickhere is not None:
            print("-ended-")
            break

if __name__ == "__main__":
    while 1:
        print("###############################")
        print("# 대상 디바이스 번호 : " + sys.argv[2])
        print("# 리세 횟수 : " + str(cycle))
        print("###############################")
        cycle = cycle + 1
        resetmara()
        while 1:
            print("계속하시겠습니까? (y / n) : ")
            a = input()
            if a == 'y':
                break
            else:
                continue