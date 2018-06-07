from google.appengine.ext import db

from catnado.properties.translatable_property import TranslatableStringProperty
from catnado.testing.testcase import SimpleAppEngineTestCase


class SimpleTranslatablePropertyEntity(db.Model):
  """ Simple entity for testing """
  description = TranslatableStringProperty()


class TestTranslatableSringProperty(SimpleAppEngineTestCase):

  def test_simple_entity(self):
    SimpleTranslatablePropertyEntity(description={
      'en': 'test',
      'es': 'prueba'
    }).put()

  def test_getting_translation(self):
    entity = SimpleTranslatablePropertyEntity.get(
      SimpleTranslatablePropertyEntity(description={
        'en': 'take a glance at the fancy ants',
        'es': 'echa un vistazo a las elegantes hormigas'
      }).put()
    )
    self.assertEqual(
      entity.description.get_translation('es'),
      'echa un vistazo a las elegantes hormigas',
    )
