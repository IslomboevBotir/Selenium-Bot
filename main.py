import json
import random
import time
import datetime
import requests

from seleniumwire import webdriver
from selenium.webdriver.chrome.webdriver import Options
from pymongo import MongoClient
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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

from excelParse import listArr

client = MongoClient('mongodb://localhost:27017/Crawler')
mydatabase = client['Crawler']
namedir = mydatabase['Crawler']
todayDate = mydatabase['todayDate']
today_date = datetime.date.today()
new_today_date = today_date.strftime("%d/%m/%Y")
todayDate.insert_one({"time": new_today_date, "report": []})
search_date = todayDate.find_one({"time": "02/00/2023"})
if search_date is not None:
    if new_today_date == search_date['time']:
        print("что то есть")
    else:
        print("нет")
else:
    todayDate.insert_one({"time": new_today_date, "report": []})

print(namedir.find_one())


def screenshot_thread(mydata):
    path_of_account_data = '/home/hermes/Python_projects/ax-crawler/Chrome'
    options = Options()
    options.add_argument(f"user-data-dir={path_of_account_data}")
    driver = webdriver.Chrome(options=options)
    WebDriverWait(driver, 10)
    for index, data in enumerate(mydata):

        ref_url = ("?new_format_start&utm_source=google&utm_medium=cpc&utm_campaign_id={campaignid}&utm_term={"
                   "keyword}&utm_adgroup_id={adgroupid}&target_id={targetid}&loc_interest_ms={"
                   "loc_interest_ms}&loc_physical_ms={loc_physical_ms}&matchtype={matchtype}&network={"
                   "network}&device={device}&device_model={device_model}&if_mobile={ifmobile:[mobile]}&not_mobile={"
                   "ifnotmobile:[computer_tablet]}&if_search={ifsearch:[google_search_network]}&if_display={"
                   "ifcontent:[google_display_network]}&ad_id={creative}&placement={placement}&target={"
                   "target}&ad_position={adposition}&source_id={sourceid}&ad_type={adtype}&new_format_end")
        driver.implicitly_wait(10)
        driver.get(data['url'] + ref_url)
        driver.implicitly_wait(10)
        popup_form = None
        time.sleep(5)
        popup_form1 = driver.find_elements(by=By.ID, value='popupModal')
        popup_form2 = driver.find_elements(by=By.ID, value='Modal')
        popup_form3 = driver.find_elements(by=By.ID, value='popup')
        if len(popup_form1) > 0:
            popup_form = popup_form1
            print('popupForm1 - ТУТ что то есть ')
        if len(popup_form2) > 0:
            popup_form = popup_form2
            print('popupForm2 - ТУТ что то есть ')
        if len(popup_form3) > 0:
            popup_form = popup_form3
            print('popupForm3 - ТУТ что то есть ')
        try:

            popup_form

        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException,
                ElementNotSelectableException, ElementNotVisibleException, ImeActivationFailedException,
                InsecureCertificateException, InvalidArgumentException, InvalidCookieDomainException,
                InvalidCoordinatesException, InvalidElementStateException, InvalidSelectorException,
                InvalidSessionIdException, InvalidSwitchToTargetException, MoveTargetOutOfBoundsException,
                NoAlertPresentException, NoSuchAttributeException, NoSuchCookieException, NoSuchFrameException,
                NoSuchWindowException, StaleElementReferenceException, TimeoutException, UnableToSetCookieException,
                UnexpectedAlertPresentException, UnexpectedTagNameException) as err:
            pass
        if popup_form:
            my_time = 1
            timing = time.time()
            check_element = True
            while check_element:
                if time.time() - timing > my_time:
                    timing = time.time()
                    print(data['url'])
                    if popup_form[0].get_attribute('style') == 'display: block;':
                        n = random.randint(100000000, 999999999)

                        check_element = False
                        element_phone = driver.find_element(By.XPATH,
                                                            "//form[@data-gtag-submit='popup']//input[@name='phone']")
                        element_name = driver.find_element(By.XPATH,
                                                           "//form[@data-gtag-submit='popup']//input[@name='name']")
                        inputs = driver.find_element(By.XPATH,
                                                     "//form[@data-gtag-submit='popup']//input[@name='email']")
                        btn = driver.find_element(By.XPATH, "//form[@data-gtag-submit='popup']//button[@type='submit']")
                        print(popup_form[0].get_attribute('id'))
                        poper = popup_form[0].get_attribute('id')
                        element_phone.send_keys(n)
                        element_name.send_keys('crawler_checker')
                        inputs.send_keys('crawler@tester.com')
                        time.sleep(3)
                        btn.click()

                        print("//form[@id=" + poper + "//button[@data-bs-dismiss='modal']")
                        closebtn = driver.find_element(By.XPATH,
                                                       "//div[contains (@id," + poper + ")]//button["
                                                                                        "@data-bs-dismiss='modal']")
                        print(closebtn.location['x'])
                        actions = ActionChains(driver)
                        actions.send_keys(Keys.ESCAPE)
                        actions.perform()
                        time.sleep(3)
                        okbtn = driver.find_element(By.XPATH, "//button[text()='OK']")

                        time.sleep(1)
                        okbtn.click()

                        time.sleep(5)
                        ajax_check(driver, n)
                        api_check(n)
                        metrics_check(driver)

        try:
            submit_for(driver)
        finally:
            continue


def submit_for(driver: WebDriver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
    form_elements = driver.execute_script("return document.querySelectorAll('form');")
    for form in form_elements:
        wait = WebDriverWait(driver, 10)
        input_elements = form.find_elements(By.CSS_SELECTOR, 'input')
        n = random.randint(100000000, 999999999)
        for input_element in input_elements:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", input_element)
            time.sleep(3)
            wait.until(EC.presence_of_element_located((By.XPATH, "//button")))
            input_type = input_element.get_attribute('type')
            input_name = input_element.get_attribute('name')
            try:
                if input_type == 'text' and input_name == 'name':
                    time.sleep(2)
                    input_element.send_keys('crawler_checker')
                elif input_type == 'email':
                    input_element.send_keys('crawler@tester.com')
                elif input_type == 'tel':
                    input_element.send_keys(n)
                    time.sleep(2)
                elif input_name == 'datepicker' and input_type == 'text':
                    date_input = driver.find_element(By.NAME, "datepicker")
                    driver.execute_script("arguments[0].value = arguments[1];", date_input, new_today_date)
                    try:
                        select_element = driver.find_element(By.XPATH, "//select[@name='interesting_projects']")
                    except NoSuchElementException as e:
                        print(f"Ошибка: элемент не найден форма работает некорректно. {e}")
                    time.sleep(2)
                    if select_element:
                        select = Select(select_element)
                        select.select_by_index(2)
                        time.sleep(2)
            finally:
                continue
        submit_button = form.find_element(By.XPATH, ".//button[@type='submit']")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
        try:
            submit_button.click()
        except ElementClickInterceptedException as e:
            print(f"ElemenCliclInterecptedException: {e}")
        time.sleep(3)
        okbtn = driver.find_element(By.XPATH, "//button[text()='OK']")
        time.sleep(1)
        okbtn.click()
        ajax_check(driver, n)
        api_check(n)
        metrics_check(driver)


def ajax_check(driver: WebDriver, n: int):
    desired_url = "https://form.sales-inquiries.ae/api/forms/receiver/"
    request = list(filter(lambda x: x.url == desired_url, driver.requests))[-1]
    body = request.body
    status_code = request.response.status_code
    if status_code == 200:
        print('Всё окей форма передалась')
    else:
        print('Всё плохо есть ошибка')
    data_body = json.loads(body.decode('utf-8'))
    name = data_body.get('name')
    if name == 'crawler_checker':
        print('Всё окей имя передалось')
    else:
        print('Имя передалось некорректно либо вообще не передалось')
    email = data_body.get('email')
    if email == 'crawler@tester.com':
        print('Всё окей почта передалось')
    else:
        print('Почта передалась некорректно либо вообще не передалась')
    number = data_body.get('phone')
    if number == '+998' + str(n):
        print('Всё окей номер передался')
    else:
        print('Номер передался некорректно либо вообще не передался')


def api_check(n: int):
    url = 'https://form.sales-inquiries.ae/api/forms/today/'
    response = requests.get(url)
    data = response.json()

    if "items" in data and data["items"]:
        first_item = data["items"][0]
        name = first_item.get("name", "")
        if name == 'crawler_checker':
            print("Всё окей 2-ой тест на имя пройден")
        else:
            print("2-ой тест на имя не пройден")
        email = first_item.get("email", "")
        if email == 'crawler@tester.com':
            print("Всё окей 2-ой тест на email пройден ")
        else:
            print("2-ой тест по email не пройден")
        phone = first_item.get("phone", "")
        if phone == '+998' + str(n):
            print("Всё окей 2-ой тест на номер телефона пройден")
        else:
            print("2-ой тест на номер телефона не пройден")


def metrics_check(driver: WebDriver):
    page_source = driver.page_source
    gtm_code = 'GTM-TMT24JCZ'
    if gtm_code in page_source:
        print(f'Код Google Tag Manager {gtm_code} присутствует')
    else:
        print(f'Код Google Tag Manager {gtm_code} отсутствует')

    ga4_code = 'G-42ZYSQVM8D'
    if ga4_code in page_source:
        print(f'Код Google Analytics4 {ga4_code} присутствует')
    else:
        print(f'Код Google Analytics4 {ga4_code} отсутствует')

    yandex_code = '94366143'
    if yandex_code in page_source:
        print(f'Код Яндекс.Метрика {yandex_code} присутствует')
    else:
        print(f'Код Яндекс.Метрика {yandex_code} отсутствует')


def main():
    data = listArr()

    num_threads = 2
    length = len(data) // num_threads

    for i in range(num_threads):
        mydata = data[i * length: (i + 1) * length]
        screenshot_thread(mydata)


if __name__ == "__main__":
    main()
