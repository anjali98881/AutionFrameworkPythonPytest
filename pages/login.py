from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, 'username')
        self.password_input = (By.NAME, 'password')
        self.login_button = (By.ID, 'btn-login')
        self.appointment_page_heading = (By.XPATH, '//*[@id="appointment"]/div/div/div/h2')
    
    def login(self, username, password):
        self.driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_input))
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
    
    def is_logged_in(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.appointment_page_heading))
            return True
        except TimeoutException:
            return False
    
    def capture_screenshot(self, filename):
        self.driver.save_screenshot(f"{filename}.png")
