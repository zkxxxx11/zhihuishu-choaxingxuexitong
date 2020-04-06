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
def main():
    url='https://onlineh5.zhihuishu.com/onlineWeb.html#/studentIndex'

    a={'domain': '.zhihuishu.com', 'expiry': 1586008542, 'httpOnly': False, 'name': 'exitRecod_EmQpBQKK', 'path': '/', 'secure': False, 'value': '2'}, {'domain': '.zhihuishu.com', 'httpOnly': False, 'name': 'CASLOGC', 'path': '/', 'secure': False, 'value': '%7B%22myuniRole%22%3A0%2C%22username%22%3A%222e53790507c945f0a525ff7224bc8f1e%22%2C%22mycuRole%22%3A0%2C%22userId%22%3A800057807%2C%22myinstRole%22%3A0%2C%22realName%22%3A%22%E7%8E%8B%E7%A5%9E%E7%BF%94%22%2C%22uuid%22%3A%22EmQpBQKK%22%2C%22headPic%22%3A%22https%3A%2F%2Fimage.zhihuishu.com%2Fzhs%2Fablecommons%2Fdemo%2F201804%2F4aee171746a7437bad86d0699197df9f_s3.jpg%22%7D'}, {'domain': '.zhihuishu.com', 'httpOnly': False, 'name': 'Hm_lpvt_0a1b7151d8c580761c3aef32a3d501c6', 'path': '/', 'secure': False, 'value': '1585749342'}, {'domain': '.zhihuishu.com', 'httpOnly': False, 'name': 'CASTGC', 'path': '/', 'secure': False, 'value': 'TGT-1732760-YdeWqMb5pXe0w1kAEd7aaGzqeZjULP7FlqsvfgdclXCli2PpJy-passport.zhihuishu.com'}, {'domain': '.zhihuishu.com', 'expiry': 1617285341, 'httpOnly': False, 'name': 'Hm_lvt_0a1b7151d8c580761c3aef32a3d501c6', 'path': '/', 'secure': False, 'value': '1585749321'}
    driver=webdriver.Chrome()
    driver.get(url)
    time.sleep(50)
    #输入账号密码
    print(driver.get_cookies())
    '''driver.delete_all_cookies()
    for cookie in a:
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)'''
    time.sleep(2)


    driver.get(url)
    driver.maximize_window()
    driverwait = WebDriverWait(driver, 20)
    driverwait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="sharingClassed"]/div[2]/ul[2]/div/dl/dt/div[1]'))).click()
    driverwait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[6]/div/div[3]/span/button'))).click()
    driverwait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[7]/div[2]/div[1]/i'))).click()
    time.sleep(2)

    '''ActionChains(driver).move_by_offset(710,350)
    driver.find_element_by_xpath('//*[@id="vjs_container"]/div[10]/div[6]').click()
    driver.find_element_by_xpath('// *[ @ id = "vjs_container"] / div[10] / div[8]').click()
    driver.find_element_by_xpath('// *[ @ id = "vjs_container"] / div[10] / div[8] / div / div[1]').click()'''



    #ActionChains(driver).move_by_offset(1057, 696).click_and_hold().perform()
    #print(driver.get_window_position())
    while True:
        time.sleep(20)
        if driver.find_elements_by_xpath('//*[@id="app"]/div/div[7]/div/div[1]/div/h4')==[]:
            #.get_attribute('textContent')
            #driver.switch_to.frame('vjs_container')

            '''print(url)
            print("start")
            driver.execute_script("arguments[0].play()", video)
            driver.find_element_by_xpath('//*[@id="nextBtn"]').click()

            print("stop")
            driver.execute_script("arguments[0].pause()", video)
            time.sleep(10)'''
            #a = driver.find_element_by_xpath('//*[@id="vjs_container"]/div[10]/div[6]').is_displayed()
            #print('dis',a)
            #c = driver.find_element_by_xpath('//*[@id="vjs_container"]/div[5]/div[4]/div').get_attribute('innerHTML')
            #d = driver.find_element_by_xpath('//*[@id="vjs_container"]/div[5]/div[4]/div').get_attribute('textContent')
            time1= driver.find_element_by_xpath('//*[@id="vjs_container"]/div[5]/div[4]/div').get_attribute('innerText')
            time2= driver.find_element_by_xpath('//*[@id="vjs_container"]/div[5]/div[2]/div').get_attribute('innerText')
            time1=time1[-5:]
            time2=time2[-5:]
            #ActionChains(driver).move_by_offset(588, 1128).double_click().perform()



            if time1==time2:
                ele = driver.find_element_by_class_name('controlsBar')

                print(ele)
                driver.execute_script("arguments[0].setAttribute (arguments[1],arguments[2])", ele, 'style',
                                      'z-index: 2; overflow: inherit; display: block;')

                print(ele.get_attribute("style"))
                print(ele.get_attribute("class"))

                video = driver.find_element_by_id("vjs_container_html5_api")
                url = driver.execute_script("return arguments[0].currentSrc;", video)


                driver.find_element_by_xpath('//*[@id="nextBtn"]').click()
                time.sleep(3)

                driver.find_element_by_xpath('//*[@id="vjs_container"]/div[10]/div[6]').click()


                driver.find_element_by_xpath('// *[ @ id = "vjs_container"] / div[10] / div[8]').click()


                driver.find_element_by_xpath('//*[@id="vjs_container"]/div[10]/div[8]/div/div[1]').click()
                '''pyautogui.moveTo(x=86, y=975, duration=2, tween=pyautogui.linear)
                pyautogui.click()
                pyautogui.moveTo(x=1252, y=970, duration=2, tween=pyautogui.linear)
                pyautogui.moveTo(x=1251, y=820, duration=2, tween=pyautogui.linear)
                pyautogui.click()
                pyautogui.moveTo(x=1403, y=983, duration=2, tween=pyautogui.linear)
                pyautogui.click()'''
            print('ing....................',time1,time2)


#1403,983 voice
#1252,970   1251,820

#86,975 next
        else:
            video = driver.find_element_by_id("vjs_container_html5_api")
            url = driver.execute_script("return arguments[0].currentSrc;", video)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[7]/div/div[2]/div/div[1]/div/div/div[2]/ul/li[1]/span').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="app"]/div/div[7]/div/div[3]/span/div').click()
            print("start")
            driver.execute_script("arguments[0].play()", video)


    print('ddddddddddddddddddddddddddddddddddddddddddddd')



    time.sleep(100000000)




main()
