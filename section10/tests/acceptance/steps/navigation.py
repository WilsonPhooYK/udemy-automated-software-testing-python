from typing import Any
from behave import *
from selenium import webdriver
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.new_post_page import NewPostPage

# Allows steps to receve arguments from scenarios
use_step_matcher('re')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

@given('I am on the homepage')
def step_impl(context: Any):
    context.driver = webdriver.Chrome('chromedriver', options=options)
    page = HomePage(context.driver)
    context.driver.get(page.url)
    
@given('I am on the blog page')
def step_impl(context: Any):
    context.driver = webdriver.Chrome('chromedriver', options=options)
    page = BlogPage(context.driver)
    context.driver.get(page.url)
    
@given('I am on the new post page')
def step_impl(context: Any):
    context.driver = webdriver.Chrome('chromedriver', options=options)
    page = NewPostPage(context.driver)
    context.driver.get(page.url)
    
    
@then('I am on blog page')
def step_impl(context: Any):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url
    
@then('I am on the homepage')
def step_impl(context: Any):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url