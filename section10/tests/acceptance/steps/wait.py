from typing import Any
from behave import *

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.acceptance.locators.blog_page import BlogPageLocators

use_step_matcher('re')

@given('I wait for the posts to load')
def step_impl(context: Any):
    try:
        WebDriverWait(context.driver, 5).until(
            expected_conditions.visibility_of_any_elements_located(BlogPageLocators.POSTS_SECTION)
        )
    except Exception as e:
        raise e
    