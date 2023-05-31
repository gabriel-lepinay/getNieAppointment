##
## Gabriel Lepinay, 2023
## getNieAppointment
## File description:
## main
##
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

def loadingDrivers():
    print("Loading drivers...", end=" ")
    try:
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    except Exception as e:
        print("Failed.\n", e)
        return None
    print("Success.")
    return driver

# Navigate to the website
def openWebsite(driver, url):
    print("Opening website...", end=" ")
    try:
        driver.get(url)
    except Exception as e:
        print("Failed.\n", e)
        return False
    print("Success.")
    return True

def main(args):
    driver = loadingDrivers()
    if driver == None:
        sys.exit(84)
    if openWebsite(driver, "https://webinpact.com/ip-address/") == False:
        sys.exit(84)

    ip = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div/div/div/span")
    print(ip.text)
    driver.close()

if __name__ == "__main__":
    main(sys.argv)