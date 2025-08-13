import time, random

from selenium.common import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddCustomer:
    # add customer page

    lnkCustomers_menu_xpath = "//p[contains(text(),'Customers')]"
        #"//a[@href='#']//p[contains(text(),'Customers')]"
    #//p[normalize-space()='Customers']
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtCompanyName_xpath = "//input[@id='Company']"
    chIStaxexempt_xpath = "//input[@id='IsTaxExempt']"
    txtcustomerRoles_xpath = "//select[@id='SelectedCustomerRoleIds']"
    listitemForumModerators_xpath = "//li[@title='Forum Moderators']"
    listitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    listitemvendors_xpath = "//li[contains(text(), 'Vendors')]"
    listitemAdministrators_xpath = "//li[contains(text(), 'Administrators')]"
    listitemGuests_xpath = "//li[contains(text(),'Guests')]"
    drpmgofVendor_xpath = "//select[@id='VendorId']"
    chActive_xpath = "//input[@id='Active']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver # this constructor will get driver from actual testcase and will intiate local driver

    def clickonCustomerMenu(self):
        # self.driver.find_element("xpath", self.lnkCustomers_menu_xpath).click()
        menu = WebDriverWait(self.driver, 100, poll_frequency= 5).until(
        EC.element_to_be_clickable(("xpath", self.lnkCustomers_menu_xpath))).click()



    def clickonCustomerMenuItem(self):
         # self.driver.find_element("xpath", self.lnkCustomers_menuitem_xpath).click()
         # menuitem = WebDriverWait(self.driver, 100, poll_frequency= 5).until(
         #     EC.element_to_be_clickable(("xpath", self.lnkCustomers_menuitem_xpath))).click()
         timeout = 20  # max time to wait
         poll = 0.5  # poll every 0.5 sec

         wait = WebDriverWait(
             self.driver,
             timeout,
             poll_frequency=poll,
             ignored_exceptions=[NoSuchElementException, ElementClickInterceptedException]
         )

         try:
             # Wait until menu item is clickable, then click
             elem = wait.until(EC.element_to_be_clickable(("xpath", self.lnkCustomers_menuitem_xpath)))
             elem.click()
         except TimeoutException:
             print(f"Menu Item not clickable within {timeout} seconds")

    try:
     def clickonAddNew(self):
        addnew = WebDriverWait(self.driver, 100, poll_frequency= 5).until(
            EC.element_to_be_clickable(("xpath", self.btnAddnew_xpath))).click()
        # self.driver.find_element("xpath", self.btnAddnew_xpath).click()
    except TimeoutException:
     print("element not found within 10 seconds")

    def setEmail(self, email):
        # self.driver.find_element("xpath", self.txtEmail_xpath).send_keys(email)
        email = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(("xpath", self.txtEmail_xpath))).click()

    def setPassword(self, password):
        self.driver.find_element("xpath", self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element("xpath", (self.txtFirstName_xpath)).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element("xpath", self.txtLastName_xpath).send_keys(lname)

    def setCustomerRoles(self, role):
        self.driver.find_element("xpath", self.txtcustomerRoles_xpath).click()
        time.sleep(3)

        if role == "Registered":
            self.listitem = self.driver.find_element("xpath", self.listitemRegistered_xpath)

        elif role == "Adminstrators":
            self.listitem = self.driver.find_element("xpath", self.listitemAdministrators_xpath)

        elif role == "Guests":
            # here user can registered or guests, only one can select at a time
            time.sleep(3)
            self.driver.find_element("xpath", "//li[@class='select2-selection__choice']//span[@class='select2-selection__choice__remove']").click()
            self.listitem = self.driver.find_element("xpath", self.listitemGuests_xpath)

        elif role == "Registered":
            self.listitem = self.driver.find_element("xpath", self.listitemRegistered_xpath)

        elif role == "Vendors":
            self.listitem = self.driver.find_element("xpath", self.listitemvendors_xpath)

        else:
            self.listitem = self.driver.find_element("xpath", self.listitemGuests_xpath)

        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element("xpath", self.drpmgofVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == "Male":
            male= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(("id", self.rdMaleGender_id)))
            self.driver.execute_script('argument[0].click();', male)
        elif gender == "Female":
            self.driver.find_element("id", self.rdFemaleGender_id).click()

        else:
            male = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(("id", self.rdMaleGender_id)))
            self.driver.execute_script('argument[0].click();', male)

    def setCompanyName(self, Comname):
        self.driver.find_element("xpath", self.txtCompanyName_xpath)

    def setAdminContent(self, content):
        self.driver.find_element("xpath", self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element("xpath", self.btnSave_xpath).click()


