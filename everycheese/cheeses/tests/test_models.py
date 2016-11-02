from test_plus.test import TestCase

from ..models import Cheese

class TestClass(TestCase):
    def test__str__(self):
        cheese = Cheese.objects.create(
            name="Stracchino",
            description="Semi-sweet cheese that goes well with starches.",
            firmness=Cheese.FIRMNESS_SOFT,
        )
        self.assertEqual(cheese.__str__(), "Stracchino")
