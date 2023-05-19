from selenium.webdriver.common.by import By


# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select


class loginpage:
    textbox_username_xpath = "//input[@name='username']"
    textbox_password_xpath = "//input[@type='password']"
    button_login_xpath = "//button[@type='submit']"
    dr_logout_xpath = "//p[@class='oxd-userdropdown-name']"
    button_logout_xpath = "//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, valid_username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(valid_username)

    def setPassword(self, valid_password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(valid_password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.XPATH, self.dr_logout_xpath).click()
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()




