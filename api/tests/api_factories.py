from random import random
import factory
import pytz

from api.category.models import Category
from api.user.models import CustomUser
from api.product.models import Product
from faker import Factory, Faker


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


class ProducFactory(factory.django.DjangoModelFactory):
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
    