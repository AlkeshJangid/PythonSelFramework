from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    Text_username_Name = (By.NAME, "username")
    Text_Password_Name = (By.NAME, "password")
    Click_Login_Xpath = (By.XPATH, "//button[@type='submit']")
    Click_menu_Xpath = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    Click_Logout_Xpath = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):  # <<-- Constructor used to call itself automatically whenever the program starts
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    # we need to add the argument for sending keys
    def Enter_UserName(self, username):
        self.wait.until(expected_conditions.presence_of_element_located(self.Text_username_Name))
        self.driver.find_element(*Login.Text_username_Name).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(*Login.Text_Password_Name).send_keys(password)

    def Click_Login(self):  # <<--here, no need to write argument because we are using Click()
        self.driver.find_element(*Login.Click_Login_Xpath).click()

    def Login_Status(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located(self.Click_menu_Xpath))
            self.driver.find_element(*Login.Click_menu_Xpath)
            return True
        except (NoSuchElementException,TimeoutException):
            return False
            pass

    def Click_Menu_Button(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.Click_menu_Xpath))
        self.driver.find_element(*Login.Click_menu_Xpath).click()

    def Click_Logout_Button(self):
        self.driver.find_element(*Login.Click_Logout_Xpath).click()









