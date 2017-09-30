import unittest
import random
from hashtable import HashTable

# The Unit Test Suite for HashTable
class TestContainer(unittest.TestCase):
    # The constructor working properly
    def test_constructor_success(self):
        size = random.randint(1, 100)
        x = HashTable(size)
        self.assertTrue(x)
        self.assertEqual(x.size, size)
        self.assertTrue(len(x.buckets)>size)
        self.assertEqual(x.itemCount, 0)

    # The Constructor given a size too small
    def test_constructor_value_error(self):
        size = 0
        try:
            x = HashTable(size)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    # The Constructor given an non-int
    def test_constructor_type_error(self):
        size = "hello"
        try:
            x = HashTable(size)
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

    # All actions should fail if given a non-string key
    def test_key_error(self):
        size = 1
        x = HashTable(size)
        try:
            x.begin_action(1)
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

    # Makes sure set returns true and increments itemCount
    def test_set_success(self):
        size = 1
        x = HashTable(size)
        self.assertTrue(x.set("test", 1))
        self.assertEqual(x.itemCount, 1)

    # Makes sure set fails if the table is full
    def test_set_failure(self):
        size = 1
        x = HashTable(size)
        x.set("test", 1)
        self.assertFalse(x.set("test2", 1))

    # Makes sure that get returns correct value when value exists
    def test_get_success(self):
        size = 1
        x = HashTable(size)
        x.set("test", 1)
        self.assertTrue(x.get("test"))
        self.assertEqual(x.get("test"), 1)

    # Makes sure that get returns the most recent value if set is
    # used twice with the same key. Also checks that itemCount is not
    # incremented
    def test_update(self):
        size = 1
        x = HashTable(size)
        x.set("test", 1)
        x.set("test", 2)
        self.assertEqual(x.get("test"), 2)
        self.assertEqual(x.itemCount, 1)

    # Makes sure that x returns none for non-existing entries
    def test_get_failure(self):
        size = 1
        x = HashTable(size)
        self.assertIsNone(x.get("test"))

    # Makes sure deleting an existing entry returns the value,
    # decrements the item count, and removes the entry
    def test_delete_success(self):
        size = 1
        x = HashTable(size)
        x.set("test", 1)
        self.assertEqual(x.delete("test"), 1)
        self.assertEqual(x.itemCount, 0)
        self.assertFalse(x.get("test"))

    # Makes sure deleting non existant values returns None
    def test_delete_failure(self):
        size = 1
        x = HashTable(size)
        self.assertFalse(x.delete("test"))

    # Tests that the type can handle alot of entries and
    # always appropriately calculates load
    def test_load(self):
        size = 100
        x = HashTable(size)
        for i in range(x.size):
            self.assertTrue(x.set("test"+str(i), i))
            self.assertEqual(x.load(), float(i+1)/float(size))

# Runs all tests
if __name__ == '__main__':
    unittest.main()
