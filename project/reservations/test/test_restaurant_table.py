from django.test import TestCase
from reservations.models import RestaurantTable
from django.core.exceptions import ValidationError

class RestaurantTableModelTest(TestCase):
    
    def create_table(self, capacity):
        return RestaurantTable(capacity = capacity)
    
    def test_canary(self):
        self.assertTrue(True)

    def test_initializing_a_table(self):
        table = self.create_table(4)
        table.save()

        self.assertEqual(RestaurantTable.objects.count(), 1)
        
    def test_table_capacity_limits(self):
        table_one = self.create_table(2)
        table_one.save()
        self.assertEqual(RestaurantTable.objects.count(), 1)
        self.assertLessEqual(table_one.capacity, 8)

        table_two = self.create_table(8)
        table_two.save()
        self.assertEqual(RestaurantTable.objects.count(), 2)
        self.assertLessEqual(table_two.capacity, 8)

        table_three = self.create_table(7)
        table_four = self.create_table(10)
        
        self.assertRaises(ValidationError, table_three.save)
        self.assertRaises(ValidationError, table_four.save)

