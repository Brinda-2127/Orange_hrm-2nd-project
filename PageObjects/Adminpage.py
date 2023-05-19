from selenium.webdriver.common.by import By


class Admin_Option:
    link_admin_xpath = "//span[text()='Admin']"
    link_admin_elements_xpath = "//li[contains(@class,'oxd-topbar-body-nav-tab')]"

    def __init__(self, driver):
        self.driver = driver

    def Click_admin(self):
        self.driver.find_element(By.XPATH, self.link_admin_xpath).click()

    def set_admin_elements(self):
        elem = self.driver.find_elements(By.XPATH, self.link_admin_elements_xpath)
        return elem
