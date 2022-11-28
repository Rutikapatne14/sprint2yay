#cross browsing and preconditions
import pytest
from selenium import webdriver
from library.config import Config



@pytest.fixture(params=["Chrome","Edge"])
def _driver(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome(executable_path=Config.ChromeDriver)

    elif request.param == "Edge":
        driver = webdriver.Edge(Config.EdgeDriver)

    driver.get(Config.url)
    driver.maximize_window()

    yield driver
    print(driver.title)
    #driver.save_screenshot("text_demowebshop.png")
    driver.close()






