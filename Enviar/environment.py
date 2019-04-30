from Pyautomators.contrib.scenario_autoretry import scenario_retry
from selenium import webdriver
import time
from pages.pages.home import Home

def before_all(context):
	context.driver=webdriver.Chrome('driver/chromedriver.exe')
	context.home=Home(context.driver)

def after_all(context):
	context.driver.quit()


