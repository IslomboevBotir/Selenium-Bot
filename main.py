# import asyncio
# import datetime
# import gzip
# import hashlib
# import json
# import os.path
# from selenium.webdriver.support.ui import WebDriverWait
# import random
# import time
# from excelParse import listArr
# import openpyxl
# import pandas as pd
# import threading  # Import the threading module
# from selenium.webdriver.support import expected_conditions as EC
# from urlAdd import addurl
# import requests
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException ,ElementClickInterceptedException, ElementNotInteractableException, ElementNotSelectableException, ElementNotVisibleException, ImeActivationFailedException, InsecureCertificateException, InvalidArgumentException, InvalidCookieDomainException, InvalidCoordinatesException, InvalidElementStateException, InvalidSelectorException, InvalidSessionIdException, InvalidSwitchToTargetException, MoveTargetOutOfBoundsException, NoAlertPresentException, NoSuchAttributeException, NoSuchCookieException, NoSuchFrameException, NoSuchWindowException, StaleElementReferenceException, TimeoutException, UnableToSetCookieException, UnexpectedAlertPresentException, UnexpectedTagNameException
# import subprocess

# from lxml import etree



# # options.add_argument('--dns-prefetch-disable')


# # chrome_options.add_argument('--headless=new')

# # print(data)


# def screenshot_thread(mydata):
#         chrome_options = Options()
#         service = webdriver.ChromeService()
#         chrome_options.add_argument('--log-level=CRITICAL')
#         # options.add_argument(f'--log-path=selenium.log')
#         # options.add_argument('--proxy-server=http://localhost:8080')
#         chrome_options.add_argument('--disable-extensions')
#         chrome_options.add_argument('--disable-gpu')
#         # options.add_argument('--disable-application-cache')
#         # options.add_argument('--disable-session-storage')
#         # options.add_argument('--disable-web-security')
#         # options.add_argument('--disable-breakpad')
#         # options.add_argument('--disable-sync')
#         # options.add_argument('--no-proxy-server')
#         chrome_options.add_argument('--enable-automation')
#         chrome_options.add_argument('--ignore-certificate-errors')
#         chrome_options.add_argument('--ignore-ssl-errors')
#         chrome_options.add_argument("--enable-logging")
#         chrome_options.add_argument('--no-sandbox')
#         chrome_options.add_argument('--disable-dev-shm-usage')
    
        
        
#         # print(g['name'])
#         # print(g['url'])
#         # print(data.index(g))
        
#         # myurl = addurl(g['url'])
#         # print('Моя ссылка '+myurl)
#         # driver.get(g['url'])
#         # driver.get('https://sales-inquiries.ae/axcapital/address-villas-hillcrest/')
#         # element = driver.find_element(By.TAG_NAME, 'form')
#         # print(element)
#         # driver.get("https://google.com")
        
#         disablemyfun = True
        
#         driver = webdriver.Chrome()
#         # for index,  data in enumerate(mydata):
#             #  print(data['url'], "index ", index)
#             # driver.implicitly_wait(10) 
            
#             # wait = WebDriverWait(driver, timeout=60)
#             # driver.get(data['url'])
#             # try:
#             #     print(data['url'], "До")
                 
#             #     wait.until(EC.element_to_be_clickable(
#             #             driver.find_element(By.XPATH, '//*[@id="room-label-1"]/div/span[1]')))
#             #     time.sleep(2)
#             #     # driver.get('https://sales-inquiries.ae/axcapital/seslia-tower/')
#             #     all_forms = driver.find_elements(By.TAG_NAME, 'form')
#             #     # all_forms = driver.find_elements(By.ID, 'user-login-form')
                
#             #     # print(all_forms)
#             #     driver.implicitly_wait(10) 
                
#             #     buttons = driver.find_elements(By.XPATH, "//button[(@data-bs-toggle='modal')]")
#             #     popupForm = driver.find_element(by=By.ID, value='popupModal')
#             #     print(popupForm)
                
#             #     if popupForm: 
#             #         # print(popupForm.get_attribute('outerHTML'))
#             #         mytime = 1
#             #         timing = time.time()
#             #         checkElement = True
#             #         while checkElement:
#             #             if time.time() - timing > mytime:
#             #                 timing = time.time()
#             #                 print( mytime, "seconds")
#             #                 if popupForm.get_attribute('style') == 'display: block;':
#             #                     print("Пришел")
#             #                     checkElement = False           
#             #     # for form in all_forms
            
#             #     for data in buttons:
#             #         # print(data.get_attribute('data-text-title'))
#             #         # driver.execute_script("arguments[0].setAttribute('id',arguments[1])",data, "32423432")
#             #         # print(data.get_attribute('outerHTML'))
#             #         # print(data.get_attribute('outerHTML'))
                    
                
#             #         print(data['url'], "После")
#             #         # elemntid = data.get_attribute('innerHTML')
#             #         # data.execute_script('id=234234234234', all_forms)
#             #         # element = driver.find_element(By.TAG_NAME, 'form')
#             #         # myhtml = data.get_attribute('outerHTML')
#             #         # soup = BeautifulSoup(myhtml)
#             #         # for link in soup.find_all('input'):
#             #             # print(link['name'])
#             #             # link.exe
#             #             # link.send_keys('23r32r')
                        

            
                
#             #         # elementName = elemntid.find_element(By.NAME, "email")
#             #         # elementEmail = driver.find_element(By.XPATH, "//form[@data-gtag-submit='get_consultation']//input[@name='email']")
#             #         # elementPhone = driver.find_element(By.XPATH, "//form[@data-gtag-submit='get_consultation']//input[@name='phone']")
        
#             #     # time.sleep(99999)   
#             #     # driver.implicitly_wait(10) 
#             #     # driver.execute_script("arguments[0].scrollIntoView(true)", elementName)

#             #     # driver.implicitly_wait(10) 
#             #     # print("Element is visible? " + str(element.is_displayed()))
            

#             #     # print(elementName.get_attribute('outerHTML'))
#             #     # print(elementEmail.get_attribute('outerHTML'))
#             #     # print(elementPhone.get_attribute('outerHTML'))
#             #     # element.send_keys('fdfdsfsfdsf')
           
#             # except  (NoSuchElementException ,ElementClickInterceptedException, ElementNotInteractableException, ElementNotSelectableException, ElementNotVisibleException, ImeActivationFailedException, InsecureCertificateException, InvalidArgumentException, InvalidCookieDomainException, InvalidCoordinatesException, InvalidElementStateException, InvalidSelectorException, InvalidSessionIdException, InvalidSwitchToTargetException, MoveTargetOutOfBoundsException, NoAlertPresentException, NoSuchAttributeException, NoSuchCookieException, NoSuchFrameException, NoSuchWindowException, StaleElementReferenceException, TimeoutException, UnableToSetCookieException, UnexpectedAlertPresentException, UnexpectedTagNameException) as err:
#             #     print("")
            
#             # finally:
#             #     print
            
#             # time.sleep(50)
#             # print(element.get_attribute('outerHTML'))
#             # time.sleep(10)
            
       
       

# num_threads = 5 # You can change the number of threads as needed

# threads = []
# currentpage=0



# for i in range(num_threads):
#     data = listArr()
#     length = len(data) // num_threads
#     mydata = data[currentpage * length : (currentpage + 1) * length]
#     for index, data in enumerate(mydata):
#         print(data['url'], index)
#     # thread = threading.Thread(target=screenshot_thread, args=([mydata]))
#     # currentpage+=1
    
#     # threads.append(thread)
#     # thread.start()

# for thread in threads:
#     thread.join()



from selenium.webdriver.support.ui import WebDriverWait
import threading
import time
from excelParse import listArr

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException, ElementNotSelectableException, ElementNotVisibleException, \
    ImeActivationFailedException, InsecureCertificateException, InvalidArgumentException, InvalidCookieDomainException, \
    InvalidCoordinatesException, InvalidElementStateException, InvalidSelectorException, InvalidSessionIdException, \
    InvalidSwitchToTargetException, MoveTargetOutOfBoundsException, NoAlertPresentException, NoSuchAttributeException, \
    NoSuchCookieException, NoSuchFrameException, NoSuchWindowException, StaleElementReferenceException, \
    TimeoutException, UnableToSetCookieException, UnexpectedAlertPresentException, UnexpectedTagNameException


def screenshot_thread(mydata):
    chrome_options = Options()
    chrome_options.add_argument('--log-level=CRITICAL')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--enable-automation')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument("--enable-logging")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome()

    for index, data in enumerate(mydata):
        
        
           
            # print(data['url'], "index ", index)
            driver.implicitly_wait(10)
            driver.get(data['url'])
            # driver.get('https://sales-inquiries.ae/axcapital/seslia-tower/')
            all_forms = driver.find_elements(By.TAG_NAME, 'form')
            # all_forms = driver.find_elements(By.ID, 'user-login-form')

            # print(all_forms)
            driver.implicitly_wait(10)

            buttons = driver.find_elements(By.XPATH, "//button[(@data-bs-toggle='modal')]")
            popupForm = None
            time.sleep(5)
            popupForm1 = driver.find_elements(by=By.ID, value='popupModal')
            popupForm2 = driver.find_elements(by=By.ID, value='Modal')
            popupForm3 = driver.find_elements(by=By.ID, value='popup')
            if len(popupForm1)>0:
                popupForm = popupForm1
                print('popupForm1 - ТУТ что то есть ')
            if len(popupForm2)>0:
                popupForm = popupForm2
                print('popupForm2 - ТУТ что то есть ')
            if len(popupForm3)>0:
                popupForm = popupForm3
                print('popupForm3 - ТУТ что то есть ')
            try:

                popupForm
               
            except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException,
                ElementNotSelectableException, ElementNotVisibleException, ImeActivationFailedException,
                InsecureCertificateException, InvalidArgumentException, InvalidCookieDomainException,
                InvalidCoordinatesException, InvalidElementStateException, InvalidSelectorException,
                InvalidSessionIdException, InvalidSwitchToTargetException, MoveTargetOutOfBoundsException,
                NoAlertPresentException, NoSuchAttributeException, NoSuchCookieException, NoSuchFrameException,
                NoSuchWindowException, StaleElementReferenceException, TimeoutException, UnableToSetCookieException,
                UnexpectedAlertPresentException, UnexpectedTagNameException) as err:
                pass
            if popupForm:
                mytime = 1
                timing = time.time()
                checkElement = True
                while checkElement:
                    if time.time() - timing > mytime:
                        timing = time.time()
                        # print(mytime, "seconds")
                        print(data['url'])
                        # print(popupForm[0].get_attribute('outerHTML'))
                        if popupForm[0].get_attribute('style') == 'display: block;':
                            # print("Пришел")
                            checkElement = False
            # for form in all_forms
            # print(buttons)
            for datats in buttons:

                # driver.execute_script("arguments[0].setAttribute('id',arguments[0])",datats, "32423432")
         

                print(datats)
                # elemntid = datats.get_attribute('innerHTML')
                # driver.execute_script('id=234234234234', all_forms)
                # element = driver.find_element(By.TAG_NAME, 'form')
                # myhtml = datats.get_attribute('outerHTML')
                # soup = BeautifulSoup(myhtml)
                # for link in soup.find_all('input'):
                #     link.exe
                #     link.send_keys('23r32r')

                # elementName = elemntid.find_element(By.NAME, "email")
                # elementEmail = driver.find_element(By.XPATH, "//form[@data-gtag-submit='get_consultation']//input[@name='email']")
                # elementPhone = driver.find_element(By.XPATH, "//form[@data-gtag-submit='get_consultation']//input[@name='phone']")

            # time.sleep(99999)
                driver.implicitly_wait(10)
                driver.execute_script("arguments[0].scrollIntoView(true)", datats)
                # time.sleep(5)
            # driver.implicitly_wait(10)
            # print("Element is visible? " + str(element.is_displayed()))

          


        # time.sleep(1000)
        # print(element.get_attribute('outerHTML'))
        # time.sleep(10)
    driver.quit()

num_threads = 5  # You can change the number of threads as needed

threads = []
cursor = 0

for i in range(num_threads):
    data = listArr()
    length = len(data) // (num_threads - 1)
    mydata = data[cursor * length: (cursor + 1) * length]
    thread = threading.Thread(target=screenshot_thread, args=([mydata]))
    cursor += 1

    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


