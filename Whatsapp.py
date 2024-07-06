from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException

class Whatsapp:
    WHATSAPP_URL = "https://web.whatsapp.com/"

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("https://web.whatsapp.com")

    def _find_element(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def type_message(self, message):
        message_box = self._find_element('//div[@contenteditable="true"][@data-tab="10"]')
        message_box.send_keys(message)

    def is_last_message_sent(self):
        try:
            # Example implementation based on WhatsApp Web behavior
            last_message_status = self._find_element('//span[@data-icon="msg-check"]')
            return True if last_message_status else False
        except NoSuchElementException:
            return False
# Example usage in your main script
if __name__ == "__main__":
    from selenium import webdriver

    driver_path = '/path/to/chromedriver'
    driver = webdriver.Chrome(executable_path=driver_path)

    whatsapp = Whatsapp(driver)
    whatsapp.open_page()

    # Close the browser session
    driver.quit()
