from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from urls import BaseURL


class TestSectionConstructor:
    def test_seach_section_sauces_success(self, driver):
        driver.get(BaseURL)
        driver.find_element(TestLocators.HEADER_BUTTON_SAUCES).click()
        WebDriverWait(driver, 5).until(
            visibility_of_element_located(TestLocators.CONDITION_SAUCES)
        )
        assert (
            driver.find_element(TestLocators.SAUCE).text == "Соус фирменный Space Sauce"
        )

    def test_seach_section_buns_success(self, driver):
        driver.get(BaseURL)
        driver.find_element(TestLocators.HEADER_BUTTON_BREADS).click()
        WebDriverWait(driver, 5).until(
            visibility_of_element_located(TestLocators.CONDITION_BREADS)
        )
        assert (
            driver.find_element(TestLocators.BREAD).text == "Флюоресцентная булка R2-D3"
        )

    def test_seach_section_fillings_success(self, driver):
        driver.get(BaseURL)
        driver.find_element(TestLocators.HEADER_BUTTON_FILLINGS).click()
        WebDriverWait(driver, 5).until(
            visibility_of_element_located(TestLocators.CONDITION_FILLINGS)
        )
        assert (
            driver.find_element(TestLocators.FILLING).text == "Филе Люминесцентного тетраодонтимформа"
        )
