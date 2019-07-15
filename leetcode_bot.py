from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
from datetime import timedelta
from datetime import datetime
import time

'''
This python program is a bot that automatically signs you up for leetcode weekly contest.
To make this work, in additionally to the code here, you will need 3 more components.

(1) You need a task scheduler that would execute this program at a time of your choosing.
    For example, cron daemon on Linux. Personally, I set the program to run at 1PM on Wednesday.
    It won't work if leetcode hasn't posted the new contest up yet.

(2) You need to install the driver program that Selenium API can interact with.
    Personally, I prefer Google Chrome, so I installed Chromedriver, which this Python code will call.

(3) You need to install selenium. Just pip install selenium.

Note: If leetcode makes changes to its web html source code, you will have to adjust this code accordingly.
'''

# LeetCode credentials
username = '--- Enter your leetcode username ---'
password = '--- Enter your leetcode password ---'

# variables
driver_path = '--- Enter path for your chromedriver ---'

# ------------------------------------------------------------------------------
# open driver
driver = webdriver.Chrome(driver_path)
# maximize window
driver.maximize_window()
# go to LeetCode
driver.get('https://www.leetcode.com')

# locate sign in button
sign_in = driver.find_element_by_link_text('Sign in')
sign_in.click()
# enter username
username_field = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'username-input'))
)
username_field.send_keys(username)
# enter password
password_field = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'password-input'))
)
password_field.send_keys(password + '\n')
time.sleep(3)

# ------------------------------------------------------------------------------
# locate contest page
contest_url = 'https://leetcode.com/contest/weekly-contest-'
alpha_contest = 141

# calculate how many weeks have passed since the alpha date
alpha = datetime(2019, 6, 12).date()
today = date.today()
alpha_adjusted = alpha - timedelta(days = alpha.weekday())
today_adjusted = today - timedelta(days = today.weekday())
weeks_elapsed = int((today_adjusted - alpha_adjusted).days / 7)

# find out current weekly contest number and concat onto the contest_url
contest_number = alpha_contest + weeks_elapsed
contest_url += str(contest_number)

# go to this week's contest page
driver.get(contest_url)

# ------------------------------------------------------------------------------
# locate register button and click
register = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, './/*[@id="contest-app"]/div/div/div[3]/span/a'))
)
register.click()
# locate confirmation button and click
confirm = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[@class="swal2-container swal2-center swal2-fade swal2-shown"]/div/div[10]/button[1]'))
)
confirm.click()

# close program
time.sleep(5)
driver.close()
time.sleep(5)
