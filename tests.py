from main import fact, Animal, Dog, Cat
from nose.tools import raises
# nose


class TestFunctions:
    def test_fact(self):
        assert fact(0) == 1
        assert fact(1) == 1
        assert fact(6) == 2 * 3 * 4 * 5 * 6

    @raises(AssertionError)
    def test_fact2(self):
        fact(-1)


class TestAnimals:
    def setUp(self):
        self.dog = Dog("Furby")
        self.cat = Cat("Mary")

    def tearDown(self):
        pass

    def test_dog(self):
        assert self.dog
        assert self.cat

    # def test_said(self):
    #     assert self.dog.say() == "Гав"
    #     assert self.cat.say() == "Мяу"
