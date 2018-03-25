from unittest import TestCase

from structural import Structure


class TestStructural(TestCase):

    def test__list_eq(self):
        self.assertEqual(
            Structure.of([1,2,3]),
            Structure.of([4,5,6])
        )

    def test__list_ne(self):
        self.assertNotEqual(
            Structure.of([1,2,3]),
            Structure.of(['4', '5', '6'])
        )
        self.assertNotEqual(
            Structure.of([1,2,3]),
            Structure.of([1, 2, 3, 4])
        )

    def test_dict_eq(self):
        self.assertEqual(
            Structure.of({
                'a': 21,
                'b': 'bee',
                'c': None
            }),
            Structure.of({
                'a': -1,
                'b': 'B',
                'c': None 
            })
        )

    def test__dict_ne(self):
        self.assertNotEqual(
            Structure.of({
                'a': 21,
                'b': 'bee',
                'c': None,
            }),
            Structure.of({
                'a': -1,
                'b': 'B',
                'c': 12, 
            })
        )
        self.assertNotEqual(
            Structure.of({
                'a': 21,
                'b': 'bee',
                'c': None,
            }),
            Structure.of({
                'a': 21,
                'b': 'bee',
                'c': None,
                'd': 'extra item', 
            })
        )

    def test__composite_eq(self):
        self.assertEqual(
            Structure.of({
                'a': [
                    {'b': 32},
                    {'c': [None]}
                ],
                'd': 0,
                'e': {
                    'f': ['abc', 'def']
                }
            }),
            Structure.of({
                'a': [
                    {'b': 9},
                    {'c': [None]}
                ],
                'd': 100,
                'e': {
                    'f': ['CAT', 'DOG']
                }
            }),
        )

    def test__composite_ne(self):
        self.assertNotEqual(
            Structure.of({
                'a': [
                    {'b': 32},
                    {'c': [None]}
                ],
                'd': 0,
                'e': {
                    'f': ['abc', 'def']
                }
            }),
            Structure.of({
                'a': [
                    {'b': 9},
                    # {'c': [None]}
                ],
                'd': 100,
                'e': {
                    'f': ['CAT', 'DOG']
                }
            }),
        )

        self.assertNotEqual(
            Structure.of({
                'a': [
                    {'b': 32},
                    {'c': [None]}
                ],
                'd': 0,
                'e': {
                    'f': ['abc', 'def']
                }
            }),
            Structure.of({
                'a': [
                    {'b': 9},
                    # {'c': [None]}
                ],
                'd': 100,
                'e': {
                    'f': ['CAT', 'DOG']
                },
                'f': None,
            }),
        )