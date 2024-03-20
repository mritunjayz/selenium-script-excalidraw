# -*- coding: utf-8 -*-
import time
import psutil
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Function to draw on canvas
def draw_on_canvas(driver):
    canvas = driver.find_element_by_id("canvas")

    actions = ActionChains(driver)
    actions.move_to_element(canvas).move_by_offset(50, 50).click_and_hold().move_by_offset(100, 0).release().perform()
    actions.move_to_element(canvas).move_by_offset(50, 50).click_and_hold().move_by_offset(0, 100).release().perform()

def draw_ellipse_on_canvas(driver):
    ellipse_tool = driver.find_element_by_css_selector('[title="Ellipse — O or 4"]')
    ellipse_tool.click()

    canvas = driver.find_element_by_css_selector('.excalidraw__canvas.interactive')

    actions = ActionChains(driver)
    actions.move_to_element(canvas).click_and_hold().move_by_offset(400, 400).release().perform()

# Function to get CPU usage
def get_cpu_usage():
    return psutil.cpu_percent()

# Set up Selenium WebDriver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("https://excalidraw.com")  # Replace with your website URL containing the canvas element

# Perform drawing on canvas while monitoring CPU usage
try:
    for i in range(10):  # Draw 10 times as an example
        draw_ellipse_on_canvas(driver)
        cpu_usage = get_cpu_usage()
        print("CPU Usage:", cpu_usage)
        time.sleep(1)  # Add a delay to space out drawing actions
finally:
    driver.quit()
