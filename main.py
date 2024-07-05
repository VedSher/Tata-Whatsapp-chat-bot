from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from Whatsapp import Whatsapp  # Assuming Whatsapp class is in a file named 'whatsapp.py'

driver = webdriver.Chrome()

def msg():
    name = input("\nEnter Group/User Name: ")
    message = input("\nEnter your message to Group/User: ")
    count = int(input("\nEnter the number of times you want to send the message: "))

    whatsapp = Whatsapp(driver)
    whatsapp.open_page()

    try:
        print(f"Opening chat with '{name}'...")
        whatsapp.open_chat_with(name)
        time.sleep(3)  # Wait for the chat to open (adjust if necessary)

        print(f"Sending message '{message}' {count} times...")
        for _ in range(count):
            whatsapp.type_message(message)
            send_button = whatsapp._find_element('//button[@data-testid="send"]')
            send_button.click()
            time.sleep(1)  # Add a slight delay between messages if necessary

        if whatsapp.is_last_message_sent():
            print(f"Message '{message}' sent {count} times to '{name}'.")
        else:
            print(f"Failed to send message '{message}' to '{name}'.")

    except TimeoutException as e:
        print(f"Timeout Error: {e} - Could not locate the element within the given time.")
    except NoSuchElementException as e:
        print(f"Element Not Found: {e} - Check the XPath or class names.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def reps():
    while True:
        ask_user = input("Do you want to send more messages to anyone? (y/n): ").lower()
        if ask_user == 'y':
            msg()
        elif ask_user == 'n':
            print("Thank you, see you soon!")
            driver.quit()  # Close the browser window
            break
        else:
            print("Please enter a valid option (y/n):")

reps()
