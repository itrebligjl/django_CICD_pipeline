from django.test import TestCase
from django.urls import reverse
import uuid
import pytest

# Create your tests here.
@pytest.fixture
def test_password_strength():
   return 'strong password'

@pytest.fixture
def create_user(db, django_user_model, test_password_strength):
   def create_new_user(**kwargs):
       kwargs['password'] = test_password_strength
       if 'username' not in kwargs:
           kwargs['username'] = str(uuid.uuid4())
       return django_user_model.objects.create_user(**kwargs)
   return create_new_user

@pytest.fixture
def auto_login_user(db, client, create_user, test_password_strength):
   def perform_login(user=None):
       if user is None:
           user = create_user()
       client.login(username=user.username, password=test_password_strength)
       return client, user
   return perform_login

@pytest.mark.django_db
def test_authenticate_user(auto_login_user):
   client, user = auto_login_user()
   url = reverse('login')
   response = client.get(url)
   assert response.status_code == 200
