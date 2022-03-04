from selenium.webdriver.remote.webdriver import WebDriver
from utils.enums.EnumBrowserCrawler import EnumBrowserCrawler
from utils.enums.EnumIdentifierTypeDriver import EnumIdentifierType
from selenium import webdriver
from selenium.webdriver.common import utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from msedge.selenium_tools import Edge, EdgeOptions

from selenium.webdriver.firefox.options import Options

import time
import os
import uuid
import requests
import tempfile

from utils.enums.EnumIdentifierTypeDriver import EnumIdentifierType
from utils.enums.EnumBrowserCrawler import EnumBrowserCrawler

import os

class BaseCrawler:
    def __init__(self, url_login, url_scrapper, browser):
        self.url_login = url_login
        self.url_scrapper = url_scrapper
        self.browser = browser
    
    def start_driver(self, *args, **kwargs):
        
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        headless                        = False if 'headless' not in kwargs else kwargs['headless']
        use_extension                   = False if 'use_extension' not in kwargs else kwargs['use_extension']
        implicit_wait                   = False if 'implicit_wait' not in kwargs else kwargs['implicit_wait']
        implicit_wait_time              = 10    if 'implicit_wait_time' not in kwargs else kwargs['implicit_wait_time']
        download_default_directory_temp = False if 'download_default_directory_temp' not in kwargs else kwargs['download_default_directory_temp']
        default_download_directory      = None  if 'default_download_directory' not in kwargs else kwargs['default_download_directory']
        download_pdf_without_chrome_ext = False if 'download_pdf_without_chrome_ext' not in kwargs else kwargs['download_pdf_without_chrome_ext']

        if self.browser==EnumBrowserCrawler.edge.value:
            edge_options = EdgeOptions()
            edge_options.use_chromium = True
            edge_options.add_argument('window-size=1920,1080')
            edge_options.add_argument('start-maximized')
            edge_options.add_argument('ignore-certificate-errors')
            
            if use_extension:
                edge_options.add_extension(BASE_DIR+'\\buster_captcha.crx')
                edge_options.add_extension(BASE_DIR+'\\anticaptcha-plugin_v0.52.crx')
            
            if 'user_data_dir' in kwargs and kwargs['user_data_dir'] is not None and\
            'profile' in kwargs and kwargs['profile'] is not None: 
                edge_options.add_argument('--user-data-dir={0}'.format(kwargs['user_data_dir']))
                edge_options.add_argument('--profile-directory={0}'.format(kwargs['profile']))

            if headless:
                edge_options.add_argument('headless')

            if 'proxy' in kwargs and kwargs['proxy'] is not None:
                edge_options.add_argument('proxy-server={0}'.format(kwargs['proxy']))

            if download_default_directory_temp:
                prefs = {
                    "profile.default_content_settings.popups": 0,
                    "download.default_directory":tempfile.gettempdir(),
                    "download.prompt_for_download":False,
                    "directory_upgrade": True,
                    'plugins.always_open_pdf_externally':True
                }
                edge_options.add_experimental_option("prefs", prefs)
            
            driver=Edge(
                options=edge_options
            )

        elif self.browser==EnumBrowserCrawler.internet_explorer.value:                                 #internet explorer
            caps = DesiredCapabilities.INTERNETEXPLORER
            caps['ignoreProtectedModeSettings'] = True
            caps['enableNativeEvents'] = False
            caps['enablePersistentHover'] = True
            caps['ignoreZoomLevel'] = True
            caps['ignoreZoomSetting'] = True
            caps['acceptInsecureCertificates'] = True
            caps['introduceInstabilityByIgnoringProtectedModeSettings'] = True
            caps['ensureCleanSession'] = True
            caps['javascriptEnabled'] = True
            caps['requireWindowFocus'] = False
            caps['enablePersistentHover'] = False
            driver = webdriver.Ie(
                capabilities=caps
            )

        elif self.browser==EnumBrowserCrawler.mozilla.value:
            options = Options()
            if headless:
                options.headless = True
            if 'proxy' in kwargs and kwargs['proxy'] is not None:
                options.add_argument('proxy-server={0}'.format(kwargs['proxy']))

            if download_default_directory_temp:
                options.add_argument("download.default_directory={0}".format(tempfile.gettempdir()))
            
            profile = webdriver.FirefoxProfile()
            profile.accept_untrusted_certs = True
            profile.set_preference('browser.download.folderList', 2) # custom location
            profile.set_preference('browser.download.manager.showWhenStarting', False)
            profile.set_preference('browser.download.dir', '/tmp')
            profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/html')
            profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf')
            driver = webdriver.Firefox(options=options, firefox_profile=profile)
        
        elif self.browser==EnumBrowserCrawler.chrome.value:
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            options.add_argument('ignore-certificate-errors')
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument('--log-level=3')
            options.add_argument("--output=/dev/null")

            if use_extension:
                options.add_extension(BASE_DIR+'\\anticaptcha-plugin_v0.52.crx')
                options.add_extension(BASE_DIR+'\\buster_captcha.crx')

            if 'user_data_dir' in kwargs and kwargs['user_data_dir'] is not None and\
            'profile' in kwargs and kwargs['profile'] is not None: 
                options.add_argument('--user-data-dir={0}'.format(kwargs['user_data_dir']))
                options.add_argument('--profile-directory={0}'.format(kwargs['profile']))
            
            if headless:
                options.add_argument('--headless')

            if 'proxy' in kwargs and kwargs['proxy'] is not None:
                options.add_argument('proxy-server={0}'.format(kwargs['proxy']))

            if download_default_directory_temp:
                prefs = {
                    "profile.default_content_settings.popups": 0,
                    "download.default_directory":tempfile.gettempdir(),
                    "download.prompt_for_download":False,
                    "directory_upgrade": True
                }
                if download_pdf_without_chrome_ext:
                    prefs["plugins.always_open_pdf_externally"] = True
                options.add_experimental_option("prefs", prefs)
            
            if default_download_directory is not None:
                prefs = {
                    "profile.default_content_settings.popups": 0,
                    "download.default_directory":default_download_directory,
                    "download.prompt_for_download":False,
                    "directory_upgrade": True,
                }
                if download_pdf_without_chrome_ext:
                    prefs["plugins.always_open_pdf_externally"] = True
                options.add_experimental_option("prefs", prefs)
            
            driver = webdriver.Chrome(chrome_options=options)
            
            driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })
            """
            })
            driver.execute_cdp_cmd("Network.enable", {})
            driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browser1"}})

            if implicit_wait:
                driver.implicitly_wait(implicit_wait_time)

        self.driver=driver

    def _find_element_by(self, identifier_type:EnumIdentifierType, identifier:str, **kwargs):
        
        """
            kwargs:
                - is_multiple (bool): Default is false. If is multiple elements.
                - element_to_look (selenium webdriver): Default is self._driver. Element in which to find element.
        """

        element_to_look = self.driver if 'element_to_look' not in kwargs else kwargs['element_to_look']
        is_multiple     = False if 'is_multiple' not in kwargs else bool(kwargs['is_multiple'])

        if not is_multiple:
            if identifier_type.value == EnumIdentifierType.id.value:
                return element_to_look.find_element_by_id(identifier)
            elif identifier_type.value == EnumIdentifierType.class_name.value:
                return element_to_look.find_element_by_class_name(identifier)
            elif identifier_type.value == EnumIdentifierType.css_selector.value:
                return element_to_look.find_element_by_css_selector(identifier)
            elif identifier_type.value == EnumIdentifierType.name.value:
                return element_to_look.find_element_by_name(identifier)
            elif identifier_type.value == EnumIdentifierType.tag_name.value:
                return element_to_look.find_element_by_tag_name(identifier)
            elif identifier_type.value == EnumIdentifierType.xpath.value:
                return element_to_look.find_element_by_xpath(identifier)
            elif identifier_type.value == EnumIdentifierType.partial_link_text:
                return element_to_look.find_element_by_partial_link_text(identifier)
            else:
                raise(Exception("Not passed possible identifier_type."))       
        else:
            if identifier_type.value == EnumIdentifierType.id.value:
                return element_to_look.find_elements_by_id(identifier)
            elif identifier_type.value == EnumIdentifierType.class_name.value:
                return element_to_look.find_elements_by_class_name(identifier)
            elif identifier_type.value == EnumIdentifierType.css_selector.value:
                return element_to_look.find_elements_by_css_selector(identifier)
            elif identifier_type.value == EnumIdentifierType.name.value:
                return element_to_look.find_elements_by_name(identifier)
            elif identifier_type.value == EnumIdentifierType.tag_name.value:
                return element_to_look.find_elements_by_tag_name(identifier)
            elif identifier_type.value == EnumIdentifierType.xpath.value:
                return element_to_look.find_elements_by_xpath(identifier)
            elif identifier_type.value == EnumIdentifierType.partial_link_text:
                return element_to_look.find_elements_by_partial_link_text(identifier)
            else:
                raise(Exception("Not passed possible identifier_type.")) 

    def _change_driver(self, driver):
        self.driver = driver

    def _change_page(self, *args, **kwargs):
        wait_time = True if 'wait_time' not in kwargs else kwargs['wait_time']

        if wait_time:
            time.sleep(4)
        
        main_page = self._driver.current_window_handle

        for handle in self._driver.window_handles:
            if handle != main_page:
                next_page = handle
                break

        self.driver.switch_to.window(next_page)
    
    def _check_more_than_one_tab(self):
        if len(self._driver.window_handles)>=2:
            return True
        return False
    
    def _change_tab(self, close_tabs = False):

        current_window_handel = self._driver.current_window_handle

        window_handles = self._driver.window_handles

        for handle in window_handles:
            if(handle != current_window_handel):
                if close_tabs:
                    self._driver.close()
                self._driver.switch_to.window(handle)
                break
    
    def _change_page_and_close(self, *args, **kwargs):
        wait_time = True if 'wait_time' not in kwargs else kwargs['wait_time']

        if wait_time:
            time.sleep(10)
        
        main_page = self._driver.current_window_handle
        
        next_page = None
        
        for handle in self._driver.window_handles:
            if handle != main_page:
                next_page = handle
                break
        
        if next_page!=None:
            self._driver.close()
            self._driver.switch_to.window(next_page)
    
    def _check_for_element(self, ec, id_type, id, MAX_WAIT_TIME=1, MAX_NUMBER_OF_RETRIES=2 ):
        try:
            self._get_element_retry(
                ec,
                id_type,
                id,
                MAX_WAIT_TIME=MAX_WAIT_TIME,
                MAX_NUMBER_OF_RETRIES=MAX_NUMBER_OF_RETRIES
            )
            return True
        except Exception as e:
            return False
        
    def remove_alerts(self, refuse=False):
        try:
            alert = Alert(self._driver)
            if refuse:
                alert.dismiss()
            else:
                alert.accept()
        except:
            pass
    
    def quit_driver(self):
        try:
            self._driver.quit()
        except:
            pass
    
    def close_driver(self):
        try:
            self._driver.close()
        except:
            pass
    
    def fill_input(self, identifier_type, identifier, text, *args, **kwargs):
        send_individual = False if 'send_individual' not in kwargs else kwargs['send_individual']
        
        input_value_correct = False
        input_element = self._get_element_retry(
            EC.visibility_of_element_located,
            identifier_type,
            identifier
        )

        if input_element.get_attribute("type")=="password":
            self._driver.execute_script("arguments[0].type = 'text';", input_element) 

        while not input_value_correct:
            input_element = self._get_element_retry(
                EC.visibility_of_element_located,
                identifier_type,
                identifier
            )
            if input_element.is_enabled() and\
            not self._driver.execute_script("return arguments[0].hasAttribute(\"readonly\")", input_element):
                input_element.clear()
                if send_individual:
                    for char in text:
                        time.sleep(0.3)
                        input_element.send_keys(char)                    
                else:
                    input_element.send_keys(text)
            
            if input_element.get_attribute("value") == text:
                input_value_correct = True
    
    def login(self, *args, **kwargs):

        button_go_login = None
        user_password = None
        user_email = None
        login_driver = None
        button_go_login = None

        if 'user_password' in kwargs:
            user_password = kwargs['user_password']
        if 'user_email' in kwargs:
            user_email = kwargs['user_email']
        if 'login_driver' in kwargs:
            login_driver = kwargs['login_driver']
            box_email_driver = login_driver['user_email']
            box_password_driver = login_driver['user_password']
            btn_submit_driver = login_driver['submit_button']
        if 'button_go_login' in kwargs:
            button_go_login = kwargs['button_go_login']
        
        if button_go_login:
            btn_go_login = self._find_element_by(
                identifier=button_go_login['identifier'],
                identifier_type=button_go_login['identifier_type']
            )
            btn_go_login.click()
            time.sleep(0.5)
        
        if user_email and user_password and login_driver:
            box_email = self._find_element_by(
                identifier=box_email_driver['identifier'],
                identifier_type=box_email_driver['identifier_type'],
            )
            box_password = self._find_element_by(
                identifier=box_password_driver['identifier'],
                identifier_type=box_password_driver['identifier_type'],
            )
            btn_submit = self._find_element_by(
                identifier=btn_submit_driver['identifier'],
                identifier_type=btn_submit_driver['identifier_type'],
            )

            box_email.send_keys(user_email)
            time.sleep(0.5)
            box_password.send_keys(user_password)

            btn_submit.click()
            time.sleep(0.5)
        
    def scroll_element_in_to_view(self, *args, **kwargs):
        
        element:WebDriver
        if 'element' in kwargs:
            element = kwargs['element']
        else:
            identifier_type:EnumIdentifierType
            identifier:str
            identifier_type = kwargs['identifier_type']
            identifier = kwargs['identifier']
            element = self._find_element_by(identifier_type, identifier)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    


