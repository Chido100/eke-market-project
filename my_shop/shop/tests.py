from django.test import TestCase
from django.db import IntegrityError
from .models import Category, Product

# Test shop models
class TestShopModel(TestCase):

    # test shop category model
    def test_category_model(self):
        new_cat = Category.objects.create(name='Toys', slug='toys')
        self.assertEqual(new_cat.name, 'Toys')
        self.assertEqual(new_cat.slug, 'toys')

        try:
            duplicate_cat = Category.objects.create(name='Duplicate', slug='toys')
        except IntegrityError:
            pass
        else:
            self.fail('Category with duplicate slug should not be created')

    # test shop product model
    def setUp(self):
        self.category = Category.objects.create(name='Books', slug='books')

    def test_product_model(self):
       new_product = Product.objects.create(
        category=self.category, name='Test Book',
        slug='test-book', image='',
        description='This is a test', price=20.00,
        available=True
       )
       self.assertEqual(new_product.name, 'Test Book')


# Test Shop views


    
