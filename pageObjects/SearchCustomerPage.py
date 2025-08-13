from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SearchCustomer:
    #add customer page
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btn_Search_id = "search-customers"

    tblSearchResults_xpath = "//div[@id='customers-grid_wrapper']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath= "//table[@id='customers-grid']//tbody/tr/td"


    def __init__(self, driver):
        self.driver=driver


    def setEmail(self, email):
        # self.driver.find_element("id", self.txtEmail_id).clear()
        emaillocator = WebDriverWait(self.driver, 20, poll_frequency=2).until(EC.presence_of_element_located(("id", self.txtEmail_id)))
        emaillocator.send_keys(email)

    def setFirstname(self, fname):
        # self.driver.find_element("id", self.txtFirstName_id).clear()
        fnamelocator = WebDriverWait(self.driver, 100, poll_frequency=2).until(EC.presence_of_element_located(("id", self.txtFirstName_id)))
        fnamelocator.send_keys(fname)
    def setLastname(self, lname):
        # self.driver.find_element("id", self.txtLastName_id).clear()
        lnamelocator = WebDriverWait(self.driver, 20, poll_frequency=2).until(EC.presence_of_element_located(("id", self.txtLastName_id)))
        lnamelocator.send_keys(lname)
    def clickSearch(self):
        self.driver.find_element("id", self.btn_Search_id)


    def getNoOfRows(self):
        return len(self.driver.find_elements("xpath", self.tableRows_xpath))
    def getNoOfColums(self):
        return len(self.driver.find_elements("xpath", self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        mywait = WebDriverWait(self.driver, 20, poll_frequency=2)
        flag = False

        for r in range(1, self.getNoOfRows()+1):
            table =self.driver.find_element("xpath", self.table_xpath)
            # emailid=table.find_element("xpath", "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text

            rowele = mywait.until(EC.presence_of_element_located(("xpath", "//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]")))
            emailid=rowele.text
            if emailid == email:
                flag = True
        return flag

    def searchCustomerByName(self, Name):
        mywait = WebDriverWait(self.driver, 20, poll_frequency=2)
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element("xpath", self.table_xpath)
            # name = table.find_element("xpath", "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[3]").text
            name = mywait.until(EC.presence_of_element_located(("xpath", "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[3]"))).text
            print(name)
            if name == Name:
                flag = True
        return flag