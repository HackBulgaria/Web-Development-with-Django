import tempfile
from PIL import Image
from django.urls import reverse
from django.test import TestCase, Client
from .factories import CategoryFactory, UserFactory, OfferFactory
from .models import Offer
from faker import Factory

faker = Factory.create()


# Create your tests here.
class IndexViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('website:index')

    def test_list_all_offers(self):
        self.user = UserFactory()
        self.category = CategoryFactory()
        self.offer1 = OfferFactory(category=self.category, author=self.user)
        self.offer2 = OfferFactory(category=self.category, author=self.user)

        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, response.context['offers'].count())


class AddOfferTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = CategoryFactory()
        self.user = UserFactory()

    def test_cannot_create_offer_if_user_is_not_logged(self):
        data = {
            'title': faker.word(),
            'description': faker.text(),
            'category': self.category,
        }

        url = reverse('website:add-offer')
        response = self.client.post(url, data=data)
        self.assertEqual(302, response.status_code)

    def test_cannot_create_offer_with_invalid_data(self):
        self.assertEqual(0, Offer.objects.count())

        data = {
            'title': faker.word(),
            'description': faker.text(),
            'category': self.category,
        }

        url = reverse('website:add-offer')

        self.client.login(username=self.user.username, password='Ivoepanda', follow=True)
        response = self.client.post(url, data=data)
        self.assertEqual(302, response.status_code)
        self.assertEqual(0, Offer.objects.count())

    def test_can_create_offer_if_user_is_logged(self):
        self.assertEqual(0, Offer.objects.count())

        image = Image.new('RGB', (100, 100), color='green')
        tmp_file = tempfile.NamedTemporaryFile(suffix='.png')
        image.save(tmp_file.name)

        data = {
            'title': faker.word(),
            'description': faker.text(),
            'category': self.category.id,
            'image': tmp_file,
        }

        url = reverse('website:add-offer')

        logged = self.client.force_login(self.user)
        response = self.client.post(url, data=data)
        self.assertEqual(302, response.status_code)
        self.assertEqual(1, Offer.objects.count())

    def tearDown(self):
        self.client.logout()


class EditOfferViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = CategoryFactory()
        self.user = UserFactory()
        self.offer = OfferFactory(category=self.category, author=self.user)

    def test_cannot_edit_offer_if_user_is_not_logged(self):
        data = {
            'title': faker.word(),
        }

        url = reverse('website:edit-offer', kwargs={'pk': self.offer.id})
        response = self.client.post(url, data=data)
        self.assertEqual(302, response.status_code)
        self.assertNotEqual(data['title'], self.offer.title)
