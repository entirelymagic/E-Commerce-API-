from django.urls import reverse
from faker import Faker

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .random_generator import random_string_generator
from .api_factories import ProductFactory, CategoryFactory, OrderFactory, UserFactory

fake = Faker()
client = APIClient()
Faker.seed(0)


class OrderTest(APITestCase):
    """
    Test for Order api endpoints.
    """

    def setUp(self):
        self.user = UserFactory()
        self.category = CategoryFactory()
        self.produc1 = ProductFactory()
        self.produc2 = ProductFactory()
        self.produc3 = ProductFactory()
        self.order = OrderFactory()

    def test_get_all_orders(self):
        """
        Test to get all orders.
        """
        url = reverse('order-list')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_one_order(self):
        """
        Test to get one order.
        """
        url = reverse('order-detail', kwargs={'pk': self.order.id})
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_order(self):
        """
        Test to create order.
        """
        url = reverse('order-list')
        data = {
            'user': self.user.pk,
            'product_names': self.produc1.name + ' ' +  self.produc2.name,
            'total_products': 2,
            'total_amount': self.produc1.price + self.produc2.price,
            'transaction_id': random_string_generator(size=6)
            
        }
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_order(self):
        """
        Test to update order.
        """
        url = reverse('order-detail', kwargs={'pk': self.order.id})
        data = {
            'user': self.user.pk,
            'product_names': self.produc1.name + ' ' +  self.produc3.name,
            'total_products': 2,
            'total_amount': self.produc1.price + self.produc2.price,
            'transaction_id': random_string_generator(size=10)
        }
        response = client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['product_names'], data['product_names'])
        self.assertEqual(response.data['total_products'], data['total_products'])
        self.assertEqual(response.data['total_amount'], data['total_amount'])
        self.assertEqual(response.data['transaction_id'], data['transaction_id'])
        

    def test_delete_order(self):
        """
        Test to delete order.
        """
        url = reverse('order-detail', kwargs={'pk': self.order.id})
        response = client.delete(url)