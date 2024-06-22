from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging
import os


class SeleniumActions:

    def __init__(self):
        self.driver = None

    def start_webdriver_chrome(self):
        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': 'D:\Archivo\Codes\ElectricCarAutomation\Downloads'}
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        time.sleep(1)
        self.driver.get("https://catalog.data.gov/dataset/")
        self.driver.maximize_window()
        return self.driver


    def close_browser(self, driver):
        driver.close()
        driver.quit()
