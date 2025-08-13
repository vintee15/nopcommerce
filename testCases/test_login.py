import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:   # Test_001_Login is test case id

    # valriable are hard coded
    # baseURL= "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    # username = "admin@yourstore.com"
    # password = "admin"

    # how to read value from .ini file using utilities file, is below
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    #
    #
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("********** Test_001_Login *********** ")
        self.logger.info("********* verifying Home page title *************")
        self.driver = setup   # return driver
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title =="nopCommerce demo store. Login":
            assert True
            self.driver.close()
            time.sleep(2)
            self.logger.info("********* Home page title test is passed *************")

        else:
            self.driver.save_screenshot("C:\\Users\\vchau\\PycharmProjects\\pythonformyself\\nopcommerce\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********* Home page title test is failed *************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self):
        self.logger.info("********* verifying login test *************")
        self.driver = webdriver.Edge()
        # self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver) #object creation for Login page class

        self.lp.setUserName(self.username)

        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** loged in ******")
        time.sleep(20)
        self.lp.clickLogout()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********* login test is passes *************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("********* login test is failed *************")
            assert False

    #

    #



