import time, csv
from selenium.webdriver.common.by import By


class FindTesla:


    def __init__(self):
        self.driver = None


    def wait_for_load_page(self, driver):
        load = len(driver.find_elements(By.XPATH, "//div[contains(text(), 'datasets found')]"))
        while load == 0:
            time.sleep(0.5)
            load = len(driver.find_elements(By.XPATH, "//div[contains(text(), 'datasets found')]"))

    
    def make_search_on_bar(self, driver):
        driver.find_element(By.ID, "search-big").send_keys('electric car')
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        time.sleep(2)


    def click_on_result(self, driver):
        driver.find_element(By.XPATH, "//a[text()='Electric Vehicle Population Data']").click()
        time.sleep(1.5)


    def download_file(self, driver):
        driver.execute_script("window.scrollBy(0, 100);")
        time.sleep(1)
        driver.find_element(By.XPATH, "//a[text()=' Download ']").click()
        time.sleep(30)
        

    def count_tesla_word(self, driver): 
        count = 0
        with open('D:\Archivo\Codes\ElectricCarAutomation\Downloads\Electric_Vehicle_Population_Data.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                for campo in row:
                    words = campo.split(',')
                    for word in words:
                        if word == 'TESLA':
                            count += 1
        print('Se terminó de buscar y la palabra TESLA aparece:', count, 'veces  en el archivo')

