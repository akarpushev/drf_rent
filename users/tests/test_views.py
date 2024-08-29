import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_home_view_renders_template():
    client = Client()
    response = client.get(reverse('home'))  # Используем имя маршрута 'home'
    assert response.status_code == 200
    assert 'Welcome to the Home Page!' in response.content.decode()
