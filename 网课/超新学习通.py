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
    url='https://mooc1-1.chaoxing.com/mycourse/studentstudy?chapterId=278850953&courseId=208157236&clazzid=17639393&enc=114f4f65333f18eb3925e18fad9376c1'
    a={'domain': '.chaoxing.com', 'httpOnly': False, 'name': 'thirdRegist', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.chaoxing.com', 'httpOnly': False, 'name': 'source', 'path': '/', 'secure': False, 'value': '""'}, {'domain': 'i.mooc.chaoxing.com', 'httpOnly': True, 'name': 'JSESSIONID', 'path': '/', 'secure': False, 'value': '1B65E16A3181970AE561920ECBE7AEA4'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551542, 'httpOnly': False, 'name': 'DSSTASH_LOG', 'path': '/', 'secure': False, 'value': 'C_38-UN_287-US_58662822-T_1585811785279'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551518, 'httpOnly': False, 'name': 'xxtenc', 'path': '/', 'secure': False, 'value': '504a6c4001dc1bf61141ef58b4a2391d'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551283, 'httpOnly': False, 'name': 'pid', 'path': '/', 'secure': False, 'value': '33406'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551406, 'httpOnly': False, 'name': 'UID', 'path': '/', 'secure': False, 'value': '58662822'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551491, 'httpOnly': False, 'name': 'vc3', 'path': '/', 'secure': False, 'value': 'fEOkczcD9ygYFNQHNI26UZtVJqLXPlkjY3NAlScPXJf5sgHsw8g7NkOlXeNjJ2RLa3GLJtFuwO09cw6ff2kkugkecdKuRHmTBxmRzfGzvl5PSf%2BrZvH6RucSl212pkX%2BsAyFoik5%2FDx2OnB5lyCF4zB9qo3RdtUK3euAmtABk4I%3Dfba386d27d5286fd77606f34b8225906'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.55143, 'httpOnly': True, 'name': 'vc', 'path': '/', 'secure': False, 'value': '7A36C7F955C52F47A7473338E7D80331'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551163, 'httpOnly': False, 'name': 'uname', 'path': '/', 'secure': False, 'value': '201705021121'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551254, 'httpOnly': False, 'name': 'fid', 'path': '/', 'secure': False, 'value': '14'}, {'domain': '.chaoxing.com', 'expiry': 1585898184.462983, 'httpOnly': False, 'name': 'tl', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551382, 'httpOnly': False, 'name': '_d', 'path': '/', 'secure': False, 'value': '1585811785277'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551457, 'httpOnly': True, 'name': 'vc2', 'path': '/', 'secure': False, 'value': '17EE7776945DF03CFFA011F918E818C6'}, {'domain': 'i.mooc.chaoxing.com', 'httpOnly': False, 'name': 'route', 'path': '/', 'secure': False, 'value': '0d3ee366e02d727b7b6bb10aae7f99cf'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551225, 'httpOnly': False, 'name': 'lv', 'path': '/', 'secure': False, 'value': '2'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551345, 'httpOnly': False, 'name': 'uf', 'path': '/', 'secure': False, 'value': 'b2d2c93beefa90dcdd008caef2b6662d7b6b069153ed664b7a4fb73fc63758498780e57f42b1b031ad5ec19e2d94ddcd9b0594e13f4b452f9f4fcd6f19e32a2ed08218e4e8aff7ed0d8a4c92b12beb4b38556611397fefe18974337d24b1c5d746da21146a924e23'}, {'domain': '.chaoxing.com', 'expiry': 1588403783.551314, 'httpOnly': False, 'name': '_uid', 'path': '/', 'secure': False, 'value': '58662822'}
    driver=webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="unameId"]').send_keys('15674912561')
    driver.find_element_by_xpath('//*[@id="passwordId"]').send_keys('wly561999')
    driver.maximize_window()

    a=driver.find_element_by_xpath('//*[@id="fid"]')
    print(a,a.is_displayed())
    driver.execute_script("arguments[0].setAttribute (arguments[1],arguments[2])", a, 'value',
                          '2632')

    driverwait = WebDriverWait(driver, 20)
    #输入验证码
    time.sleep(5)


    all = driver.find_elements_by_xpath('//div/h4/span[2]')
    all.remove(all[0])
    title = driver.find_elements_by_xpath('//div/h4/a')
    title.remove(title[0])
    print(len(title))
    '''for j,i in enumerate(title):

        if '章' in i.get_attribute('innerText'):
            title.remove(title[j])
            all.remove(all[j])'''
    for i in title:
        print(i.get_attribute('innerText'))
    print(len(title))


    for j,i in enumerate(all):

        #print(i.text)
        if i.text=='1':
            title[j].click()


            break
    chaozuo(driver)
    while True:

        if driver.find_elements_by_class_name('ans-videoquiz-submit') != []:
            print('出现弹出--------------')
            answer=driver.find_elements_by_xpath('//*[contains(@value,"true")]')
            for i in answer:
                i.click()
            driver.find_element_by_class_name('ans-videoquiz-submit').click()
            print('提交完毕；；；；')


        else:
            currenttime = driverwait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="video"]/div[5]/div[2]/span[2]'))).get_attribute(
                'innerText')

            alltime = driverwait.until(EC.presence_of_element_located(
                (By.XPATH, '//*[@id="video"]/div[5]/div[4]/span[2]'))).get_attribute(
                'innerText')
            print(currenttime, alltime)
            if currenttime == alltime:
                driver.switch_to.default_content()
                all = driver.find_elements_by_xpath('//div/h4/span[2]')
                all.remove(all[0])
                title = driver.find_elements_by_xpath('//div/h4/a')
                title.remove(title[0])
                for j, i in enumerate(title):

                    if '章' in i.get_attribute('innerText'):
                        title.remove(title[j])
                        all.remove(all[j])
                print(len(title))
                for j, i in enumerate(all):

                    # print(i.text)
                    if i.text == '1':
                        title[j].click()

                        print(j)
                        break
                chaozuo(driver)

def chaozuo(driver):
        time.sleep(2)
        if driver.find_elements_by_id('dct2')!=[]:
            driver.find_element_by_id('dct2').click()
        time.sleep(2)
        driver.switch_to.frame('iframe')
        driver.switch_to.frame(6)
       

       
        time.sleep(2)
        video = driver.find_element_by_id("video_html5_api")
        url = driver.execute_script("return arguments[0].currentSrc;", video)
        print('url:', url)
        time.sleep(4)
        print("start")
        driver.execute_script("arguments[0].play()", video)
        driver.find_element_by_xpath('//*[@id="video"]/div[5]/div[6]/button').click()
        driver.find_element_by_xpath('//*[@id="video"]/div[5]/div[1]/button').click()
        driver.find_element_by_xpath('//*[@id="video"]/div[5]/div[1]/button').click()
        driver.find_element_by_xpath('//*[@id="video"]/div[5]/div[1]/button').click()

main()

