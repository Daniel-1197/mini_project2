# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class NewUserPage:
#     def __init__(self,driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver,20)
#
#     def go_to_add_user_form(self):
#         self.wait.until(EC.element_to_be_clickable((By.XPATH,'//span[text()="Admin"]'))).click()
#         self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[text()=" Add "]'))).click()
#
#     def select_user_role(self, role='Admin'):
#         user_role_dropdown = self.wait.until(
#             EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'oxd-select-text-input')])[1]")))
#         user_role_dropdown.click()
#         time.sleep(2)
#         self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@role='listbox']//span[text()='{role}']"))).click()
#
#     def select_employee(self, name='James Williams David'):
#         employee_name = self.wait.until(
#             EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))
#         employee_name.send_keys(name)
#         time.sleep(10)
#         self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='listbox']")))
#         employee_name_suggestion =self.wait.until(
#             EC.element_to_be_clickable((By.XPATH, f"//div[@role='option']//span[contains(text(),'{name}')]")))
#         employee_name_suggestion.click()
#
#     def select_status(self, status='Enabled'):
#         status_dropdown = self.wait.until(
#             EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'oxd-select-text-input')])[2]")))
#         status_dropdown.click()
#         time.sleep(2)
#         enabled_option = self.wait.until(
#             EC.element_to_be_clickable((By.XPATH, f"//div[@role='listbox']//span[text()='{status}']")))
#         enabled_option.click()
#
#     def fill_credentials(self):
#         user_name = self.wait.until(
#             EC.visibility_of_element_located((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")))
#         user_name.send_keys("TestUser04")
#         password =self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='password'])[1]")))
#         password.send_keys("Test@123")
#         confirm_password = self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='password'])[2]")))
#         confirm_password.send_keys("Test@123")
#     def click_save(self):
#         submit = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Save ']")))
#         submit.click()
#     def verify_user_created(self):
#         self.wait.until(EC.presence_of_element_located((By.XPATH, f"//div[text()='TestUser04']")))
#         return True

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewUserPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def go_to_add_user_form(self):
        # Wait for the "Admin" menu and click
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Admin"]'))).click()

        # Wait for "Add" button to be clickable and click
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()=" Add "]'))).click()

    def select_user_role(self, role='Admin'):
        # Wait for the user role dropdown to be clickable and click it
        user_role_dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'oxd-select-text-input')])[1]")))
        user_role_dropdown.click()

        # Wait for the role option to be clickable and select the role
        role_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='listbox']//span[text()='{role}']")))
        role_option.click()

    def select_employee(self, name='James Williams David'):
        # Wait for the employee search input to be visible and type the name
        employee_name = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))
        employee_name.send_keys(name)

        # Wait for the suggestions list to appear and select the employee name from the suggestions
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='listbox']")))

        employee_name_suggestion = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='option']//span[contains(text(),'{name}')]")))
        employee_name_suggestion.click()

    def select_status(self, status='Enabled'):
        # Wait for the status dropdown to be clickable and select it
        status_dropdown = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'oxd-select-text-input')])[2]")))
        status_dropdown.click()

        # Wait for the status option to be clickable and select the status
        status_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@role='listbox']//span[text()='{status}']")))
        status_option.click()

    def fill_credentials(self):
        # Wait for the username input to be visible and type the username
        user_name = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")))
        user_name.send_keys("TestUser04")

        # Wait for the password input to be visible and type the password
        password = self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='password'])[1]")))
        password.send_keys("Test@123")

        # Wait for the confirm password input to be visible and type the password again
        confirm_password = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@type='password'])[2]")))
        confirm_password.send_keys("Test@123")

    def click_save(self):
        # Wait for the save button to be clickable and click it
        submit = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Save ']")))
        submit.click()

    def verify_user_created(self):
        # Wait for the newly created user to be visible in the user list
        self.wait.until(EC.presence_of_element_located((By.XPATH, f"//div[text()='TestUser04']")))

        # Return True if the user is found (optional for confirmation)
        return True
