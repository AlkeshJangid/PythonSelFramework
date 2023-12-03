import pytest
import time
from selenium.webdriver.common.by import By
from pageObject.LoginPage import Login
from utilities.Logger import LogGen
from utilities.ReadConfigFile import ReadValue


class Test_URL_Login:
    username = ReadValue.getUsername()
    password = ReadValue.getPassword()
    log = LogGen.loggen()
    URL = ReadValue.getURL()

    @pytest.mark.Sanity
    def test_url_001(self, setup):
        self.driver = setup
        self.driver.get(self.URL)
        # self.log.debug("Debug Message")
        # self.log.info("Info Message")
        # self.log.warning("Warning message")
        # self.log.error("Error Message")
        # self.log.critical("Critical Message")
        self.log.info("Openning Browser")
        self.log.info("Check Page title")
        if self.driver.title == "OrangeHRM":
            self.log.info(f'You are in correct site --> {self.driver.title}')
            time.sleep(1)
            self.driver.save_screenshot("F:\\Testing Documents\\Pycharm Practice\\OrangeHRMFramework\\Screenshots\\test_url_001_pass.png")
            assert True
            self.driver.close()        #<<-- Closing driver here
            self.log.info(" test_url_001 : Logout and Completed ")
        else:
            self.log.info(" test_url_001 : Failed ")
            self.driver.save_screenshot("F:\\Testing Documents\\Pycharm Practice\\OrangeHRMFramework\\Screenshots\\test_url_001_fail.png")
            assert False


    @pytest.mark.Sanity
    def test_login_002(self, setup):

        self.log.info("Openning Browser")
        self.driver = setup
        self.driver.get(self.URL)
        self.log.info("Check Page title")
        self.lp = Login(self.driver)
        self.lp.Enter_UserName(self.username)
        self.log.info("Enter Username :" + self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Enter Password :" + self.password)
        self.lp.Click_Login()
        self.log.info("Click on Login Button")
        self.lp.Login_Status()

        if self.lp.Login_Status() == True:
            assert True
            self.log.info("test_login_002 Status : PASS")
            self.driver.save_screenshot("F:\\Testing Documents\\Pycharm Practice\\OrangeHRMFramework\\Screenshots\\test_login_002_pass.png")
            self.lp.Click_Menu_Button()
            self.log.info("Click on Menu Button")
            self.lp.Click_Logout_Button()
            self.log.info("Click on Logout Button")

        else:
            self.log.info("test_login_002 Status : FAILED")
            self.driver.save_screenshot("F:\\Testing Documents\\Pycharm Practice\\OrangeHRMFramework\\Screenshots\\test_login_002_fail.png")
            assert False

        self.driver.close()
        self.log.info("test_login_002 is Completed")
