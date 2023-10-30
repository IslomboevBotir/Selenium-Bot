from excelParse import listArr
# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver as wiredriver
from urlAdd import addurl
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, ElementNotSelectableException, ElementNotVisibleException, ImeActivationFailedException, InsecureCertificateException, InvalidArgumentException, InvalidCookieDomainException, InvalidCoordinatesException, InvalidElementStateException, InvalidSelectorException, InvalidSessionIdException, InvalidSwitchToTargetException, MoveTargetOutOfBoundsException, NoAlertPresentException, NoSuchAttributeException, NoSuchCookieException, NoSuchFrameException, NoSuchWindowException, StaleElementReferenceException, TimeoutException, UnableToSetCookieException, UnexpectedAlertPresentException, UnexpectedTagNameException
import time
import json
import requests
data = listArr()
total_forms = 0
# list_var = json.loads(data)
chrome_options = Options()
service = wiredriver.ChromeService()
chrome_options.add_argument('--log-level=CRITICAL')
# options.add_argument(f'--log-path=selenium.log')
# options.add_argument('--proxy-server=http://localhost:8080')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-gpu')
# options.add_argument('--disable-application-cache')
# options.add_argument('--disable-session-storage')
# options.add_argument('--disable-web-security')
# options.add_argument('--disable-breakpad')
# options.add_argument('--disable-sync')
# options.add_argument('--no-proxy-server')
chrome_options.add_argument('--enable-automation')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument("--enable-logging")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless=new')
# driver = wiredriver.Chrome(options=chrome_options, service=service)
driver = wiredriver.Chrome()
# print(len(data))
driver.get('https://sales-inquiries.ae/axcapital/gems-estates/')
element = driver.find_element(By.TAG_NAME, 'form')
print(element)
for g in data:
    print(g['name'])
    print(g['url'])
    # print(data.index(g))
    myurl = addurl(g['url'])
    # print('Моя ссылка '+myurl)
    # driver.get(g['url'])
    # driver.get('https://sales-inquiries.ae/axcapital/address-villas-hillcrest/')
    # element = driver.find_element(By.TAG_NAME, 'form')
    # print(element)
    # driver.get("https://google.com")
    driver.implicitly_wait(10) 
    try:
        driver.implicitly_wait(10) 
        time.sleep(10)
        # element = driver.find_element(By.TAG_NAME, 'form')
        # print(element)
        # elementName = driver.find_element(By.XPATH, "//form[@data-gtag-submit='get_consultation']//input[@name='name']")
        # elementEmail = driver.find_element(By.XPATH, "//form[@data-gtag-submit='get_consultation']//input[@name='email']")
        # elementPhone = driver.find_element(By.XPATH, "//form[@data-gtag-submit='get_consultation']//input[@name='phone']")
        # driver.implicitly_wait(10) 
        # driver.execute_script("arguments[0].scrollIntoView(true)", elementName)

        # driver.implicitly_wait(10) 
        # print("Element is visible? " + str(element.is_displayed()))
      

        # print(elementName.get_attribute('outerHTML'))
        # print(elementEmail.get_attribute('outerHTML'))
        # print(elementPhone.get_attribute('outerHTML'))
        # element.send_keys('fdfdsfsfdsf')

    except InvalidArgumentException as err:
        print("fdfdsfdsfdsf")
    finally:
        print("////////////////////////////////////////////////////////////")
    # print(element.get_attribute('outerHTML'))
    # time.sleep(10)
    # driver.quit()
