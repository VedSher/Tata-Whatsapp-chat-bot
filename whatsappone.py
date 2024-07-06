from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from Whatsapp import Whatsapp

# Ensure the path to chromedriver is correct
driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com")

def msg():
    name = input("\nEnter Group/User Name: ")
    message = input("\nEnter your message to Group/User: ")
    count = int(input("\nEnter the number of times you want to send the message: "))

    whatsapp = Whatsapp(driver)

    try:
        # Wait for the user element using XPath with contains (consider more specific XPaths)
        print(f"Waiting for the contact or group '{name}' to appear...")
        user = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, f'//span[@title="{name}"]'))
        )
        user.click()

        print(f"Opening chat with '{name}'...")
        time.sleep(3)  # Wait for the chat to open (adjust if necessary)

        # Use a different method to locate the text box
        print(f"Sending message '{message}' {count} times...")
        time.sleep(3)
        for _ in range(count):
            whatsapp.type_message(message)
            send_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, f'//span[@data-icon="send"]'))
            )
            send_button.click()
            time.sleep(3)  # Add a slight delay between messages if necessary

        # if whatsapp.is_last_message_sent():
        #     print(f"Message '{message}' sent {count} times to '{name}'.")
        # else:
        #     print(f"Failed to send message '{message}' to '{name}'.")

    except TimeoutException as e:
        print(f"Timeout Error: {e} - Could not locate the element within the given time.")
    except NoSuchElementException as e:
        print(f"Element Not Found: {e} - Check the XPath or class names.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def reps():
    print("Do you want to send more messages to anyone?")
    askUser = input("Press y for Yes and n for No: ")
    if askUser.lower() == 'y':
        msg()
        reps()
    elif askUser.lower() == 'n':
        print("Thank you, see you soon!")
        driver.quit()  # Close the browser window
    else:
        print("Please enter a valid option:\n")
        reps()

reps()