"""
Web Steps for BDD tests using Selenium
"""
import logging
from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions

logger = logging.getLogger("flask.app")

ID_PREFIX = "product_"


@when('I visit the "{page_name}"')
def step_impl(context, page_name):
    """Make a call to the base URL"""
    context.driver.get(context.base_url)
    logger.info("Visiting: %s", context.base_url)


@when('I set the "{element_name}" to "{text_string}"')
def step_impl(context, element_name, text_string):
    element_id = ID_PREFIX + element_name.lower().replace(" ", "_")
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, element_id))
    )
    element.clear()
    element.send_keys(text_string)


@when('I change "{element_name}" to "{text_string}"')
def step_impl(context, element_name, text_string):
    element_id = ID_PREFIX + element_name.lower().replace(" ", "_")
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, element_id))
    )
    element.clear()
    element.send_keys(text_string)


@when('I select "{text}" in the "{element_name}" dropdown')
def step_impl(context, text, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(" ", "_")
    element = Select(
        WebDriverWait(context.driver, context.wait_seconds).until(
            expected_conditions.presence_of_element_located((By.ID, element_id))
        )
    )
    element.select_by_visible_text(text)


@when('I press the "{button}" button')
def step_impl(context, button):
    """Press a button on the page"""
    element_id = button.lower().replace(" ", "_")
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.element_to_be_clickable(
            (By.ID, element_id)
        )
    )
    element.click()


@when('I copy the "{element_name}" field')
def step_impl(context, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(" ", "_")
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, element_id))
    )
    context.clipboard = element.get_attribute("value")
    logger.info("Clipboard contains: %s", context.clipboard)


@when('I paste the "{element_name}" field')
def step_impl(context, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(" ", "_")
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, element_id))
    )
    element.clear()
    element.send_keys(context.clipboard)


@then('I should see the message "{message}"')
def step_impl(context, message):
    """Verify a flash message is displayed"""
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.text_to_be_present_in_element(
            (By.ID, "flash_message"),
            message
        )
    )
    expect(found).to_be(True)


@then('I should see "{name}" in the results')
def step_impl(context, name):
    """Check that a product name appears in the search results"""
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.text_to_be_present_in_element(
            (By.ID, "search_results"),
            name
        )
    )
    expect(found).to_be(True)


@then('I should not see "{name}" in the results')
def step_impl(context, name):
    """Check that a product name does NOT appear in the search results"""
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located(
            (By.ID, "search_results")
        )
    )
    assert name not in element.text, \
        f"Expected '{name}' NOT to be in results but it was found"


@then('I should see "{text_string}" in the "{element_name}" field')
def step_impl(context, text_string, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(" ", "_")
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.text_to_be_present_in_element_value(
            (By.ID, element_id),
            text_string
        )
    )
    expect(found).to_be(True)


@then('the "{element_name}" field should be empty')
def step_impl(context, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(" ", "_")
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, element_id))
    )
    assert element.get_attribute("value") == ""


@then('I should see "{text_string}" in the title')
def step_impl(context, text_string):
    """Check the document title for a text string"""
    WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.title_contains(text_string)
    )


def expect(condition):
    """Helper class for assertions"""
    class Expect:
        def __init__(self, val):
            self.val = val
        def to_be(self, expected):
            assert self.val == expected, f"Expected {expected} but got {self.val}"
    return Expect(condition)
