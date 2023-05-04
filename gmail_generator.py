#! python3

#   Author      : Stavros Grigoriou
#   Updated    : yungK1LL
#   GitHub      : https://github.com/unix121
#   GitHub      : https://github.com/blooditrix
#   Year        : 2018
#   Description : [Updated]Script that generates random Gmail account. Still stalls at phone verification.

import pyautogui
import sys
import time
import random
import string

# Printing funtion with 3 modes
# 1 : Normal message
# 2 : Information message
# 3 : Caution message
def msg(
        _option_,
        _message_
        ):
    if _option_ == 1:
        print('\x1b[0;32;40m> %s\x1b[0m' % _message_)
    elif _option_ == 2:
        print('\x1b[0;32;40m>\x1b[0m %s' % _message_)
    elif _option_ == 3:
        print('\n\x1b[0;32;40m[\x1b[0m%s\x1b[0;32;40m]\x1b[0m' % _message_)
    else:
        print('\n\x1b[0;31;40m[ERROR]\x1b[0m')

# Exiting function
def ext():
    msg(1,'Exiting...')
    sys.exit()


# Function used to open Firefox
def open_firefox():

    # Printing basic message
    msg(1,'Opening Firefox...')

    # Location the start button
    _start_button_=pyautogui.locateOnScreen('start_button.png')
    _location_=pyautogui.center(_start_button_)

    # Clicking the start button
    if not  pyautogui.click(_location_):
        msg(1,'Opened start menu successfully!')
    else:
        msg(3,'Failed to open start menu!')
        ext()

    time.sleep(2)

    # Search for Firefox in the menu search
    pyautogui.typewrite('firefox')
    pyautogui.typewrite('\n')
    
    # Print message
    msg(1,'Firefox is now open and running.')

def open_chrome_in_incognito():
    # Print basic message
    msg(1, 'Opening Chrome in incognito mode...')

    # Location the start button
    _start_button_ = pyautogui.locateOnScreen('start_button.png')
    _location_ = pyautogui.center(_start_button_)

    # Click the start button
    if not pyautogui.click(_location_):
        msg(1, 'Opened start menu successfully!')
    else:
        msg(3, 'Failed to open start menu!')
        ext()

    # Search for Chrome in the menu search
    pyautogui.typewrite('chrome')
    pyautogui.typewrite('\n')

    # Wait for Chrome to open
    time.sleep(2)

    # Open Chrome in incognito mode
    pyautogui.hotkey('ctrl', 'shift', 'n')

    # Wait for Chrome to open in incognito mode
    time.sleep(2)

    # Create a new incognito tab
    # pyautogui.hotkey('ctrl', 't')

    # Print message
    msg(1, 'Chrome is now open in incognito mode.')
    
# Function used to locate GMail
def locate_gmail():
    # Sleep for a while and wait for Firefox to open
    time.sleep(3)

    # Printing message
    msg(1,'Opening Gmail...')

    # Typing the website on the browser
    pyautogui.keyDown('ctrlleft')
    pyautogui.typewrite('a')
    pyautogui.keyUp('ctrlleft')
    pyautogui.typewrite('https://accounts.google.com/SignUp?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default')
    pyautogui.typewrite('\n')
    
    # Wait for a while until the website responds
    time.sleep(6)

    # Print a simple message
    msg(1,'Locating the form...')

    # Locate the form
    pyautogui.press('tab')
 
    time.sleep(2)

    _gmail_ = pyautogui.locateOnScreen('gmail_form.png')
    formx, formy = pyautogui.center(_gmail_)
    pyautogui.click(formx, formy)
    
    # Check and print message
    if not pyautogui.click(formx, formy):
        msg(1,'Located the form.')
    else:
        msg(3,'Failed to locate the form.')
        ext()

    # Fill out the form with random data
    firstname = 'Mark'
    lastname = 'Zuckerberg'
    username = firstname.lower() + lastname.lower() + str(random.randint(1, 10000))
    password = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for i in range(8))
    birth_month = str(random.randint(1, 12))
    birth_day = str(random.randint(1, 28))
    birth_year = str(random.randint(1970, 2003))
    gender = random.choice(['Male', 'Female'])
    
    # Fill out the form
    pyautogui.typewrite(firstname)
    pyautogui.press('tab')
    pyautogui.typewrite(lastname)
    pyautogui.press('tab')
    pyautogui.typewrite(username)
    pyautogui.press('tab')
    pyautogui.typewrite(password)
    pyautogui.press('tab')
    pyautogui.typewrite(password)
    pyautogui.press('tab')
    # pyautogui.typewrite(birth_month)
    # pyautogui.press('tab')
    # pyautogui.typewrite(birth_day)
    # pyautogui.press('tab')
    # pyautogui.typewrite(birth_year)
    # pyautogui.press('tab')
    pyautogui.press(gender[0])
    pyautogui.press('tab')
    pyautogui.press('enter')
    
    # Print a message
    msg(1,'Form filled successfully.')


# Function used to randomize credentials

# Main function
if __name__=='__main__':

    if open_chrome_in_incognito() :
        msg(3,'Failed to execute "open_firefox" command.')
        ext()

    if locate_gmail() :
        msg(3,'Failed to execute "locate_gmail" command.')
        ext()

    # if generate_info() :
        # msg(3,'Failed to execute "generate_info" command.')
        # ext()

    msg(1,'Done...')
    ext()
