import unittest
from creational_patterns.prototype import Circle

class TestPrototype(unittest.TestCase):
    def test_circle_clone(self):
        original = Circle(radius=5)
        clone = original.clone()
        self.assertEqual(original.radius, clone.radius)

if __name__ == "__main__":
    unittest.main()