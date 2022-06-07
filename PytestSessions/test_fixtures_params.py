from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.params == "chrome":
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if request.params == "firefox":
        web_driver = web_driver.Firefox(service=Service(GeckoDriverManager().install()))
    request.cls.driver = web_driver
    yield
    web_driver.close()


class BaseTest:
    pass


class Test_Google(BaseTest):
    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"
