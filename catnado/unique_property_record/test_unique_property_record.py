"""
The type of race condition that this class is designed to prevent is somewhat
difficult to write unit tests for.

My apologies for the abysmal coverage.

T
"""

from google.appengine.ext import db

from catnado.testing.testcase import SimpleAppEngineTestCase
from catnado.unique_property_record import (
  UniquePropertyRecord,
  UniquePropertyRecordExistsError,
)

NAME = 'name'
TEST = 'test'
UNIQUE_NAME = 'unique_name'
PARENT = 'parent'


class SimpleTestModel(db.Model):
  unique_name = db.StringProperty()


class UniquePropertyRecordTest(SimpleAppEngineTestCase):

  def test_duplicate_key_raises_exception(self):
    UniquePropertyRecord.create(TEST, TEST, TEST)
    with self.assertRaises(UniquePropertyRecordExistsError):
      UniquePropertyRecord.create(TEST, TEST, TEST)

    UniquePropertyRecord.create(SimpleTestModel, UNIQUE_NAME, NAME)
    with self.assertRaises(UniquePropertyRecordExistsError):
      UniquePropertyRecord.create(SimpleTestModel, UNIQUE_NAME, NAME)

  def test_nones_disallowed(self):
    with self.assertRaises(AssertionError):
      UniquePropertyRecord.create(TEST, TEST, None)
