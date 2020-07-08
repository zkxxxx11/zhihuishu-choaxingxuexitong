import win32gui
import win32con
import win32api
import time
import win32clipboard as w
import requests
from selenium import webdriver
import time
from lxml import etree
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
def main():
    url='https://mooc1-1.chaoxing.com/mycourse/studentstudy?chapterId=151181282&courseId=206272791&clazzid=12506708&enc=4e576582fc4ea708974dff784f631286'
    a={'domain': '.chaoxing.com', 'httpOnly': False, 'name': 'thirdRegist', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.chaoxing.com', 'httpOnly': False, 'name': 'source', 'path': '/', 'secure': False, 'value': '""'}, {'domain': 'i.mooc.chaoxing.com', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', 'secure': False, 'value': '1B65E16A3181970AE561920ECBE7AEA4'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551542, 'httpOnly': False, 'name': 'DSSTASH_LOG', 'path': '/', 'secure': False, 'value': 'C_38-UN_287-US_58662822-T_1585811785279'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551518, 'httpOnly': False, 'name': 'xxtenc', 'path': '/', 'secure': False, 'value': '504a6c4001dc1bf61141ef58b4a2391d'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551283, 'httpOnly': False, 'name': 'pid', 'path': '/', 'secure': False, 'value': '33406'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551406, 'httpOnly': False, 'name': 'UID', 'path': '/', 'secure': False, 'value': '58662822'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551491, 'httpOnly': False, 'name': 'vc3', 'path': '/', 'secure': False, 'value': 'fEOkczcD9ygYFNQHNI26UZtVJqLXPlkjY3NAlScPXJf5sgHsw8g7NkOlXeNjJ2RLa3GLJtFuwO09cw6ff2kkugkecdKuRHmTBxmRzfGzvl5PSf%2BrZvH6RucSl212pkX%2BsAyFoik5%2FDx2OnB5lyCF4zB9qo3RdtUK3euAmtABk4I%3Dfba386d27d5286fd77606f34b8225906'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.55143, 'httpOnly': True, 'name': 'vc', 'path': '/', 'secure': False, 'value': '7A36C7F955C52F47A7473338E7D80331'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551163, 'httpOnly': False, 'name': 'uname', 'path': '/', 'secure': False, 'value': '201705021121'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551254, 'httpOnly': False, 'name': 'fid', 'path': '/', 'secure': False, 'value': '14'}, {'domain': '.chaoxing.com', 'expiry': 1585898184.462983, 'httpOnly': False, 'name': 'tl', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551382, 'httpOnly': False, 'name': '_d', 'path': '/', 'secure': False, 'value': '1585811785277'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551457, 'httpOnly': True, 'name': 'vc2', 'path': '/', 'secure': False, 'value': '17EE7776945DF03CFFA011F918E818C6'}, {'domain': 'i.mooc.chaoxing.com', 'httpOnly': False, 'name': 'route', 'path': '/', 'secure': False, 'value': '0d3ee366e02d727b7b6bb10aae7f99cf'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551225, 'httpOnly': False, 'name': 'lv', 'path': '/', 'secure': False, 'value': '2'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551345, 'httpOnly': False, 'name': 'uf', 'path': '/', 'secure': False, 'value': 'b2d2c93beefa90dcdd008caef2b6662d7b6b069153ed664b7a4fb73fc63758498780e57f42b1b031ad5ec19e2d94ddcd9b0594e13f4b452f9f4fcd6f19e32a2ed08218e4e8aff7ed0d8a4c92b12beb4b38556611397fefe18974337d24b1c5d746da21146a924e23'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551314, 'httpOnly': False, 'name': '_uid', 'path': '/', 'secure': False, 'value': '58662822'}
    driver=webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="unameId"]').send_keys('15988083991')
    driver.find_element_by_xpath('//*[@id="passwordId"]').send_keys('xh687991')
    driver.maximize_window()

    a=driver.find_element_by_xpath('//*[@id="fid"]')
    print(a,a.is_displayed())
    driver.execute_script("arguments[0].setAttribute (arguments[1],arguments[2])", a, 'value',
                          '11158')

    driverwait = WebDriverWait(driver, 20)
    #输入验证码
    time.sleep(5)


    all = driver.find_elements_by_xpath('//div/h4/span[2]')
    all.remove(all[0])
    
    title = driver.find_elements_by_xpath('//div/h4/a')
    title.remove(title[0])
    
    print(len(title))
    for j,i in enumerate(title):

        if '小组' in i.get_attribute('innerText'):
            title.remove(title[j])
            all.remove(all[j])

    print(len(title))


    for j,i in enumerate(all):

        print(i.text)
        if i.text=='1':
            title[j].click()


            break


    chaozuo(driver)
    while True:

        driver.switch_to.default_content()
        time.sleep(2)

        all = driver.find_elements_by_xpath('//div/h4/span[2]')
        all.remove(all[0])
        title = driver.find_elements_by_xpath('//div/h4/a')
        title.remove(title[0])
        print(len(title))
        for j,i in enumerate(title):

            if '小组' in i.get_attribute('innerText'):
                title.remove(title[j])
                all.remove(all[j])


        for j, i in enumerate(all):

            print('::::',i.text)
            if i.text == '1':
                title[j].click()

                break

        chaozuo(driver)

def chaozuo(driver):
    
    time.sleep(2)
    if driver.find_elements_by_id('dct2')!=[]:
        driver.find_element_by_id('dct2').click()
    time.sleep(2)
    driver.switch_to.frame('iframe')
    driver.switch_to.frame(0)
    driver.switch_to.frame(0)
    
    ct=driver.find_elements_by_xpath('//*[@class="TiMu"]/div[1]/div')

    k=0
    for i in ct:

        timu=i.get_attribute('innerText')
        leix=timu[:4]
        print('timu:', timu)
        print('leix:',leix)
        setText(timu)
        ctrlV()
        altS()
        time.sleep(1)
        ctrlC()
        time.sleep(1)
        cc=getText()


        cc=analyse(getText())
        cc=cc.strip()
        print(cc)
        if leix=='【判断题':



            if cc == "正确":
                print('cc::',cc)
                a = driver.find_elements_by_xpath('//*[contains(@value,"true")]')
                i.find_elements_by_xpath('//*[contains(@value,"true")]')[k].click()
                print('lenlen::',len(a))
            elif cc=="√":
                a = driver.find_elements_by_xpath('//*[contains(@value,"true")]')
                i.find_elements_by_xpath('//*[contains(@value,"true")]')[k].click()
                print('lenlen::', len(a))
            elif cc=="是":
                a = driver.find_elements_by_xpath('//*[contains(@value,"true")]')
                i.find_elements_by_xpath('//*[contains(@value,"true")]')[k].click()
                print('lenlen::', len(a))
            else:
                a = driver.find_elements_by_xpath('//*[contains(@value,"false")]')
                i.find_elements_by_xpath('//*[contains(@value,"false")]')[k].click()
                print('lenlen::',len(a))

            k=k+1
        elif leix=='【单选题':
            if 'C' in cc:
                i.find_element_by_xpath('//*[contains(@value,"C")]').click()
            elif 'A'in cc:
                i.find_element_by_xpath('//*[contains(@value,"A")]').click()
            elif 'B'in cc:
                i.find_element_by_xpath('//*[contains(@value,"B")]').click()
            elif 'D'in cc:
                i.find_element_by_xpath('//*[contains(@value,"D")]').click()
           

           

           
                

            else:
              
                print('cc::',cc)
                driver.find_element_by_xpath('//*[contains(text(),"' + cc + '")]').click()
        elif leix=='【多选题':
            if '' in cc:
                kk=cc.split('')
                for i, j in enumerate(kk):
                    driver.find_element_by_xpath('//*[contains(text(),"' + j + '")]').click()
            elif '#' in cc:
                kk=cc.split('#')
                for i, j in enumerate(kk):
                    driver.find_element_by_xpath('//*[contains(text(),"' + j + '")]').click()
            elif '===' in cc:
                kk=cc.split('===')
                for i, j in enumerate(kk):
                    driver.find_element_by_xpath('//*[contains(text(),"' + j + '")]').click()
           
            elif 'A' in cc:

                kk=['A','C']
                i.find_element_by_xpath('//*[contains(@value,"A")]').click()
                i.find_element_by_xpath('//*[contains(@value,"C")]').click()
            else :

                kk=['A','C']
                i.find_element_by_xpath('//*[contains(@value,"A")]').click()
                i.find_element_by_xpath('//*[contains(@value,"C")]').click()




        else:
            print('nn')
        time.sleep(5)
        print('下一题')
    nei='提交'
    nei2='确定'
    driver.find_element_by_xpath('//*[contains(text(),"' + nei + '")]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="confirmSubWin"]/div/div/a[1]').click()
    print('next')
    time.sleep(6)


def analyse(m):
    if '答' in m:

        content=m.split('答案:')[1]
        content=content.split('如')[0]

        print(content)
        return content
    else:
        ctrlC1()
        m = getText()

        content=m.split('答案：')[1]

        print(content)
        return content

           
    
    
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
    pyautogui.moveTo(x=659, y=811,duration=1, tween=pyautogui.linear)
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

main()


'''win = win32gui.FindWindow('WeChatMainWndForPC','微信')
tid = win32gui.FindWindowEx(win,None,'Edit',None)
win32gui.SendMessage(tid, win32con.WM_SETTEXT, None, '你好hello word!')
win32gui.PostMessage(tid,win32con.WM_KEYDOWN,win32con.VK_RETURN,0)
print("%x" % tid)
win32api.SetCursorPos([727, 1059])
        # 模拟鼠标左键按下。
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
time.sleep(1)
        # 模拟鼠标左键放开。
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)'''

