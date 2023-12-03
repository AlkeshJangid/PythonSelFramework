import pytest
from pageObject.LoginPage import Login
from utilities.Logger import LogGen
from utilities.ReadConfigFile import ReadValue

class Test_Login_Params:
    log = LogGen.loggen()
    URL = ReadValue.getURL()

    @pytest.mark.regression
    def test_login_params_003(self, setup, getDataForLogin):
        self.log.info("Openning Browser")
        self.driver = setup
        self.driver.get(self.URL)
        self.log.info("Check Page title")
        self.lp = Login(self.driver)
        self.lp.Enter_UserName(getDataForLogin[0])
        self.log.info("Enter Username :" + getDataForLogin[0])
        self.lp.Enter_Password(getDataForLogin[1])
        self.log.info("Enter Password :" + getDataForLogin[1])
        self.lp.Click_Login()
        self.log.info("Click on Login Button")

        login_status=[]
        if self.lp.Login_Status() == True:
            if getDataForLogin[2] == "Pass":
                login_status.append("Pass")

                self.driver.save_screenshot("F:\\Testing Documents\\Pycharm Practice\\OrangeHRMFramework\\Screenshots\\test_login_params_003_pass.png")
                self.lp.Click_Menu_Button()
                self.log.info("Click on Menu Button")
                self.lp.Click_Logout_Button()
                self.log.info("Click on Logout Button")
            elif getDataForLogin[2] == "Fail":
                login_status.append("Fail")
                self.driver.save_screenshot("F:\\Testing Documents\\Pycharm Practice\\OrangeHRMFramework\\Screenshots\\test_login_params_003_Fail.png")
                self.lp.Click_Menu_Button()
                self.log.info("Click on Menu Button")
                self.lp.Click_Logout_Button()
                self.log.info("Click on Logout Button")

        else:
            if getDataForLogin[2] == "Fail":
                login_status.append("Pass")
                self.driver.save_screenshot("F:\\Testing Documents\\Pycharm Practice\\OrangeHRMFramework\\Screenshots\\test_login_params_003_pass.png")

            elif getDataForLogin[2] == "Pass":
                login_status.append("Fail")
                self.driver.save_screenshot("F:\\Testing Documents\\Pycharm Practice\\OrangeHRMFramework\\Screenshots\\test_login_params_003_fail.png")
        print(login_status)

        if "Fail" not in login_status:
            self.log.info("test_login_Param_003 is Passed")
            assert True
        else:
            self.log.info("test_login_Param_003 is Failed")
            assert False
        self.driver.close()