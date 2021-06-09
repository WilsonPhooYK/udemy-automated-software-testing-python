from tests.acceptance.locators.base_page import BasePageLocators
from typing import Any


class BasePage:
    def __init__(self, driver: Any) -> None:
        self.driver = driver
        
    @property
    def url(self) -> str:
        return 'http://127.0.0.1:5000'
    
    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)
    
    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)
    