import unittest
from ddt import ddt, data, idata, file_data, unpack

from unique_customer import UniqueCustomer

@ddt
class UniqueCustomerTestCase(unittest.TestCase):
    expected = 'firstlastemail@here.com0412123123'

    @data(
        ['first', 'last', 'email@here.com', '0412123123'],
        ['First', 'Last', 'email@here.com', '0412123123']
    )
    def test_with_ddt_data_unpack(self, test_data):
        # Arrange
        sut = UniqueCustomer()

        # Act
        result = sut.calc_checksum(test_data)

        # Assert
        self.assertEqual(result, self.expected)


if __name__ == '__main__':
    unittest.main()
