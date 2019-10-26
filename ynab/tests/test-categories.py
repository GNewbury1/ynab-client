import unittest
from ynab.lib import category_api


class CategoryTests(unittest.TestCase):

    def get_api_categories(self):
        self.assertEqual(True, True)

    def get_test_category(self):
        test_category = category_api.category(
            'TestCat',
            'TestCatParent',
            '',
            '',
            '10.33'
        )
        expected_category = 'TestCat'
        self.assertEqual(test_category.getName(), expected_category)


if __name__ == '__main__':
    unittest.main()
