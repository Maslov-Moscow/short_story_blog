from django.test import TestCase
from django.test import TestCase, Client
from django.contrib.auth import get_user_model


class StaticURLTests(TestCase):
    """Проверка доступности статических страниц """

    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200, 'Главная страница не доступна')

    def test_about(self):
        response = self.client.get('/about/author/')
        self.assertEqual(response.status_code, 200, 'Страница автор не доступна')

    def test_tech(self):
        response = self.client.get('/about/tech/')
        self.assertEqual(response.status_code, 200, 'Страница технологии не доступна')


class AuthTest(TestCase):
    """Проверка авторизации """
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='test', password='12test12', email='test@test.com')
        self.client = Client()

    def test_login(self):
        response = self.client.login(username='test', password='12test12')
        self.assertEqual(response, True, 'Ошибка авторизации ')

    def test_login_wrong(self):
        response = self.client.login(username='test', password='12te213t12')
        self.assertEqual(response, False, 'Ошибка проверки пароля')


class LoginRequaredTest(TestCase):
    """Проверка доступа неавторизованных пользователей """
    def setUp(self):
        self.client = Client()

    def test_create_post(self):
        response = self.client.get("/post/new")
        self.assertRedirects(response, "/auth/login/?next=/post/new",
                             msg_prefix="Неавторизованный пользователь не перенаправляется на страницу авторизации"
                             )
