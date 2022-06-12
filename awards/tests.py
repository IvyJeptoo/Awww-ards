from django.test import TestCase
from .models import Category,Profile,Project

# Create your tests here.
class CategoryTestCase(TestCase):
    '''
    A test case for category model
    '''
    
    def setUp(self):
        '''
        model instance setup
        '''
        self.category = Category(name='Python')
        
    def tearDown(self):
        '''
        a method to clear the db after each test case
        '''
        Category.objects.all().delete()
        
    def test_instance(self):
        '''
        test to check if created category is an instance of category class
        '''
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        '''
        test to check if the created category is being saved to the database
        '''
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
        
    def test_delete_category(self):
        '''
        test to check if saved category is being removed from the database
        '''
        
        self.category.save_category()
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)
        
    def test_update_category(self):
        '''
        test to check if updated category is being updated successfully
        '''
        self.category.save_category()
        self.category.name = 'Java'
        Category.update_category(self.category)
        update_category = Category.objects.get(id=self.category.id)
        self.assertEqual(update_category.name,'Java')
        