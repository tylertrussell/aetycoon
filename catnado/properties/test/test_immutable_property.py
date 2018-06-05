from google.appengine.ext import db

from catnado.properties.immutabe_property import (
  ImmutableStringProperty,
  ImmutablePropertyException,
)
from catnado.testing.testcase import SimpleAppEngineTestCase


class ImmutablePropertyTestModel(db.Model):
  """ A simple model for testing """
  name = ImmutableStringProperty(required=True)
  human_name = db.StringProperty(required=True)


class TestImmutableProperty(SimpleAppEngineTestCase):

  def test_immutable_property_cannot_be_changed(self):

    NAME = 'name'
    HUMAN_NAME = 'human_name'

    entity = ImmutablePropertyTestModel(
      name=NAME,
      human_name=HUMAN_NAME,
    )

    with self.assertRaises(ImmutablePropertyException):
      entity.name = 'anything'

    refetched_entity = ImmutablePropertyTestModel.get(entity.put())

    self.assertEqual(refetched_entity.name, NAME)

    with self.assertRaises(ImmutablePropertyException):
      refetched_entity.name = 'anything'
