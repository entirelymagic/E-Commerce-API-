from django.urls import reverse
from faker import Faker

from rest_framework.test import APIClient, APITestCase
from .api_factories import UserFactory


fake = Faker()
client = APIClient()
Faker.seed(0)

class UserActionsTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
    
    def test_user_login(self):
        url = reverse('login')
        data = {
            'username': self.user.username,
            'password': self.user.password
        }
        pass
    
    def test_user_logout(self):
        pass
    
    