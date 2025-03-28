from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
import helpers
import data
from locators import TestLocators
from urls import BaseURL, LoginURL


class TestRegistration:
    def test_registration_in_button_success(self, driver):
        driver.get(BaseURL)
        driver.find_element(TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            visibility_of_element_located(TestLocators.EMAIL_FIELD)
        )
        driver.find_element(TestLocators.TEXT_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            visibility_of_element_located(TestLocators.EMAIL_FIELD)
        )
        driver.find_element(TestLocators.NAME_FIELD).send_keys(data.name)
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
        assert driver.current_url == LoginURL

    def test_registration_with_incorrect_password(self, driver):
        driver.get(BaseURL)
        driver.find_element(TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            visibility_of_element_located(TestLocators.EMAIL_FIELD)
        )
        driver.find_element(TestLocators.TEXT_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            visibility_of_element_located(TestLocators.EMAIL_FIELD)
        )
        driver.find_element(TestLocators.NAME_FIELD).send_keys(data.name)
        driver.find_element(TestLocators.EMAIL_FIELD).send_keys(
            helpers.DateToTest.generation_email(
                data.name,
                data.surname,
                data.number_kogort,
                data.domain,
            )
        )
        driver.find_element(TestLocators.PASSWORD_FIELD).send_keys("qwe")
        driver.find_element(TestLocators.LOGIN_BUTTON).click()
        error_text = driver.find_element(TestLocators.ERROR_TEXT)
        assert error_text.text == "Некорректный пароль"
