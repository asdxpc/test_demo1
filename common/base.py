from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.log import Get_log
from config.setting_path import screen_path
from selenium.common.exceptions import TimeoutException
import time
from selenium import webdriver
driver =webdriver.Chrome()
driver.get_screenshot_as_file()

#公用的基础操作类
class BasePage:
    def __init__(self,driver,url):
        self.driver =driver
        self.url =url
        self.log =Get_log()

    def open_browser(self):
        self.driver.get(self.url)

    def wait_element(self,ele):
        try:
            WebDriverWait(self.drive,5,0.5).until(EC.visibility_of_element_located(ele))
            return True
        except TimeoutException:
            self.log.log_error(f'没有定位到元素{ele}')
            return False
        except Exception as e:
            raise e

    def find_ele(self,ele):
        if self.wait_element(ele):
            try:
                return self.drive.find_element(*ele)
            except Exception as e:
                raise e
        else:
            self.log.log_error(f'没有定位到元素{ele}')
            return False
    #点击定位元素
    def click(self,div_click):
        self.find_ele(div_click).click()

    def send_key(self,div,data):
        self.find_ele(div).send_key(data)

    def get_text(self,ele):
        return self.find_ele(ele).text

    def get_curr_url(self):
        url =self.driver.current_url()
        return url
    #截图
    def get_screen_shot(self):
        current_time = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
        file_name = screen_path+'\\'+current_time+'.png'
        self.driver.get_screenshot_as_file(file_name)
        self.driver.get_screenshot(file_name)
