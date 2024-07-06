from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import datetime, timedelta
from time import sleep

def init_driver():
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    return driver

def wait_for_login(driver):
    print("Please scan the QR code to log in.")
    try:
        WebDriverWait(driver, 300).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )
        print("Logged in successfully!")
    except TimeoutException:
        print("Login timeout. Please ensure you scan the QR code within 5 minutes.")
        driver.quit()
        exit()

def send_message(driver, name, message, count):
    try:
        print(f"Searching for contact/group: {name}")
        user = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, f'//span[@title="{name}"]'))
        )
        user.click()
        
        print(f"Contact/group {name} found and clicked.")
        
        text_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
        )
        
        print("Text box located.")
        
        for i in range(count):
            print(f"Sending message {i+1}/{count}")
            text_box.send_keys(message)
            send_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Send"]'))
            )
            send_button.click()
            sleep(1)  # Short delay between messages

        print(f"Message sent to {name} successfully {count} times.")
        return True

    except (NoSuchElementException, TimeoutException) as e:
        print(f"An error occurred while sending the message: {e}")
        return False

def reps(driver):
    while True:
        ask_user = input("Do you want to send more messages to anyone? (y/n): ").lower()
        if ask_user == 'y':
            msg(driver)
        elif ask_user == 'n':
            print("Thank you, see you soon.")
            break
        else:
            print("Please enter a valid option.")

def msg(driver):
    name = input('\nEnter Group/User Name: ')
    message = f'Happy Birthday to you, {name}'
    count = int(input("Enter the message count: "))
    send_time = input("Enter the time (HH:MM) at which you want to send the message: ")
    
    # Parse the desired send time
    send_hour, send_minute = map(int, send_time.split(':'))
    
    # Get the current time and the target send time
    now = datetime.now()
    target_time = now.replace(hour=send_hour, minute=send_minute, second=0, microsecond=0)
    
    # If the target time is before the current time, schedule for the next day
    if target_time < now:
        target_time += timedelta(days=1)
    
    # Calculate the delay in seconds
    delay_seconds = (target_time - now).total_seconds()

    print(f"Waiting until {target_time.strftime('%H:%M')} to send the message...")
    sleep(delay_seconds)

    success = send_message(driver, name, message, count)
    if not success:
        print("Retrying...")
        msg(driver)

if __name__ == "__main__":
    driver = init_driver()
    try:
        wait_for_login(driver)
        msg(driver)
    finally:
        driver.quit()
