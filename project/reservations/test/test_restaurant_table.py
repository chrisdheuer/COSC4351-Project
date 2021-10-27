from django.test import TestCase
from reservations.models import *
from django.core.exceptions import ValidationError

def create_table(capacity):
    return RestaurantTable(capacity = capacity)

class RestaurantTableModelTest(TestCase):
    
    def test_canary(self):
        self.assertTrue(True)

    def test_table_capacity_limits(self):
        table_one = create_table(2)
        table_two = create_table(10)
        table_three = create_table(7)
        table_four = create_table(8)

        self.assertEqual(table_one.capacity, 2)
        self.assertRaises(ValidationError, table_two.save)
        self.assertRaises(ValidationError, table_three.save)
        self.assertEqual(table_four.capacity, 8)

