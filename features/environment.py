"""
Environment for Behave Testing
"""
import os
from selenium import webdriver

WAIT_SECONDS = int(os.getenv("WAIT_SECONDS", "60"))
BASE_URL = os.getenv("BASE_URL", "http://localhost:8080")


def before_all(context):
    """Executed once before all tests"""
    context.base_url = BASE_URL
    context.wait_seconds = WAIT_SECONDS
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(context.wait_seconds)


def after_all(context):
    """Executed once after all tests"""
    context.driver.quit()
