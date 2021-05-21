from selenium import webdriver
import time
import re
import pickle
import pandas as pd

file = open('pmx.pkl', 'rb')
data = pickle.load(file)
file.close()

header = False

def web_scrape():
    driver = webdriver.Firefox()

    driver.get('meraki.url')

    s_bandwith = []

    try:
        field = driver.find_element_by_xpath('//*[@id="email"]')
        field.clear()
        field.send_keys("username")
        field.submit()

        time.sleep(5)

        field = driver.find_element_by_xpath('//*[@id="password"]')
        field.clear()
        field.send_keys("password")
        field.submit()

        time.sleep(5)

    except:
        pass

    for entry in data:
        driver.get(entry[0][0])

        time.sleep(8)
        try:
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[1]/div[3]/div/div/section/section[2]/nav/div/a[5]').click()

            time.sleep(5)

            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[1]/div[3]/div/div/section/section[2]/section/div/ul/li[3]/div/button').click()

            time.sleep(10)

            bandwith = driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[1]/div[3]/div/div/section/section[2]/section/div/ul/li[3]/ul/li/div/pre')
            ex_bandwith = bandwith.get_attribute('innerHTML')
            cleanr = re.compile('&nbsp;')
            bandwith_clean = re.sub(cleanr, '', ex_bandwith)

            b = entry[0][2], bandwith_clean
            s_bandwith.append(b)

            time.sleep(2)
            print(s_bandwith)
            df = pd.DataFrame([b], columns=['Identifier', 'Bandwidth'])

            if header == True:
                mode = 'w'
            else:
                mode = 'a'
            df.to_csv('meraki_bandwidth.csv', mode=mode, header=header, index=False)

            time.sleep(2)
        except:
            continue


web_scrape()
