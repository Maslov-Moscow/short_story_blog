from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from ..models import Post


class PostPagesTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='test')
        Post.objects.create(author=self.user, text='Test text 123')
        client = Client().force_login(self.user)

    def test_template(self):
        response = self.client.get("/posts/1/")
        self.assertTemplateUsed(response, 'posts/post_detail.html')

    def test_context(self):
        response = self.client.get("/posts/1/")
        self.assertEqual(response.context['object'].text, "Test text 123")
