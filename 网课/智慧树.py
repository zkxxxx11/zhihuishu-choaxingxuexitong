import requests
import win32gui
import win32con
import win32api
import win32clipboard as w

from selenium import webdriver
import time
from lxml import etree
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
def main():
    url='https://onlineexamh5new.zhihuishu.com/stuExamWeb.html#/webExamList/dohomework/19985/e9bAY2pX/K56P9AWw/2065845/5163/0'
    a=[{'domain': '.zhihuishu.com', 'httpOnly': False, 'name': 'CASLOGC', 'path': '/', 'secure': False, 'value': '%7B%22realName%22%3A%22%E7%AB%A0%E9%92%B6%22%2C%22myuniRole%22%3A0%2C%22myinstRole%22%3A0%2C%22userId%22%3A800069181%2C%22headPic%22%3A%22https%3A%2F%2Fimage.zhihuishu.com%2Fzhs%2Fablecommons%2Fdemo%2F201804%2F5e314c660d31448d94fc201d434ca736_s3.jpg%22%2C%22uuid%22%3A%22Vv45gY8y%22%2C%22mycuRole%22%3A0%2C%22username%22%3A%2204517999709842b1872b411dba1b6a67%22%7D'}, {'domain': '.zhihuishu.com', 'httpOnly': False, 'name': 'CASTGC', 'path': '/', 'secure': False, 'value': 'TGT-2908935-zB13wVw3zDmY0Aj6nFz2dNRYfcVgSBOO4houf2hP7TfXBIgMpg-passport.zhihuishu.com'}, {'domain': '.zhihuishu.com', 'httpOnly': False, 'name': 'o_session_id', 'path': '/', 'secure': False, 'value': 'E97F12AEF2CAF55C5A48585F243AB226'}]
    driver=webdriver.Chrome()
    driver.get(url)
    '''time.sleep(30)
    #输入账号密码
    print(driver.get_cookies())'''
    driver.delete_all_cookies()
    for cookie in a:
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)
    xx=[]

    driver.get(url)
    driver.maximize_window()
    driverwait = WebDriverWait(driver, 20)
    time.sleep(3)
   
   
    xx=driver.find_elements_by_xpath("//*[@class='subject_describe']/p")
    print(len(xx))
    for i in range(0,len(xx)):
        
        timu=xx[i].get_attribute('innerText')
        print('timu:',xx[i].get_attribute('innerText'))
        setText(timu)
        ctrlV()
        altS()
        time.sleep(1)
        ctrlC()
        time.sleep(1)
        cc=getText()
        cc=analyse(cc)
        cc=cc.strip()
        dui=[]
        cuo=[]
        dui=driver.find_elements_by_xpath('//*[contains(text(),"对")]')
        cuo=driver.find_elements_by_xpath('//*[contains(text(),"错")]')
        dui.remove(dui[0])
        dui.remove(dui[1])
        k=0
        '''for i in range(0,len(dui)):
            print('dui::::::',len(dui))
            #print(dui[i].get_attribute('innerText'))
            if len(dui[i].get_attribute('innerText'))!=1:
                dui.remove(dui[i])'''
        
        
        if '' in cc:
            kk=cc.split('')
            print(kk)
            for i, j in enumerate(kk):
                driver.find_element_by_xpath('//*[contains(text(),"' + j + '")]').click()
        elif '#' in cc:
            kk=cc.split('#')
            print(kk)
            for i, j in enumerate(kk):
                driver.find_element_by_xpath('//*[contains(text(),"' + j + '")]').click()
        elif '===' in cc:
            kk=cc.split('===')
            print(kk)
            for i, j in enumerate(kk):

                driver.find_element_by_xpath('//*[contains(text(),"' + j + '")]').click()
        elif ' --- ' in cc:
            kk=cc.split(' --- ')
            print(kk)
            for i, j in enumerate(kk):
                driver.find_element_by_xpath('//*[contains(text(),"' + j + '")]').click()
        else:
            if '错' in cc:
                driver.find_element_by_xpath(cuo[k]).click()
                k=k+1

            elif '对' in cc:
                driver.find_element_by_xpath(dui[k]).click()
                k=k+1
        
            
            else:
                driver.find_element_by_xpath('//*[contains(text(),"' + cc + '")]').click()

           
        print('next;;;;;;;;;;;;;')  
        
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()
def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return(d).decode('GBK')


def ctrlC1():
    time.sleep(1)
    pyautogui.moveTo(x=659, y=665, duration=1, tween=pyautogui.linear)
    pyautogui.doubleClick()
    time.sleep(1)
    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(67, 0, 0, 0)  # c键位码是67
    win32api.keybd_event(67, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(1)


def ctrlC():
    time.sleep(2)
    pyautogui.moveTo(x=696, y=535,duration=1, tween=pyautogui.linear)
    pyautogui.doubleClick()
    time.sleep(1)
    win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
    win32api.keybd_event(67,0,0,0)  #c键位码是67
    win32api.keybd_event(67,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(1)
    
    
def ctrlV():
    
    altS()
    time.sleep(3)
    
        # 模拟鼠标左键按下。
    
    win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
    win32api.keybd_event(86,0,0,0)  #v键位码是86
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
 
def altS():
    win32api.keybd_event(18, 0, 0, 0)    #Alt键位码
    win32api.keybd_event(83,0,0,0) #s键位码
    win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    win32api.keybd_event(83,0,win32con.KEYEVENTF_KEYUP,0)

def analyse(m):
    print(m)
    '''content=m.split('答案:')[1]
    content=content.split('如')[0]'''
    content=m.split('：')[2]
    content=content.split('?')[0]
    print(content)
    return content



main()
