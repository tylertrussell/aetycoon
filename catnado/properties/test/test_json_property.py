import unittest

from catnado.properties.json_property import JSONProperty
from catnado.properties.test.data import json_data, json_schemas
from catnado.testing.testcase import SimpleAppEngineTestCase
from google.appengine.ext import db
import jsonschema


class JSONPropertyTestDataSanityCheckTest(unittest.TestCase):

  def test_sanity_check_geo_schema(self):

    for entry in json_data.GOOD_GEO_DATA:
      jsonschema.validate(entry, json_schemas.GEO)

    for entry in json_data.BAD_GEO_DATA:
      with self.assertRaises(jsonschema.ValidationError):
        jsonschema.validate(entry, json_schemas.GEO)

  def test_sanity_check_address_schema(self):

    for entry in json_data.GOOD_ADDRESS_DATA:
      jsonschema.validate(entry, json_schemas.ADDRESS)

    for entry in json_data.BAD_ADDRESS_DATA:
      with self.assertRaises(jsonschema.ValidationError):
        jsonschema.validate(entry, json_schemas.ADDRESS)


class SimpleJSONPropertyTestModel(db.Model):
  address = JSONProperty(schema=json_schemas.ADDRESS)
  geo = JSONProperty(schema=json_schemas.GEO)


class JSONPropertyTest(SimpleAppEngineTestCase):

  def test_validation(self):

    SimpleJSONPropertyTestModel(
      address=json_data.GOOD_ADDRESS_DATA[0],
      geo=json_data.GOOD_GEO_DATA[0]
    ).put()

    with self.assertRaises(db.BadValueError):
      SimpleJSONPropertyTestModel(
        address=json_data.GOOD_ADDRESS_DATA[0],
        geo=json_data.BAD_ADDRESS_DATA[0]
      ).put()
