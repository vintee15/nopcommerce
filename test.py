import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import uuid

obj1 = Options()
obj1.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=obj1)
mywait = WebDriverWait(driver, 50, poll_frequency= 2)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

mywait.until(EC.element_to_be_clickable((By.NAME, "username"))).send_keys("Admin")
mywait.until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()


mywait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"))).click()
mywait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']"))).click()

mywait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'oxd-select-text')])[1]"))).click()
role = "Admin"
if role == "ESS":
     mywait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//span[text()='ESS']"))).click()

elif role == "Admin":
    mywait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//span[text()='Admin']"))).click()
else:
    print("❌ Invalid user role provided")

mywait.until(EC.element_to_be_clickable((By.XPATH,
    "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]"))).click()

# Pick "Enabled" or "Disabled"
# Enabled is typically third child -> index 2 if zero‑based
mywait.until(EC.element_to_be_clickable((By.XPATH,
    "(//div[@role='listbox']//child::div)[2]"))).click()

emp_input = mywait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))
emp_input.send_keys("a")  # 'a' gives multiple suggestions

# Wait for dropdown suggestions to appear
suggestions = mywait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "//div[@role='listbox']//span")))


# Choose a random one from suggestions
random_employee = random.choice(suggestions)
random_employee_name = random_employee.text
random_employee.click()

print(f"Selected employee: {random_employee_name}")

# Enter random username
random_username = "user_" + str(uuid.uuid4())[:8]
driver.find_element(By.XPATH, "//label[text()='Username']/../following-sibling::div//input").send_keys(random_username)
# driver.find_element(By.XPATH, "").send_keys(random_username)

# Enter random password

mywait.until(EC.element_to_be_clickable((By.XPATH, "//label[text() = 'Password']/../following-sibling::div//input"))
             ).send_keys('12345vin')
mywait.until(EC.element_to_be_clickable((By.XPATH, "//label[text() = 'Confirm Password']/../following-sibling::div//input"))
             ).send_keys('12345vin')


mywait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))).click()
# try:
#     password_input = mywait.until(EC.element_to_be_clickable(
#         (By.XPATH, "//label[text()='Password']/../following-sibling::div//input")
#     ))
#     password_input.send_keys('abc123')
# except Exception as e:
#     print("❌ Exception:", e)



# # Fill the Search Form
# # -----------------------------
#
# # 1. Username
# driver.find_element(By.XPATH, "//label[text()='Username']/../following-sibling::div/input").send_keys("Admin")
#
# # 2. User Role dropdown
# wait.until(EC.element_to_be_clickable((By.XPATH,
#     "//label[text()='User Role']/../following-sibling::div//div[contains(@class,'oxd-select-text')]"))).click()
# wait.until(EC.element_to_be_clickable((By.XPATH,
#     "//div[@role='listbox']//div[text()='Admin']"))).click()
#
# # 3. Employee Name (with autocomplete)
# emp_input = driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
# emp_input.send_keys("Linda")  # Start typing a real employee
# time.sleep(2)  # wait for suggestions
# driver.find_element(By.XPATH, "//div[@role='listbox']//span[text()='Linda Anderson']").click()
#
# # 4. Status dropdown
# wait.until(EC.element_to_be_clickable((By.XPATH,
#     "//label[text()='Status']/../following-sibling::div//div[contains(@class,'oxd-select-text')]"))).click()
# wait.until(EC.element_to_be_clickable((By.XPATH,
#     "//div[@role='listbox']//div[text()='Enabled']"))).click()
#
# # 5. Click Search
# driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
#
# time.sleep(3)
#
# # Optional: Click Reset
# driver.find_element(By.XPATH, "//button[normalize-space()='Reset']").click()
#
# # Cleanup
# time.sleep(2)
# driver.quit()