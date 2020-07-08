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

    a=[{'domain': 'onlineh5.zhihuishu.com', 'httpOnly': False, 'name': 'SERVERID', 'path': '/', 'secure': False, 'value': '58a6d0bed134adfd5bca4c165678e873|1591008650|1591008633'}, {'domain': '.zhihuishu.com', 'httpOnly': False, 'name': 'Hm_lpvt_0a1b7151d8c580761c3aef32a3d501c6', 'path': '/', 'secure': False, 'value': '1591008650'}, {'domain': '.zhihuishu.com', 'expiry': 1591267849, 'httpOnly': False, 'name': 'exitRecod_dbN4YlgO', 'path': '/', 'secure': False, 'value': '2'}, {'domain': 'onlineh5.zhihuishu.com', 'expiry': 1593687033.392755, 'httpOnly': True, 'name': 'acw_tc', 'path': '/', 'secure': False, 'value': '707c9f9915910086330414583e372e44149a822be94f41876aaf77a15ed070'}, {'domain': '.zhihuishu.com', 'httpOnly': False, 'name': 'CASLOGC', 'path': '/', 'secure': False, 'value': '%7B%22realName%22%3A%22%E6%B1%9F%E6%80%9D%E6%88%90%22%2C%22myuniRole%22%3A0%2C%22myinstRole%22%3A0%2C%22userId%22%3A215125835%2C%22headPic%22%3A%22https%3A%2F%2Fimage.zhihuishu.com%2Fzhs%2Fablecommons%2Fdemo%2F201804%2Fa3b5f5570a2740749d3c372848a18d6f_s3.jpg%22%2C%22uuid%22%3A%22dbN4YlgO%22%2C%22mycuRole%22%3A0%2C%22username%22%3A%22a839d56179e64733bd0594494414c65f%22%7D'}, {'domain': 'onlineh5.zhihuishu.com', 'httpOnly': False, 'name': 'u_asec', 'path': '/', 'secure': False, 'value': '099%23KAFEF7EKE64EJETLEEEEEpEQz0yFD6fJSXJYZ6z3DX9IW60cSry4V6N1DuB5E7EFlllbrmQTEE7EERpClYFETJDovlvUE7TxEqgUEFyV0HUCBFt05cmoRJqtkfMV%2BwdZcw76LLlLciobftP2yl5GcZKYnH4OVwMWoZ7fBB8sIhj2q7VB6OT26mGrZTzezSKr0kj7JxcGkLFDBcQTEEMFluuta3toE7EIlllbazb29ilbE7EUlllPP9iSlCwllu8Gt37F6lllWsaStEgtlllO%2F3iS16allu8vt37INqMTEwdEvypC%2FqYWcR4f9BZsDi2S6sRqlleE6R7SrYCc%2Fq4BbyXZ9MZWDO7nbebRx%2FexcOMZ4BZcU65CbLoWTFZGDiAhE7EhlGwP%2F3iS'}, {'domain': 'onlineh5.zhihuishu.com', 'expiry': 1906368632, 'httpOnly': False, 'name': '_uab_collina', 'path': '/', 'secure': False, 'value': '159100863296153782542745'}, {'domain': '.zhihuishu.com', 'expiry': 1622544649, 'httpOnly': False, 'name': 'Hm_lvt_0a1b7151d8c580761c3aef32a3d501c6', 'path': '/', 'secure': False, 'value': '1591008650'}, {'domain': '.zhihuishu.com', 'httpOnly': False, 'name': 'CASTGC', 'path': '/', 'secure': False, 'value': 'TGT-782614-MfUAVdC5t3aLoeWrxCpgYHdQGl7nqxPYjVdKZeTNgYKAp0J4ff-passport.zhihuishu.com'}]
    driver=webdriver.Chrome()
    driver.get(url)
    
    
    driver.delete_all_cookies()
    for cookie in a:
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)
    time.sleep(2)


    driver.get(url)
    driver.maximize_window()
    driverwait = WebDriverWait(driver, 20)
    driverwait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="sharingClassed"]/div[2]/ul[3]/div/dl/dt/div[1]'))).click()
    driverwait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[6]/div/div[3]/span/button'))).click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[7]/div[2]/div[1]/i').click()
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
                print('点下一页')
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
            print('出现题')
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
