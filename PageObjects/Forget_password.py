from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Fp_validation:
    link_FPWord_cssSelector = ".oxd-text.oxd-text--p.orangehrm-login-forgot-header"
    txt_Reset_username_xpath = "//input[@name='username']"
    btn_Reset_xpath = "//button[@type='submit']"
    title_forget_xpath = "//h6[@class='oxd-text oxd-text--h6 orangehrm-forgot-password-title']"

    def __init__(self, driver):
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver, 10)

    def Click_F_PWord(self):
        self.WebDriverWait.until(
            (EC.presence_of_element_located((By.CSS_SELECTOR, self.link_FPWord_cssSelector)))).click()

    def ResetUsername(self, username):
        self.driver.find_element(By.XPATH, self.txt_Reset_username_xpath).send_keys(username)

    def ClickReset(self):
        self.driver.find_element(By.XPATH, self.btn_Reset_xpath).click()

    def ResetPWord_Title(self):
        ele = self.driver.find_element(By.XPATH, self.title_forget_xpath)
        return ele

    def username_visible(self):
        User = self.driver.find_element(By.XPATH, self.txt_Reset_username_xpath)
        User.is_displayed()
        return True
