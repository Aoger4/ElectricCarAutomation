from seleniumActions import SeleniumActions
from findTesla import FindTesla

if __name__ == "__main__":
   sa = SeleniumActions()
   driver = sa.start_webdriver_chrome()
   tesla = FindTesla()
   tesla.wait_for_load_page(driver)
   tesla.make_search_on_bar(driver)
   tesla.click_on_result(driver)
   tesla.download_file(driver)
   tesla.count_tesla_word(driver)
   sa.close_browser(driver)