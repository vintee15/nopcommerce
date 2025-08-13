import time

import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.customLogger import LogGen
import string
import random
from utilities.readProperties import ReadConfig


# def random_generator():
#     pass

def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))



class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger =LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("*******Test_003_AddCustomer ***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** LoginSuccesful ***********")

        self.logger.info("******** Starting add cutomer Test **********")

        time.sleep(10)
        self.addcust = AddCustomer(self.driver)


        self.addcust.clickonCustomerMenu()
        self.addcust.clickonCustomerMenuItem()
        self.logger.info("**** till here is workinh ******")
        self.driver.save_screenshot(".\\Screenshots\\" + "test_error.png")
        self.addcust.clickonAddNew()
        self.logger.info("****** providing customer info *******")
        self.logger.info("**** till2 here is workinh ******")
        self.driver.save_screenshot(".\\Screenshots\\" + "test_error2.png")

        self.email = random_generator()+"@gamil.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Vintee")
        self.addcust.setLastName("Chaudhary")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing ......")
        self.addcust.clickOnSave()

        self.logger.info("******* saving cutomer info ********")

        self.logger.info("******** add customer validation started ********")

        self.msg = self.driver.find_element("tag_name", "body").text
        print(self.msg)

        if "customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("**** Add customer test passed *******")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcustomer_scr.png")
            self.logger.error("******* Add customer test Failed ******")
            assert True == False

        self.driver.close()
        self.logger.info("***** Ending Home Page Title Test")