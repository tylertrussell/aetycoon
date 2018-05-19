import logging
import pkgutil

from catnado import properties as catnado_properties
from catnado.testing.testcase import SimpleAppEngineTestCase


class CatnadoPropertyImportTest(SimpleAppEngineTestCase):

  def test_importing_catnado_properties(self):
    prefix = '{}.'.format(catnado_properties.__name__)
    module_names = [
      module_name
      for _, module_name, _
      in pkgutil.iter_modules(catnado_properties.__path__, prefix=prefix)
      if 'test' not in module_name
    ]
    for name in module_names:
      try:
        logging.debug('importing {}'.format(name))
        __import__(name)
      except ImportError:
        logging.error('Error importing module {}'.format(name))
        raise
