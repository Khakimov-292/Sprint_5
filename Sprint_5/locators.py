from selenium.webdriver.common.by import By

class TestLocators:
    EMAIL_FIELD = (By.XPATH, '//label[text()="Email"]/input[@class="text input__textfield text_type_main-default"]')  #Поле для ввода email
    NAME_FIELD = (By.XPATH, '//label[text()="Имя"]/input[@class="text input__textfield text_type_main-default"]')  #Поле для ввода имени
    PASSWORD_FIELD = (By.XPATH, '//label[text()="Пароль"]/input[@class="text input__textfield text_type_main-default"]')  #Поле для ввода пароля
    LOGIN_BUTTON = (By.CLASS_NAME, 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa')  #Кнопка Вход
    ACCOUNT_LOGIN_BUTTON_ON_THE_MAIN_FORM = (By.XPATH, '//button[text()="Войти в аккаунт"]')  #Кнопка Войти в аккаунт
    ORDER_PLACE_BUTTON = (By.XPATH, '//div[@class="BurgerConstructor_basket__totalContainer__2Z-ho mr-10"]/button[text()="Оформить заказ"]')  #Кнопка Оформить заказ
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')  # Кнопка Личный Кабинет
    REGISTRATION_BUTTON = (By.XPATH, '//a[text()= "Зарегистрироваться"]')  #Гиперссылка Зарегистрироваться
    TEXT_LOGIN_BUTTON = (By.CLASS_NAME, 'Auth_link__1fOlj')  #Гиперссылка Вход
    TEXT_REGISTRATION_BUTTON = (By.XPATH, '//p[@class="undefined text text_type_main-default text_color_inactive mb-4"]/a[text()="Зарегистрироваться"]')  #Гиперссылка Зарегистрироваться
    RECOVERY_BUTTON = (By.XPATH, '//a[text()= "Восстановить пароль"]')  #Кнопка Восстановить пароль
    DESIGNER_BUTTON = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX"]/p[text()="Конструктор"]')  #Кнопка Конструктор
    BREAD_BUTTON = (By.XPATH, '//div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]/h2[text="Булки"]')  #Раздел булки
    EXIT_BUTTON = (By.XPATH, '//button[text()="Выход"]')  #Кнопка Выход в личном кабинете
    LOGO = (By.XPATH, '//a[@href="/"]')  #Логотип
    CONSTRUCTOR_HEADER = (By.XPATH, '//h1[@class = "text text_type_main-large mb-5 mt-10"]')  #Заголовок конструктора
    ERROR_TEXT = (By.CLASS_NAME, 'input__error text_type_main-default')  #Текст ошибки
    SAUCE = (By.XPATH, '//p[text()="Соус фирменный Space Sauce"]')  #Соус
    BREAD = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')  #Булка
    FILLING = (By.XPATH, '//p[text()="Филе Люминесцентного тетраодонтимформа"]')  #Начинка
    HEADER_BUTTON_BREADS = (By.XPATH, '//span[text()="Булки"]') #Заголовок раздела Булки
    HEADER_BUTTON_SAUCES = (By.XPATH, '//span[text()="Соусы"]') #Заголовок раздела Соусы
    HEADER_BUTTON_FILLINGS = (By.XPATH, '//span[text()="Начинки"]') #Заголовок раздела Начинки
    CONDITION_SAUCES = (By.XPATH, '//div[contains(@class="tab_tab__1SPyG") and span[text()="Соусы"]]')  #Раздел с соусом
    CONDITION_BREADS = (By.XPATH, '//div[contains(@class="tab_tab__1SPyG") and span[text()="Булки"]]')  #Раздел с булкой
    CONDITION_FILLINGS = (By.XPATH, '//div[contains(@class="tab_tab__1SPyG") and span[text()="Начинки"]]')  #Раздел с начинкой



