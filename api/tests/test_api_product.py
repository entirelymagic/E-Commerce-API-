from django.urls import reverse
from faker import Faker
from rest_framework.test import APIClient, APITestCase

from .api_factories import ProductFactory, CategoryFactory

fake = Faker()
client = APIClient()
Faker.seed(0)


class ProductTest(APITestCase):
    def setUp(self):
        self.product = ProductFactory.create()
        self.category = CategoryFactory.create()

    def test_create_product(self):
        url = reverse('product-list')
        data = {
            'name': fake.name(),
            'description': fake.text(),
            'price': fake.pyint(),
            'stock': fake.pyint(),
            'is_active': fake.pybool(),
            'category': self.category.id,
        }
        response = client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['description'], data['description'])
        self.assertEqual(response.data['price'], str(data['price']))
        self.assertEqual(response.data['stock'], data['stock'])

    def test_list_products(self):
        url = reverse('product-list')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], self.product.name)
        self.assertEqual(response.data[0]['description'], self.product.description)

    def test_retrieve_product(self):
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.product.name)
        self.assertEqual(response.data['description'], self.product.description)

    def test_update_product(self):
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        data = {
            'name': fake.name(),
            'description': fake.text(),
            'price': fake.pyint(),
        }
        response = client.put(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['description'], data['description'])

    def test_delete_product(self):
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        response = client.delete(url)
        self.assertEqual(response.status_code, 204)
