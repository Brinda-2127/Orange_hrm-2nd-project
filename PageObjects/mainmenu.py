from selenium.webdriver.common.by import By


class Main_menu:
    link_MainMenu_xpath = "//li[contains(@class,'oxd-main-menu-item-wrapper')]"

    def __init__(self, driver):
        self.driver = driver

    def set_MainMenu_Items(self):
        Items = self.driver.find_elements(By.XPATH, self.link_MainMenu_xpath)
        return Items
