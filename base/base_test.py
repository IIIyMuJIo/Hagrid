import pytest
from base.base_page import BasePage
from pages.registration_page import RegistrationPage


class BaseTest:

    base_page: BasePage
    registration_page: RegistrationPage

    #Fixture
    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver

        request.cls.base_page = BasePage(driver)
        request.cls.registration_page = RegistrationPage(driver)
