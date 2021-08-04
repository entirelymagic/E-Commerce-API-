from django.urls import reverse
from faker import Faker
from rest_framework.test import APIClient, APITestCase

from .api_factories import CategoryFactory, UserFactory

# create a fake instance and client for testing
fake = Faker()
client = APIClient()
Faker.seed(0)


class CategoryTest(APITestCase):
    """Test category API endpoints
    Test will include:
        1. GET
        2. POST
        3. PUT
        4. DELETE
    """

    def setUp(self):
        """Create a user and a category for testing"""
        self.user = UserFactory()
        self.category = CategoryFactory()
        self.category_url = reverse('category-detail', kwargs={'pk': self.category.pk})
        self.category_data = {
            'name': fake.name(),
            'description': fake.text(),
            'user': self.user.id
        }
        self.category_data_update = {
            'name': fake.name(),
            'description': fake.text(),
            'user': self.user.id
        }

    def test_get_category(self):
        """Test GET request to category endpoint"""
        response = client.get(self.category_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.category.name)

    def test_post_category(self):
        """Test POST request to category endpoint"""
        response = client.post(reverse('category-list'), self.category_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], self.category_data['name'])

    def test_put_category(self):
        """Test PUT request to category endpoint"""
        response = client.put(self.category_url, self.category_data_update)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.category_data_update['name'])

    def test_delete_category(self):
        """Test DELETE request to category endpoint"""
        response = client.delete(self.category_url)
        self.assertEqual(response.status_code, 204)
