import time

import pytest
import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.Forget_password import Fp_validation
from Utilities.ReadProperties import readconfig
from Utilities.customLogger import LogGen
from PageObjects.loginpage import loginpage
from PageObjects.Adminpage import Admin_Option
from PageObjects.mainmenu import Main_menu


class Test_Reset_Password:
    baseURL = readconfig.getApplicationURL()
    username = readconfig.getusername()
    UserName = readconfig.getUser_Name()
    password = readconfig.getpassword()

    logger = LogGen.loggen()

    def test_Forget_password(self, setup):
        self.logger.info("******************Test__001__Login*****************")
        self.logger.info("*****************Verifying Home Page Title*****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.rp = Fp_validation(self.driver)
        self.rp.Click_F_PWord()
        self.logger.info("**************Forget password validation Start***********")
        act_msg = "Reset Password link sent successfully"
        if self.rp.username_visible():
            self.rp.ResetUsername("Brinda")
            self.rp.ClickReset()
            exp_msg = self.rp.ResetPWord_Title().text
            if exp_msg == act_msg:
                assert True
                self.logger.info("********Forget Password Validation Test Passed**********")
            else:
                assert False
            self.logger.info("********Forget Password Validation Test failed**********")
        else:
            print("username  not visible")
            self.logger.info("**************user name not visible******** ")

    def test_adminpage_title(self, setup):
        self.logger.info("****************Verifying admin title  Test ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.setUserName(self.UserName)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.AP = Admin_Option(self.driver)
        self.AP.Click_admin()
        act_title = self.driver.title
        time.sleep(10)
        print(act_title)
        if act_title == "OrangeHRM":
            elements = self.AP.set_admin_elements
            for ele in elements():
                if ele.is_displayed:
                    print('element is visible', ele.text)
                    assert True
                else:
                    print('element is not visible')
                    assert False
        else:
            print('title is wrong', act_title)
            assert False
        self.driver.close()

    def test_MainMenu(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = loginpage(self.driver)
        self.lp.setUserName(self.UserName)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        self.AP = Admin_Option(self.driver)
        self.MM = Main_menu(self.driver)
        self.AP.Click_admin()
        act_title = self.driver.title
        time.sleep(10)
        print(act_title)
        if act_title == "OrangeHRM":
            elements1 = self.MM.set_MainMenu_Items()
            for ele in elements1:
                if ele.is_displayed():
                    print('Item is visible', ele.text)
                    assert True
                else:
                    print('items is not visible')
                    assert False
        else:
            print('title is wrong', act_title)
            assert False
        self.driver.close()
