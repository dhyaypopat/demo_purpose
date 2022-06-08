import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestHubspot(BaseTest):

    @pytest.mark.parametrize(
        "username", "password",
        [
            ("admin@gmail.com", "admin123"),
            ("dhyay@yopmail.com", "dhyay123"),
        ]
    )
    def test_login(self, username, password):
        self.driver.get("https://app.hubspot.com/login")
        self.driver.findelement(By.ID, "username").send_keys(username)
        time.sleep(3)
        self.driver.findelement(By.ID, "password").send_keys(password)
        time.sleep(3)
