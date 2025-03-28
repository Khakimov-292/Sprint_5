from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located,
    element_to_be_clickable,
)
from selenium.webdriver.support.wait import WebDriverWait
import helpers
import data
from locators import TestLocators
from urls import BaseURL, ProfileURL


class TestPersonalAccount:
    def test_first_login_to_personal_account_success(self, driver):
        driver.get(BaseURL)
        driver.find_element(TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            visibility_of_element_located(TestLocators.EMAIL_FIELD)
        )
        driver.find_element(TestLocators.EMAIL_FIELD).send_keys(
            helpers.DateToTest.generation_email(
                data.name,
                data.surname,
                data.number_kogort,
                data.domain,
            )
        )
        driver.find_element(TestLocators.PASSWORD_FIELD).send_keys("qwerty")
        driver.find_element(TestLocators.LOGIN_BUTTON).click()
        driver.find_element(TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        assert driver.current_url == ProfileURL

    def test_go_to_constructor_success(self, driver):
        driver.get(ProfileURL)
        WebDriverWait(driver, 10).until(
            element_to_be_clickable(TestLocators.DESIGNER_BUTTON)
        )
        driver.find_element(TestLocators.DESIGNER_BUTTON).click()
        WebDriverWait(driver, 10).until(
            element_to_be_clickable(TestLocators.LOGO)
        ).click()
        constructor_indicator = driver.find_element(TestLocators.CONSTRUCTOR_HEADER)
        assert constructor_indicator.text == "Соберите бургер"

    def test_logout_success(self, driver):
        driver.get(ProfileURL)
        WebDriverWait(driver, 10).until(
            element_to_be_clickable(TestLocators.EXIT_BUTTON)
        )
        driver.find_element(TestLocators.EXIT_BUTTON)
        login_button = driver.find_element(TestLocators.LOGIN_BUTTON)
        assert login_button.text == "Войти"
