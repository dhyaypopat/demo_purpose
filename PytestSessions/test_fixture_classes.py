from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.fixture(scope='class')
def init_firefox_driver(request):
    firefox_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    request.cls.driver = firefox_driver
    yield
    firefox_driver.close()


@pytest.mark.usefixtures("init_chrome_driver")
class Base_Chrome_Test:
    pass


class Test_Google_Chrome(Base_Chrome_Test):

    def test_google_title_chrome(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"


@pytest.mark.usefixtures("init_firefox_driver")
class Base_Firefox_Test:
    pass


class Test_Google_Firefox(Base_Firefox_Test):

    def test_google_title_firefox(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"
