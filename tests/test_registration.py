from base.base_test import BaseTest


class TestRegistration(BaseTest):

    def test_registration_success(self):

        # Переходим на страницу регистрации
        self.registration_page.get_url(self.registration_page.PAGE_URL)

        # Заполняем форму
        self.registration_page.fill_username("testuser")
        self.registration_page.fill_email("testuser@example.com")
        self.registration_page.fill_password("TestPassword123")
        self.registration_page.fill_confirm_password("TestPassword123")

        # Отправляем форму
        self.registration_page.submit_registration()

        # Проверяем, что регистрация успешна
        success_message = self.registration_page.get_success_message()
        assert "Регистрация прошла успешно" in success_message, "Регистрация не прошла успешно"

        # Проверяем, что появилось сообщение о подтверждении email
        email_confirmation_message = self.registration_page.get_email_confirmation_message()
        assert "Код для подтверждения" in email_confirmation_message, "Сообщение о подтверждении email не отображается"
