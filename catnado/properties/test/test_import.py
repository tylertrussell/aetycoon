import pkgutil

from catnado.testing.testcase import SimpleAppEngineTestCase


class CatnadoPropertyImportTest(SimpleAppEngineTestCase):

  def test_importing_catnado_properties(self):
    prefix = '{}.'.format(self.__module__.__name__)
    for _, name, _ in pkgutil.iter_modules(self.__path__, prefix=prefix):
      try:
        __import__(name)
      except e:
        print 'Error importing module {}'.format(name)
        raise
