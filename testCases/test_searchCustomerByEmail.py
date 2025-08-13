import time

import pytest

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseURL= ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()      #logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("*****searchCustomerByEmail_004 ************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*******login successful *********")

        self.logger.info("******* starting search customer by email *********")

        self.addcust= AddCustomer(self.driver)
        self.addcust.clickonCustomerMenu()
        self.addcust.clickonCustomerMenuItem()

        self.logger.info("****** searching customer by emailID ************")

        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setEmail("steve_gates@nopCommerce.com")
        self.searchcust.clickSearch()
        time.sleep(10)


        status = self.searchcust.searchCustomerByEmail("steve_gates@nopCommerce.com")

        assert True == status

        self.logger.info("******* TC_SearchCustomerByEmail_004 Finished *******")

