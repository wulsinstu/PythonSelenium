# 1. Import Libraries------------------------------------------------------------------------

import time as t
import os
from selenium import webdriver

# 2. Setting Variables ------------------------------------------------------------------------------

canvas_password = os.getenv('Canvas_Password')
ACTIVE_COURSES = {1035, 35, 31}
length = len(ACTIVE_COURSES)

# 3. Log in to Canvas ------------------------------------------------------------------------------------------------
print('starting driver')
driver = webdriver.Firefox()    # This is the Selenium Driver that will operate my browser for me
t.sleep(2)

print('opening window')
driver.get('https://elhaynes.instructure.com/login/canvas') # driver.get navigates to a website
t.sleep(2)

login=driver.find_element_by_id('pseudonym_session_unique_id')  # driver.find... identifies an element on the website
login.send_keys("swulsin@elhaynes.org") # driver.send_keys types into a field in the website
t.sleep(2)

pw=driver.find_element_by_id('pseudonym_session_password')
pw.send_keys(canvas_password)
t.sleep(2)

print('logging in')
LogInButton=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[2]/form[1]/div[3]/div[2]/button')
LogInButton.click() # driver.click() clicks a button in the website
t.sleep(2)

# 4. Functions ------------------------------------------------------------------------------------------------
             
def sync_to_sis(course_id):
    
    url = 'https://elhaynes.instructure.com/courses/{}/external_tools/18?display=borderless&amp;launch_type=post_grades'.format(course_id)
    driver.get(url)

    t.sleep(5)

    PostGrades = driver.find_element_by_xpath('//*[contains(@class,"fOyUs_bGBk fOyUs_fKyb")]')

    print('Clicking Post Grades for ' + str(course_id))
   #PostGrades.click()

    t.sleep(2)

def sync_all_courses():
    print('Syncing All Courses')
    count = 1  

    for course in ACTIVE_COURSES:
        sync_to_sis(course)
        print(str(count) + ' of ' + str(length) + ' course: ' + str(course))
        count += 1 
    
# Main Program ------------------------------------------------------------------------------------------

sync_all_courses()

t.sleep(5)
print('closing driver')
driver.quit()   # Closes the browser window
