from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    txt_username_id="Email"
    txt_password_id="Password"
    button_login_xpath="//button[normalize-space()='Log in']"
    link_logout_xpath = "//a[normalize-space()='Logout']"
    # link_logout_linktext="Logout"


# we need to implement action method for every locator but before doing this we need to intilize drive. for this we create a contructor
    def __init__(self, driver): # it is python constructor. it automatically invoke at the time of objet creation
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element("id", self.txt_username_id).clear()
        self.driver.find_element("id", self.txt_username_id).send_keys(username)

        wait = WebDriverWait(self.driver, 20)
        email_field = wait.until(EC.presence_of_element_located(("id", self.txt_username_id)))
        # email_field = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        email_field.clear()
        email_field.send_keys(username)

    def setPassword(self, password):

        self.driver.find_element("id", self.txt_password_id).clear()
        self.driver.find_element("id", self.txt_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element("xpath", self.button_login_xpath).click()

    def clickLogout(self):
        # self.driver.find_element("xpath", self.link_logout_xpath).click()
        logout = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(("xpath", self.link_logout_xpath))
        )
        logout.click()
