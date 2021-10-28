# L10-01. Unit Testing - Lab
# 03. List

class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.list = IntegerList(1, 2, 3, 4, 'a', 'b', 'c', 'd')

    def test_integer_list_init(self):
        expected_result = [1, 2, 3, 4]
        self.assertEqual(expected_result, self.list.get_data())

    def test_integer_list_add_int(self):
        element_int = 5
        expected_result = [1, 2, 3, 4, 5]
        self.list.add(element_int)
        self.assertEqual(expected_result, self.list.get_data())

    def test_integer_list_add_not_int_raises(self):
        element_int = 'e'
        expected_result = "Element is not Integer"
        expected_resulting_list = [1, 2, 3, 4]
        with self.assertRaises(ValueError) as ex:
            self.list.add(element_int)
        self.assertEqual(expected_result, str(ex.exception))
        self.assertEqual(expected_resulting_list, self.list.get_data())

    def test_integer_list_remove_index_in_range(self):
        idx = 0
        expected_result = 1
        expected_resulting_list = [2, 3, 4]
        actual_result = self.list.remove_index(idx)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_resulting_list, self.list.get_data())

    def test_integer_list_remove_index_out_of_range_raises(self):
        idx = 5
        expected_result = "Index is out of range"
        expected_resulting_list = [1, 2, 3, 4]
        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(idx)
        self.assertEqual(expected_result, str(ex.exception))
        self.assertEqual(expected_resulting_list, self.list.get_data())

    def test_integer_list_get_in_range(self):
        idx = 0
        expected_result = 1
        expected_resulting_list = [1, 2, 3, 4]
        actual_result = self.list.get(idx)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_resulting_list, self.list.get_data())

    def test_integer_list_get_out_of_range_raises(self):
        idx = 5
        expected_result = "Index is out of range"
        expected_resulting_list = [1, 2, 3, 4]
        with self.assertRaises(IndexError) as ex:
            self.list.get(idx)
        self.assertEqual(expected_result, str(ex.exception))
        self.assertEqual(expected_resulting_list, self.list.get_data())

    def test_integer_list_insert_int_in_range(self):
        idx = 0
        integer = 0
        expected_result = [0, 1, 2, 3, 4]
        self.list.insert(idx, integer)
        self.assertEqual(expected_result, self.list.get_data())

    def test_integer_list_insert_int_out_of_range_raises(self):
        idx = 10
        integer = 0
        expected_result = "Index is out of range"
        expected_resulting_list = [1, 2, 3, 4]
        with self.assertRaises(IndexError) as ex:
            self.list.insert(idx, integer)
        self.assertEqual(expected_result, str(ex.exception))
        self.assertEqual(expected_resulting_list, self.list.get_data())

    def integer_list_insert_not_int_in_range_raises(self):
        idx = 0
        not_integer = '@'
        expected_result = "Element is not Integer"
        expected_resulting_list = [1, 2, 3, 4]
        with self.assertRaises(ValueError) as ex:
            self.list.insert(idx, not_integer)
        self.assertEqual(expected_result, str(ex.exception))
        self.assertEqual(expected_resulting_list, self.list.get_data())

    def test_integer_list_insert_not_int_out_of_range_raises(self):
        idx = 10
        integer = 0
        expected_result = "Index is out of range"
        expected_resulting_list = [1, 2, 3, 4]
        with self.assertRaises(IndexError) as ex:
            self.list.insert(idx, integer)
        self.assertEqual(expected_result, str(ex.exception))
        self.assertEqual(expected_resulting_list, self.list.get_data())

    def test_integer_list_get_biggest(self):
        expected_result = 4
        expected_resulting_list = [1, 2, 3, 4]
        actual_result = self.list.get_biggest()
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_resulting_list, self.list.get_data())

    def test_integer_list_get_index_in_list(self):
        integer = 4
        expected_result = 3
        expected_resulting_list = [1, 2, 3, 4]
        actual_result = self.list.get_index(integer)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_resulting_list, self.list.get_data())

    def test_integer_list_get_index_not_in_list_raises(self):
        integer = 5
        expected_result = f"{integer} is not in list"
        expected_resulting_list = [1, 2, 3, 4]
        with self.assertRaises(ValueError) as ex:
            self.list.get_index(integer)
        self.assertEqual(expected_result, str(ex.exception))
        self.assertEqual(expected_resulting_list, self.list.get_data())


if __name__ == '__main__':
    unittest.main()
