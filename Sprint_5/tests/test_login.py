from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
import helpers
import data
from locators import TestLocators
from urls import BaseURL


class TestLogin:
    def test_login_in_homepage_success(self, driver):
        driver.get(BaseURL)
        driver.find_element(TestLocators.ACCOUNT_LOGIN_BUTTON_ON_THE_MAIN_FORM).click()
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
        WebDriverWait(driver, 10).until(
            visibility_of_element_located(TestLocators.ORDER_PLACE_BUTTON)
        )
        assert len(driver.find_elements(TestLocators.ORDER_PLACE_BUTTON)) == 1

    def test_login_in_personal_account_success(self, driver):
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
        assert len(driver.find_elements(TestLocators.ORDER_PLACE_BUTTON)) == 1

    def test_login_in_registration_form_success(self, driver):
        driver.get(BaseURL)
        driver.find_element(TestLocators.ACCOUNT_LOGIN_BUTTON_ON_THE_MAIN_FORM).click()
        driver.find_element(TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 10).until(
            visibility_of_element_located(TestLocators.LOGIN_BUTTON)
        )
        driver.find_element(TestLocators.TEXT_LOGIN_BUTTON).click()
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
        assert len(driver.find_elements(TestLocators.ORDER_PLACE_BUTTON)) == 1

    def test_login_in_password_recovery_form_success(self, driver):
        driver.get(BaseURL)
        driver.find_element(TestLocators.LOGIN_BUTTON).click()
        driver.find_element(TestLocators.RECOVERY_BUTTON).click()
        WebDriverWait(driver, 5).until(
            visibility_of_element_located(TestLocators.LOGIN_BUTTON)
        )
        driver.find_element(TestLocators.TEXT_LOGIN_BUTTON).click()
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
        assert len(driver.find_elements(TestLocators.ORDER_PLACE_BUTTON)) == 1
