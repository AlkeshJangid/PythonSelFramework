from pageObject.LoginPage import Login
import time
from utilities import XLutilis
from utilities.Logger import LogGen
from utilities.ReadConfigFile import ReadValue


class Test_DDT:
    log = LogGen.loggen()
    URL = ReadValue.getURL()
    path = "F:\\Testing Documents\\Pycharm Practice\\OrangeHRMFramework\\TestData\\Login_Credentials.xlsx"

    def test_login_ddt_004(self, setup):
        self.log.info("Openning Browser")
        self.driver = setup
        self.driver.get(self.URL)
        self.log.info("Check Page title")
        self.lp = Login(self.driver)
        self.rows = XLutilis.getrowCount(self.path, "Sheet1")
        print("Number Of Rows -->", self.rows)
        login_Status=[]
        for r in range (2, self.rows+1):
            self.username = XLutilis.readData(self.path, "Sheet1", r, 1)
            self.password = XLutilis.readData(self.path, "Sheet1", r, 2)
            self.Exp_Status = XLutilis.readData(self.path, "Sheet1", r, 3)
            time.sleep(1)
            self.lp.Enter_UserName(self.username)
            self.log.info("Enter Username :" + self.username)
            self.lp.Enter_Password(self.password)
            self.log.info("Enter Password :" + self.password)
            self.lp.Click_Login()
            self.log.info("Click on Login Button")
            self.lp.Login_Status()
            login_status = []
            if self.lp.Login_Status() == True:
                if self.Exp_Status == "Pass":
                    login_status.append("Pass")

                    self.driver.save_screenshot(
                        "F:\\Testing Documents\\Pycharm Practice\\OrangeHRMFramework\\Screenshots\\test_login_params_003_pass.png")
                    self.lp.Click_Menu_Button()
                    self.log.info("Click on Menu Button")
                    self.lp.Click_Logout_Button()
                    self.log.info("Click on Logout Button")
                    XLutilis.writeDate(self.path, "Sheet1", r, 4, "Pass")
                elif self.Exp_Status == "Fail":
                    login_status.append("Fail")
                    self.driver.save_screenshot(
                        "F:\\Testing Documents\\Pycharm Practice\\OrangeHRMFramework\\Screenshots\\test_login_params_003_Fail.png")
                    self.lp.Click_Menu_Button()
                    self.log.info("Click on Menu Button")
                    self.lp.Click_Logout_Button()
                    self.log.info("Click on Logout Button")
                    XLutilis.writeDate(self.path, "Sheet1", r, 4, "Fail")

            else:
                if self.Exp_Status == "Fail":
                    login_status.append("Pass")
                    self.driver.save_screenshot(
                        "F:\\Testing Documents\\Pycharm Practice\\OrangeHRMFramework\\Screenshots\\test_login_params_003_pass.png")
                    XLutilis.writeDate(self.path, "Sheet1", r, 4, "Fail")

                elif self.Exp_Status == "Pass":
                    login_status.append("Fail")
                    self.driver.save_screenshot(
                        "F:\\Testing Documents\\Pycharm Practice\\OrangeHRMFramework\\Screenshots\\test_login_params_003_fail.png")
                    XLutilis.writeDate(self.path, "Sheet1", r, 4, "Fail")
            print(login_status)

            if "Fail" not in login_status:
                self.log.info("test_login_ddt_004 is Passed")
                assert True
            else:
                self.log.info("test_login_ddt_004 is Failed")
                assert False
            self.driver.close()



