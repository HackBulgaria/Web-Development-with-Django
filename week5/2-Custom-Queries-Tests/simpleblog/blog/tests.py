from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .factories import TagFactory, BlogPostFactory
from .models import BlogPost
from faker import Factory

faker = Factory.create()

# Create your tests here.
class CreateBlogPostTests(TestCase):

    def setUp(self):
        self.tag = TagFactory()
        self.tag2 = TagFactory()
        self.blog_post = BlogPostFactory(tags=[self.tag, self.tag2])
        self.client = Client()
        self.user = User.objects.create_user(username=faker.name(), password='Ivoepanda')

    def test_get_method(self):
        response = self.client.get('/create/')
        self.assertEqual(302, response.status_code)

    def test_post_method_if_not_logged(self):
        self.assertEqual(1, BlogPost.objects.count())
        url = reverse('blog:create')
        response = self.client.post(url, data={"title": faker.name(), "content": faker.text()})

        self.assertEqual(302, response.status_code)
        self.assertEqual(1, BlogPost.objects.count())

    def test_post_with_logged_user(self):
        self.assertEqual(1, BlogPost.objects.count())
        self.client.login(username=self.user.username, password="Ivoepanda")
        url = reverse('blog:create')
        response = self.client.post(url, data={"title": faker.name(), "content": faker.text()})
        self.assertEqual(302, response.status_code)
        self.assertEqual(2, BlogPost.objects.count())

    def tearDown(self):
        self.client.logout()
