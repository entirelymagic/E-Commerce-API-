import factory
import pytz
from api.category.models import Category
from api.order.models import Order
from api.product.models import Product
from api.user.models import CustomUser
from faker import Factory, Faker

from .random_generator import random_string_generator

faker = Factory.create()
Faker.seed(0)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.LazyAttribute(lambda x: faker.name())
    description = factory.LazyAttribute(lambda x: faker.text())
    created_at = factory.LazyAttribute(lambda x: faker.date_time())


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.LazyAttribute(lambda x: faker.user_name())
    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    email = factory.LazyAttribute(lambda x: faker.email())
    password = factory.LazyAttribute(lambda x: faker.password())
    is_active = True
    is_staff = False
    is_superuser = False
    last_login = factory.LazyAttribute(lambda x: faker.date_time(tzinfo=pytz.utc))
    date_joined = factory.LazyAttribute(lambda x: faker.date_time(tzinfo=pytz.utc))


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.LazyAttribute(lambda x: faker.name())
    description = factory.LazyAttribute(lambda x: faker.text())
    created_at = factory.LazyAttribute(lambda x: faker.date_time(tzinfo=pytz.utc))
    updated_at = factory.LazyAttribute(lambda x: faker.date_time(tzinfo=pytz.utc))
    price = factory.LazyAttribute(lambda x: faker.pyint())
    stock = factory.LazyAttribute(lambda x: faker.pyint())
    image = factory.LazyAttribute(lambda x: faker.url())
    is_active = factory.LazyAttribute(lambda x: faker.pybool())
    category = factory.SubFactory(CategoryFactory)


class OrderFactory(factory.django.DjangoModelFactory):
    """[summary]

    Args:
        factory ([object]): [a factory object] representing an order

    """

    class Meta:
        model = Order

    user = factory.SubFactory(UserFactory)
    product_names = factory.SubFactory(ProductFactory)
    total_products = factory.LazyAttribute(lambda x: faker.pyint())
    total_amount = factory.LazyAttribute(lambda x: faker.pyint())
    transaction_id = factory.LazyAttribute(lambda x: random_string_generator(size=10))
