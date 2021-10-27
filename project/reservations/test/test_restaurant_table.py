from django.test import TestCase
from reservations.models import *
from django.core.exceptions import ValidationError

def create_table(capacity):
    return RestaurantTable(capacity = capacity)

class RestaurantTableModelTest(TestCase):
    
    def test_canary(self):
        self.assertTrue(True)

    def test_initializing_a_table(self):
        table = create_table(4)
        table.save()

        self.assertEqual(RestaurantTable.objects.count(), 1)
        
    def test_table_capacity_limits(self):
        table_one = create_table(2)
        table_one.save()
        self.assertEqual(RestaurantTable.objects.count(), 1)

        table_two = create_table(8)
        table_two.save()
        self.assertEqual(RestaurantTable.objects.count(), 2)

        table_three = create_table(7)
        table_four = create_table(10)
        
        self.assertRaises(ValidationError, table_three.save)
        self.assertRaises(ValidationError, table_four.save)

