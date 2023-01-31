import pytest
from django.contrib.auth.hashers import make_password
from faker import Faker
from rest_framework.reverse import reverse

from shops.models import Shop, Category, Currency
from users.models import User
from users.serializers import UserModelSerializer

fake = Faker()


@pytest.mark.django_db
class TestUserAPIView:
    @pytest.fixture
    def users(self):
        data = {
            'username': 'Jack',
            'email': 'johndoe@example.com',
            'password': make_password('string123'),
            'first_name': 'John',
            'last_name': 'Doe'
        }
        c = User.objects.create(**data)
        Shop.objects.create(name=fake.name(),
                            shop_category=Category.objects.create(name=fake.first_name()),
                            shop_currency=Currency.objects.create(name=fake.currency_code()),
                            user=c, languages=['uz', 'en', 'ru'],
                            )
        return c

    def test_user_model(self, users):
        count = User.objects.count()

        for _ in range(10):
            first_name = fake.unique.first_name()
            last_name = fake.unique.last_name()
            username = fake.profile(fields=['username'])['username']
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=f'{first_name}.{last_name}@{fake.domain_name()}'
            )
            assert first_name == user.first_name
            assert last_name == user.last_name
            assert username == user.username
        assert count < User.objects.count()

    def test_user_create_api(self, client):
        url = reverse('v1:users:register')
        data = {
            'username': 'Jack',
            'password': 'string123',
            'password2': 'string123',
            'email': 'johndoe@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response = client.post(url, data=data)
        assert response.status_code == 201
        assert response.json()['username'] == data['username']

    def test_user_retrieve_api(self, client, users):
        url = reverse('v1:users:user-detail', args=(users.id,))
        response = client.get(url)
        assert response.status_code == 200
        # assert response.json() == UserModelSerializer(users).data
        data = UserModelSerializer(users).data
        assert sorted(response.json().items()) == sorted(data.items())

    def test_user_update_api(self, client, users):
        url = reverse('v1:users:user-detail', args=(users.id,))
        data = {
            'username': 'Jane',
            'email': 'janedoe@example.com',
            'first_name': 'Jane',
        }
        response = client.patch(url, data=data, content_type='application/json')
        assert response.status_code == 200
        response = response.json()
        assert response['first_name'] == data['first_name']
        assert response['username'] == data['username']
        assert response['email'] == data['email']

    def test_user_destroy_api(self, client, users):
        url = reverse('v1:users:user-detail', args=(users.id,))
        response = client.delete(url)
        assert response.status_code == 204
        response = client.get(url)
        assert response.status_code == 404

    def test_user_change_defaul_shop_api(self, client, users):
        url = reverse('v1:users:user-detail', args=(users.id,))
        shop = users.shop_set.first()
        data = {
            'default_shop': shop.pk
        }
        response = client.patch(url, data=data, content_type='application/json')
        assert response.status_code == 200
        assert response.data['default_shop'] == shop.pk
