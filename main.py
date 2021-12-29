# This is a sample Python script.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chromedriver_location = "/Desktop/chromedriver.exe"
url = 'https://maconburgerweek.com/'
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
xpath = "//*[@id='QID1-4-label']" #//*[@id='QID1']/div[3]/div/fieldset/div/table/tbody/tr[4]/td[2]"
survey = "https://qfreeaccountssjc1.az1.qualtrics.com/jfe/form/SV_9NCaIVbgWF3MRtI"

def print_hi():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(survey)
    time.sleep(.5)
    webElement = driver.find_element(By.XPATH, xpath);
    webElement.click()
    time.sleep(.7)
    webElement = driver.find_element(By.XPATH, "//*[@id='NextButton']");
    webElement.click()
    time.sleep(.7)
    webElement = driver.find_element(By.XPATH, "//*[@id='NextButton']");
    webElement.click()
    time.sleep(.7)
    driver.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for x in range(0,100):
        print_hi()
        print(x)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
