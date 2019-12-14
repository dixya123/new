from django.test import TestCase
from .models import CategoryModel


# Create your tests here.
class CategoryModelTest():
    def setup(self):
        self.django = CategoryModel.objects.Create(name='django' ,description='django unchained')
    def test_foobar(self):
        cat=CategoryModel.objects.get(name='django' ,description='django unchained')
        self.assertEqual(cat,'django')
