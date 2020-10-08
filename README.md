# PythonSelenium
A short code to show how you can use Selenium in Python to automate web browsing

1) Start by downloading the Anaconda Python environment: https://www.anaconda.com/products/individual. This will install the Anaconda prompt, a terminal application, and Spyder, a python coding studio.

2) Open Anaconda Prompt and type "pip install selenium". This will install the selenium library on your computer.

3) Download and install the driver for the browser you like to use. Save it to your PATH, e. g., place it in /usr/bin or /usr/local/bin.:

Chrome: 	https://sites.google.com/a/chromium.org/chromedriver/downloads

Edge: 	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Firefox: 	https://github.com/mozilla/geckodriver/releases

Safari: 	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

4) Copy this code into Spyder and try running it

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://www.python.org")

elem = driver.find_element_by_name("q")

elem.clear()

elem.send_keys("pycon")

elem.send_keys(Keys.RETURN)

#driver.close()

5) The hardest part is finding elements on a website. These offer helpful suggestions:

https://selenium-python.readthedocs.io/locating-elements.html

https://www.selenium.dev/documentation/en/getting_started_with_webdriver/locating_elements/

https://ddavison.io/css/2014/02/18/effective-css-selectors.html



