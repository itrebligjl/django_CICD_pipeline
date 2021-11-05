from django.test import TestCase
from tutorials.models import Tutorial
from django.urls import reverse
import pytest

# Create your tests here.
@pytest.mark.django_db
def test_create_tutorial():
    new_tutorial = Tutorial.objects.create(title='Pytest', 
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html', 
        image_path='/static/images/pytest.pnc', 
        description='Tutorial on how to apply pytest to a Django application', 
        published=True)
    assert new_tutorial.title == "Pytest"

@pytest.fixture
def tutorial(db) -> Tutorial:
    new_tutorial = Tutorial.objects.create(title='Pytest', 
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html', 
        image_path='/static/images/pytest.pnc', 
        description='Tutorial on how to apply pytest to a Django application', 
        published=True)
    return new_tutorial

def test_search_tutorials(tutorial):
    Tutorial.objects.create(title='Pytest', 
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html', 
        image_path='/static/images/pytest.pnc', 
        description='Tutorial on how to apply pytest to a Django application', 
        published=True)
    assert Tutorial.objects.filter(title='Pytest').exists()

def test_update_tutorial(tutorial):
    new_tutorial = Tutorial.objects.create(title='Pytest', 
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html', 
        image_path='/static/images/pytest.pnc', 
        description='Tutorial on how to apply pytest to a Django application', 
        published=True)
    new_tutorial.title='Pytest-Django'
    new_tutorial.save()
    updated_tutorial = Tutorial.objects.get(title='Pytest-Django')
    assert updated_tutorial.title == 'Pytest-Django'

@pytest.fixture
def first_tutorial(db, tutorial):
    first_tutorial = Tutorial.objects.create(title='Pytest', 
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html', 
        image_path='/static/images/pytest.pnc', 
        description='Tutorial on how to apply pytest to a Django application', 
        published=True)
    return first_tutorial

@pytest.fixture
def second_tutorial(db, tutorial):
    second_tutorial = Tutorial.objects.create(title='Pytest-Django', 
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html', 
        image_path='/static/images/pytest.pnc', 
        description='Tutorial on how to apply pytest to a Django application', 
        published=True)
    return second_tutorial

def test_compare_tutorials(first_tutorial, second_tutorial):
    assert first_tutorial.pk != second_tutorial.pk

# @pytest.fixture(params=("Pytest", "Pytest-Django"))
# def tutorials(db, request):
#     return Tutorial.objects.create(title=request.param, 
#         tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html', 
#         image_path='/static/images/pytest.pnc', 
#         description='Tutorial on how to apply pytest to a Django application', 
#         published=True)

# def test_description_non_blank(tutorials):
#     for desc in tutorials:
#         assert tutorials.description != ''

@pytest.mark.django_db
def test_home_page_access(client):
   url = reverse('home')
   response = client.get(url)
   assert response.status_code == 200