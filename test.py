import asyncio
import datetime
import gzip
import hashlib
import json
import os.path
import random
import time

import openpyxl
import pandas as pd
import requests

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, \
    InvalidElementStateException, WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


service_object = Service()
options = webdriver.ChromeOptions()
all_forms_list = []
ok_forms_list = []
ajax_responses: list[dict] = []
forms_key_list = []
wrong_url_list = []
total_forms = 0

group_chat_id = -1001644844138
options.add_argument('--log-level=CRITICAL')
options.add_argument(f'--log-path=selenium.log')
# options.add_argument('--proxy-server=http://localhost:8080')
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
# options.add_argument('--disable-application-cache')
# options.add_argument('--disable-session-storage')
# options.add_argument('--disable-web-security')
# options.add_argument('--disable-breakpad')
# options.add_argument('--disable-sync')
# options.add_argument('--no-proxy-server')
options.add_argument('--enable-automation')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--enable-logging")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless=new')


# options.add_argument('--dns-prefetch-disable')


def close_it(div):
    """
    Finds the close button in the given div and clicks it
    """
    try:
        close = div.find_element(by=By.CSS_SELECTOR,
                                 value='button[class="popup-close popup__close hover popup__close-md"]')
        time.sleep(0.4)
        try:
            close.click()
        except:
            actions.move_by_offset(close.location['x'], close.location['y'])
            actions.click()
            try:
                actions.perform()
            except:
                actions.move_by_offset(close.location_once_scrolled_into_view['x'] + 20,
                                       close.location_once_scrolled_into_view['y'] - 20)
                actions.click()
                try:
                    actions.perform()
                except:
                    pass
    except:
        pass


def close_button(driver_pointer: webdriver.Chrome, opened_form):
    """
    Finds the close button div and clicks it
    """
    try:
        opened_div = opened_form.find_element(by=By.XPATH,
                                              value="ancestor::*[position() = 4]")
        close_it(opened_div)
    except:
        pass


def close_all_buttons(driver_pointer: webdriver.Chrome):
    """
    Finds all active popups and closes them
    """
    try:
        opened_divs = driver_pointer.find_elements(by=By.CSS_SELECTOR,
                                                   value="div[class*='active']")
        for div in opened_divs:
            close_it(div)
    except NoSuchElementException:
        pass


def randomizer(driver_pointer):
    """
    Returns the random number for the unique phone input
    """
    current_url = driver_pointer.current_url
    timestamp = int(time.time() * 1000)  # Current timestamp in milliseconds
    random_seed = random.randint(1, 99999999999)  # Random number between 1 and 1000
    unique_string = f"{current_url}{random_seed}"
    md5_hash = hashlib.md5(unique_string.encode()).hexdigest()
    random_number = str(int(md5_hash, 16))[:15]
    random_number = f'{timestamp}{random_number}'[:15]
    return random_number


def check_metrics(driver_pointer, metric):
    """
    Checks if the all Google Metrics are present in the current site
    """
    try:
        driver_pointer.find_element(By.CSS_SELECTOR, f'script[src*="{metric}"]')
        return True
    except NoSuchElementException:
        return False


def check_ytm(driver_pointer, ytm):
    """
    Checks if the Yandex Metrics are present in the current site
    """
    try:
        no_scripts = driver_pointer.find_elements(by=By.TAG_NAME, value='noscript')
        for no_script in no_scripts:
            no_script_text = no_script.get_attribute('textContent')
            if ytm in no_script_text:
                return True
        return False
    except NoSuchElementException:
        return False


def find_datepicker(form_pointer):
    """
    Finds the date field in the given form
    """
    try:
        datepicker = form_pointer.find_element(By.CSS_SELECTOR, 'input[name="datepicker"]')
        return datepicker if datepicker.get_attribute('name') == 'datepicker' else None
    except NoSuchElementException:
        return None


def form_key_generator(form_str: WebElement):
    """
    Returns special key and css selector of the given form
    """
    form_itself = form_str
    try:
        form_str = form_str.get_attribute('outerHTML')
    except:
        return random.randint(0, 999999999), 'Form changed its position during CSS creation'
    split_form = form_str.split(">", 1)
    form_str = split_form[0] + ">"
    char_list = list(form_str[:10])
    random.shuffle(char_list)
    form_json_key = ''.join(char_list) + str(time.time() * 1000)
    form_json_key = form_json_key.replace(' ', '')
    return form_json_key, generate_css_selector(form_itself)


def set_current_date(datepicker):
    """
    Inputs date in the datepicker field of a form
    """
    if datepicker is not None:
        current_date = datetime.datetime.today().strftime('%d/%m/%Y')
        try:
            datepicker.send_keys(current_date)
        except ElementNotInteractableException:
            pass
        actions.move_by_offset(0, 0)
        actions.click()
        actions.perform()


def check_forms(driver_pointer, forms, url, button=None):
    """
    Checks all given forms and returns the left ones
    """
    exclude_forms = []
    for form in forms:
        driver_pointer.execute_script("arguments[0].scrollIntoView();", form)
        time.sleep(2)
        try:
            inputs = form.find_elements(By.CSS_SELECTOR,
                                        'input[name="name"], input[name="phone"], input[name="email"]')
        except:
            inputs = []
        counter = 0
        if len(inputs) != 3:
            exclude_forms.append(form)
            global total_forms
            total_forms -= 1 if total_forms > 0 else 0
            continue
        if not form.is_displayed():
            try:
                driver.execute_script("window.scrollBy(0, -1500)")
            except:
                pass
            time.sleep(1)
            try:
                driver_pointer.execute_script("arguments[0].scrollIntoView();", form)
            except:
                pass
            time.sleep(1)
            if not form.is_displayed():
                try:
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                except:
                    pass
                time.sleep(1)
                try:
                    driver.execute_script("window.scrollBy(0, -300)")
                except:
                    continue
                time.sleep(1)
        for input_el in inputs:
            try:
                try:
                    input_el.clear()
                except InvalidElementStateException:
                    continue
                if input_el.get_attribute('name') == 'name':
                    input_el.clear()
                    input_el.send_keys('crawler_checker')
                    counter += 1
                elif input_el.get_attribute('name') == 'email':
                    input_el.clear()
                    input_el.send_keys('crawler@tester.com')
                    counter += 1
                elif input_el.get_attribute('name') == 'phone' or input_el.get_attribute('title name') == 'phone':
                    input_el.clear()
                    input_phone = randomizer(driver)
                    input_el.send_keys(input_phone)
                    counter += 1
            except ElementNotInteractableException as err:
                pass
        datepicker_element = find_datepicker(form)
        set_current_date(datepicker_element)
        if button and counter != 3:
            try:
                button.click()
            except:
                pass
        if counter == 3:
            try:
                form_button = form.find_element(by=By.TAG_NAME, value='button')
            except NoSuchElementException:
                continue
            try:
                form_button.click()
            except:
                driver.execute_script(
                    f"window.scrollTo({form_button.location['x']}, {form_button.location['y'] - 100})")
                time.sleep(1)
                try:
                    form_button.click()
                except:
                    continue
            time.sleep(1)
            actions.move_by_offset(0, 0)
            actions.click()
            actions.perform()
            actions.move_by_offset(0, 0)
            actions.click()
            actions.perform()
            close_button(driver, form)
            form_key_json, form_str = form_key_generator(form)
            ok_forms_list.append(
                {"domain": url, "status": 'ok', "date": datetime.datetime.now().strftime('%Y-%d-%m %H:%M:%S'),
                 "input_phone": input_phone, "gtm": int(is_gtm and is_gta and is_ytm),
                 "template_number": template_number, "form_key": form_key_json})
            forms_key_list.append({form_key_json: form_str})
            exclude_forms.append(form)
    for excluded in exclude_forms:
        forms.remove(excluded)
    return forms


def click_buttons(ll: [WebElement], url):
    """
    Clicks all buttons related for form popup invoking and checks all left forms
    """
    if len(ll) == 0:
        return ll
    buttons = driver.find_elements(by=By.XPATH,
                                   value="//button[(@data-bs-toggle='modal' or @data-popup or contains(@class, 'popup')) and not(@type='submit') and not(@class='floorplans__details-btn main-btn')]")
    wrong_type_buttons = driver.find_elements(by=By.XPATH,
                                              value="//a[@data-bs-toggle='modal' and not(@type='submit') and not(@class='floorplans__details-btn main-btn')]")
    buttons = buttons + wrong_type_buttons
    for button in buttons:
        try:
            driver.execute_script(f"window.scrollTo({button.location['x']}, {button.location['y'] - 150})")
            time.sleep(1)
            try:
                button.click()
            except ElementClickInterceptedException:
                driver.execute_script("arguments[0].scrollIntoView();", button)
                time.sleep(1)
                try:
                    button.click()
                except ElementClickInterceptedException:
                    driver.execute_script("arguments[0].scrollIntoView();", button)
                    time.sleep(1)
                    driver.execute_script("window.scrollBy(0, -500);")
                    time.sleep(1)
                    try:
                        button.click()
                    except ElementClickInterceptedException:
                        driver.execute_script("window.scrollBy(0, 500)")
                        time.sleep(1)
                        try:
                            button.click()
                        except ElementClickInterceptedException:
                            driver.execute_script("arguments[0].scrollIntoView();", button)
                            time.sleep(1)
                            try:
                                button.click()
                            except ElementClickInterceptedException:
                                actions.move_by_offset(0, 0)
                                actions.click()
                                actions.perform()
                                driver.execute_script("window.scrollBy(0, -400);")
                                time.sleep(1)
                                try:
                                    button.click()
                                except ElementClickInterceptedException:
                                    driver.execute_script("window.scrollBy(0, -1500)")
                                    time.sleep(1)
                                    try:
                                        button.click()
                                    except ElementClickInterceptedException:
                                        driver.execute_script("arguments[0].scrollIntoView();", button)
                                        time.sleep(1)
                                        try:
                                            button.click()
                                        except ElementClickInterceptedException:
                                            continue
        except (ElementNotInteractableException or ElementClickInterceptedException) as error:
            driver.execute_script("arguments[0].scrollIntoView();", button)
            time.sleep(1)
            try:
                button.click()
            except:
                continue
        ll = check_forms(driver, ll, url, button)
        close_all_buttons(driver)
        actions.move_by_offset(0, 0)
        actions.click()
        actions.perform()
        actions.move_by_offset(0, 0)
        actions.click()
        actions.perform()
        time.sleep(1)
    if len(ll) == 0:
        return ll
    try:
        navbar = driver.find_element(by=By.CSS_SELECTOR, value='div[class="navbar-toggle"]')
        try:
            navbar.click()
        except:
            return ll
        time.sleep(0.5)
        ll = check_forms(driver, ll, url, navbar)
        try:
            navbar.click()
            time.sleep(0.5)
        except:
            return ll
    except NoSuchElementException:
        pass
    return ll


def add_http_prefix(url):
    """
    Returns the converted url if the url does not have proper url string
    """
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    return url


def load_and_invoke(driver_pointer, url):
    """
    Loads the given url in the browser. If the url is wrong then returns special int for error handling
    """
    driver_connected = False
    driver_start = time.time()
    while not driver_connected:
        try:
            driver_pointer.get(f'{url}{ref_url}')
            driver_connected = True
        except:
            if time.time() - driver_start > 40:
                return 10
    time.sleep(2)
    connection_start = time.time()
    connected = False
    while not connected:
        try:
            response_url = requests.get(url)
            connected = True
        except:
            if time.time() - connection_start > 40:
                return 8
    if response_url.status_code >= 404:
        return 10
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    return None


def forms_json_handler(forms_list: list[dict]):
    """
    Saves to JSON File all iterations and dates counts
    """
    with open(rf'JSON_{today_date}_{local_iter}.json', 'w', encoding='utf-8') as file:
        json.dump(forms_list, file, indent=4, ensure_ascii=False)


def iterations_handler():
    """
    JSON File for returning current date and global iterations counts
    """
    json_path = r'iterations.json'
    try:
        with open(json_path, 'r') as file:
            iterations_data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        iterations_data = {}
    if today_date in iterations_data:
        iterations_data[today_date] += 1
    else:
        iterations_data[today_date] = 1
    global_iterations_count = 0
    for count in iterations_data.values():
        global_iterations_count += count
    with open(json_path, 'w') as file:
        json.dump(iterations_data, file, indent=4)
    return iterations_data[today_date], global_iterations_count



def generate_css_selector(element: WebElement) -> str:
    """
    Receives WebElement and returns its CSS Selector for easier element founding
    """
    css_selector = ""
    while element is not None:
        tag_name = element.tag_name
        try:
            classes = element.get_attribute("class")
        except:
            classes = None
        try:
            id_attribute = element.get_attribute("id")
        except:
            id_attribute = None
        attributes = []

        if id_attribute:
            attributes.append(f"#{id_attribute}")
        if classes:
            classes = classes.split()
            class_selector = ".".join(classes)
            attributes.append(f".{class_selector}")

        css_selector = tag_name + "".join(attributes) + " " + css_selector
        element = element.find_element(By.XPATH, "..")
        if element.tag_name == "html" or element.tag_name == "body":
            break
    return css_selector.strip()


def wait_for_ajax():
    for request in driver.requests:
        if request.response and request.url == 'https://form.sales-inquiries.ae/logger/ajax_form_receiver/':
            compressed_data = request.response.body
            try:
                decompressed_data = gzip.decompress(compressed_data)
                decoded_text = decompressed_data.decode('utf-8')
                json_data = json.loads(decoded_text)
            except gzip.BadGzipFile:
                json_data = compressed_data
            ajax_responses.append(json_data)


if __name__ == '__main__':
    """
    Main function which invokes all methods, exports report and sends to the telegram group chat
    """
    response = requests.get("https://api.ipify.org?format=json")
    today_date = datetime.datetime.now().strftime('%Y-%d-%m')
    data = response.json()
    public_ipv4_address = data["ip"]
    print(public_ipv4_address)
    df = pd.read_excel('WEBSITES_DB.xlsx', sheet_name="Sheet1")
    urls_list = df[['project_name', 'domain_initial', 'domain 2', 'template_number']]
    driver = webdriver.Chrome(service=service_object, options=options)
    driver.maximize_window()
    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 60)
    ref_url = "?new_format_start&utm_source=google&utm_medium=cpc&utm_campaign_id={campaignid}&utm_term={keyword}&utm_adgroup_id={adgroupid}&target_id={targetid}&loc_interest_ms={loc_interest_ms}&loc_physical_ms={loc_physical_ms}&matchtype={matchtype}&network={network}&device={device}&device_model={device_model}&if_mobile={ifmobile:[mobile]}&not_mobile={ifnotmobile:[computer_tablet]}&if_search={ifsearch:[google_search_network]}&if_display={ifcontent:[google_display_network]}&ad_id={creative}&placement={placement}&target={target}&ad_position={adposition}&source_id={sourceid}&ad_type={adtype}&new_format_end"
    domain_counter = 0
    missed_forms = 0
    ajax_errors = 0
    bitrix_errors = 0
    gtm_errors = 0
    df_split = urls_list.sample(frac=0.35)
    for index, row in df_split.iterrows():
        domain_counter += 1
        url = row['domain_initial']
        if pd.isna(url):
            url = row['domain 2']
            if pd.isna(url):
                wrong_url_list.append(f'Project {row["project_name"]} does not have any url')
                continue
        print(url)
        try:
            template_number = round(int(row['template_number']))
        except ValueError:
            template_number = 0
        url = add_http_prefix(url)
        listing_type = load_and_invoke(driver, url)
        if listing_type == 10:
            wrong_url_list.append(f'Wrong url {url}')
            continue
        if listing_type == 8:
            wrong_url_list.append(f'Could not connect to {url}')
            continue
        is_gtm = check_metrics(driver, 'GTM-TMT24JCZ')
        is_gta = check_metrics(driver, 'G-42ZYSQVM8D')
        is_ytm = check_ytm(driver, '94366143')
        gtm_errors += 0 if int(is_ytm and is_gta and is_gtm) else 1
        all_forms = driver.find_elements(by=By.TAG_NAME, value='form')
        total_forms += len(all_forms)
        left_forms = check_forms(driver, all_forms, url, None)
        left_forms = check_forms(driver, left_forms, url, None)
        left_forms: list[WebElement] = click_buttons(left_forms, url)
        missed_forms += len(left_forms)
        
        for left in left_forms:
            form_key, form_html = form_key_generator(left)
            all_forms_list.append(
                {'domain': url, 'status': 'left', 'date': datetime.datetime.now().strftime('%Y-%d-%m %H:%M:%S'),
                 'gtm': int(is_gtm and is_gta and is_ytm), 'ajax_response': 'np.nan', 'bitrix_response': 'np.nan',
                 'template_number': template_number, "form_key": form_key})
            forms_key_list.append({form_key: form_html})



        time.sleep(8)
        
        
        # wait_for_ajax()
        iter_while = True
        timer_start = time.time()
        # while iter_while:
        #     ajax_responses = [obj.decode('utf-8') if isinstance(obj, bytes) else obj for obj in ajax_responses]
        #     ajax_objects = [obj for obj in ajax_responses if
        #                     'messages' in obj and 'input_phones' not in obj and 'email' not in obj and 'name' not in obj]
        #     if ajax_objects:
        #         ajax_responses.clear()
        #         time.sleep(1)
        #         wait_for_ajax()
        #     else:
        #         iter_while = False
        #     if time.time() - timer_start > 40:
        #         iter_while = False
        # for ok in ok_forms_list:
        #     try:
        #         matching_objects = [obj for obj in ajax_responses if
        #                             ok['input_phone'] in obj['tel'] and obj['email'] == 'crawler@tester.com' and obj[
        #                                 'name'] == 'crawler_checker']
        #     except TypeError:
        #         matching_objects = []
        #     ok['ajax_response'] = 1 if matching_objects else 0
        #     ajax_errors += 1 if not matching_objects else 0
        #     all_forms_list.append(ok)
        # time.sleep(5)
       
        # ajax_responses.clear()
        print(all_forms_list)
        ok_forms_list.clear()
    time.sleep(90)
    bitrix_load = False
    while not bitrix_load:
        try:
            bitrix_response = requests.get(
                'http://form.sales-inquiries.ae:8182/api/forms/today/?name=crawler_checker&page=1&per_page=99999').text
            bitrix_load = True
        except requests.exceptions.ConnectTimeout:
            pass
    bitrix_responses = json.loads(bitrix_response)['items']
    all_ok_list = [obj for obj in all_forms_list if obj['status'] == 'ok']
    for bit in all_ok_list:
        bitrix_matching_objects = [obj for obj in bitrix_responses if
                                   bit['input_phone'] in obj['phone'] and obj['email'] == 'crawler@tester.com' and
                                   obj['name'] == 'crawler_checker']
        bit['bitrix_response'] = 1 if bitrix_matching_objects else 0
        bitrix_errors += 1 if not bitrix_matching_objects else 0
    domain_column, status_column, date_column, ajax_column, bitrix_column, admin_column, tracker_column, gtm_column, template_column, path_column = [], [], [], [], [], [], [], [], [], []
    for key in all_forms_list:
        domain_column.append(key['domain'])
        status_column.append(key['status'])
        date_column.append(key['date'])
        gtm_column.append(key['gtm'])
        ajax_column.append(key['ajax_response'])
        bitrix_column.append(key['bitrix_response'])
        template_column.append(key['template_number'])
        path_column.append(key['form_key'])
    wrong_url_column = []
  
    driver.close()
    driver.quit()
    # asyncio.run(send_document_with_description())
