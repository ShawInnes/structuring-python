import unittest

from unique_customer import UniqueCustomer


class MyTestCase(unittest.TestCase):
    data = ['first', 'last', 'email@here.com', '0412123123']
    expected = 'firstlastemail@here.com0412123123'

    def test_all_lowercase(self):
        # Arrange
        sut = UniqueCustomer()

        # Act
        result = sut.calc_checksum(self.data)

        # Assert
        self.assertEqual(result, self.expected)


if __name__ == '__main__':
    unittest.main()
