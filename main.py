import random
import threading
import time
import datetime

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from excelParse import listArr
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException, ElementNotSelectableException, ElementNotVisibleException, \
    ImeActivationFailedException, InsecureCertificateException, InvalidArgumentException, InvalidCookieDomainException, \
    InvalidCoordinatesException, InvalidElementStateException, InvalidSelectorException, InvalidSessionIdException, \
    InvalidSwitchToTargetException, MoveTargetOutOfBoundsException, NoAlertPresentException, NoSuchAttributeException, \
    NoSuchCookieException, NoSuchFrameException, NoSuchWindowException, StaleElementReferenceException, \
    TimeoutException, UnableToSetCookieException, UnexpectedAlertPresentException, UnexpectedTagNameException

client = MongoClient('mongodb://localhost:27017/Crawler')
mydatabase = client['Crawler']
namedir = mydatabase['Crawler']
todayDate = mydatabase['todayDate']
today_date = datetime.date.today()
new_today_date = today_date.strftime("%d/%m/%Y")
todayDate.insert_one({"time": new_today_date, "report": []})
searchDate = todayDate.find_one({"time": "02/00/2023"})
if searchDate != None:
    if new_today_date == searchDate['time']:
        print("что то есть")
    else:
        print("нет")
else:
    todayDate.insert_one({"time": new_today_date, "report": []})

print(namedir.find_one())


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

        ref_url = "?new_format_start&utm_source=google&utm_medium=cpc&utm_campaign_id={campaignid}&utm_term={keyword}&utm_adgroup_id={adgroupid}&target_id={targetid}&loc_interest_ms={loc_interest_ms}&loc_physical_ms={loc_physical_ms}&matchtype={matchtype}&network={network}&device={device}&device_model={device_model}&if_mobile={ifmobile:[mobile]}&not_mobile={ifnotmobile:[computer_tablet]}&if_search={ifsearch:[google_search_network]}&if_display={ifcontent:[google_display_network]}&ad_id={creative}&placement={placement}&target={target}&ad_position={adposition}&source_id={sourceid}&ad_type={adtype}&new_format_end"

        driver.implicitly_wait(10)
        driver.get(data['url'] + ref_url)
        all_forms = driver.find_elements(By.TAG_NAME, 'form')

        driver.implicitly_wait(10)

        buttons = driver.find_elements(By.XPATH, "//button[(@data-bs-toggle='modal')]")
        popupForm = None
        time.sleep(5)
        popupForm1 = driver.find_elements(by=By.ID, value='popupModal')
        popupForm2 = driver.find_elements(by=By.ID, value='Modal')
        popupForm3 = driver.find_elements(by=By.ID, value='popup')
        if len(popupForm1) > 0:
            popupForm = popupForm1
            print('popupForm1 - ТУТ что то есть ')
        if len(popupForm2) > 0:
            popupForm = popupForm2
            print('popupForm2 - ТУТ что то есть ')
        if len(popupForm3) > 0:
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
                    print(data['url'])
                    if popupForm[0].get_attribute('style') == 'display: block;':
                        n = random.randint(100000000, 999999999)

                        checkElement = False
                        elementPhone = driver.find_element(By.XPATH,
                                                           "//form[@data-gtag-submit='popup']//input[@name='phone']")
                        elementName = driver.find_element(By.XPATH,
                                                          "//form[@data-gtag-submit='popup']//input[@name='name']")
                        inputs = driver.find_element(By.XPATH,
                                                     "//form[@data-gtag-submit='popup']//input[@name='email']")
                        btn = driver.find_element(By.XPATH, "//form[@data-gtag-submit='popup']//button[@type='submit']")
                        print(popupForm[0].get_attribute('id'))
                        poper = popupForm[0].get_attribute('id')
                        elementPhone.send_keys(n)
                        elementName.send_keys('crawler_checker')
                        inputs.send_keys('crawler@tester.com')
                        time.sleep(3)
                        btn.click()

                        print("//form[@id=" + poper + "//button[@data-bs-dismiss='modal']")
                        closebtn = driver.find_element(By.XPATH,
                                                       "//div[contains (@id," + poper + ")]//button[@data-bs-dismiss='modal']")
                        print(closebtn.location['x'])
                        actions = ActionChains(driver)
                        actions.send_keys(Keys.ESCAPE)
                        actions.perform()
                        time.sleep(3)
                        okbtn = driver.find_element(By.XPATH, "//button[text()='OK']")

                        time.sleep(1)
                        okbtn.click()

                        time.sleep(5)

        input_elements = driver.execute_script("return document.querySelectorAll('input');")
        n = random.randint(100000000, 999999999)

        for input_element in input_elements:
            input_type = input_element.get_attribute('type')
            input_name = input_element.get_attribute('name')
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", input_element)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of(input_element))

            if input_type == 'text' and input_name == 'name':
                input_element.send_keys('crawler_checker')
            elif input_type == 'email':
                input_element.send_keys('crawler@tester.com')

            elif input_type == 'tel':
                input_element.send_keys(n)
            elif input_name == 'datepicker' and input_type == 'text':
                date_input = driver.find_element(By.NAME, "datepicker")
                driver.execute_script("arguments[0].value = arguments[1];", date_input, new_today_date)
                select_element = driver.find_element(By.XPATH, "//select[@name='interesting_projects']")
                if select_element:
                    select = Select(select_element)
                    select.select_by_index(1)

            form = input_element.find_element(By.XPATH, "./ancestor::form")
            submit_button = form.find_element(By.XPATH, ".//button[@type='submit']")
            submit_button.click()
            time.sleep(3)
            okbtn = driver.find_element(By.XPATH, "//button[text()='OK']")
            time.sleep(1)
            okbtn.click()
        time.sleep(5)
        for datat in buttons:
            driver.implicitly_wait(10)
            driver.execute_script("arguments[0].scrollIntoView(true)", datat)


num_threads = 2  # You can change the number of threads as needed

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

