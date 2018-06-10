import unittest

from catnado.utils.api import ApiDict


class TestApiDict(unittest.TestCase):

  def test_stringify(self):
    test_data = {
      'test': {
        'data': ['goes', 'here']
      }
    }
    test_data_as_string = ApiDict(test_data).stringify()
    self.assertEqual(test_data, ApiDict.from_string(test_data_as_string))
