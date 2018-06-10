from decimal import Decimal

from catnado.properties.decimal_property import DecimalProperty
from catnado.testing.testcase import SimpleAppEngineTestCase
from google.appengine.ext import db


class DecimalPropertyTestModel(db.Model):
  value = DecimalProperty(required=True)


class TestDecimalProperty(SimpleAppEngineTestCase):

  def test_creation_with_decimal(self):
    entity = DecimalPropertyTestModel.get(
      DecimalPropertyTestModel(value=Decimal('2.5')).put()
    )
    self.assertEqual(entity.value, Decimal('2.5'))

  def test_creation_with_string(self):
    entity = DecimalPropertyTestModel.get(
      DecimalPropertyTestModel(value='2.5').put()
    )
    self.assertEqual(entity.value, Decimal('2.5'))
