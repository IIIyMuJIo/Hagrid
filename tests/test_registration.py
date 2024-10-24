from selenium import webdriver
from pages.registration_page import RegistrationPage


class TestRegistration():

    def setUp(self):
        # Инициализация драйвера (Chrome)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_registration_success(self):
        # Создаем объект RegistrationPage
        registration_page = RegistrationPage(self.driver)

        # Переходим на страницу регистрации
        registration_page.get_url("https://example.com/register")

        # Заполняем форму
        registration_page.fill_username("testuser")
        registration_page.fill_email("testuser@example.com")
        registration_page.fill_password("TestPassword123")
        registration_page.fill_confirm_password("TestPassword123")

        # Отправляем форму
        registration_page.submit_registration()

        # Проверяем, что регистрация успешна
        success_message = registration_page.get_success_message()
        self.assertIn("Регистрация прошла успешно", success_message)

        # Проверяем, что появилось сообщение о подтверждении email
        email_confirmation_message = registration_page.get_email_confirmation_message()
        self.assertIn("Подтвердите ваш email", email_confirmation_message)

    def tearDown(self):
        # Закрываем браузер после теста
        self.driver.quit()
