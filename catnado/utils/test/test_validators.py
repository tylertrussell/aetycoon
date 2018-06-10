from catnado.testing.app import create_simple_test_app
from catnado.testing.testcase import SimpleAppEngineTestCase
from catnado.utils.validators import validate, ValidationError
from webapp2 import RequestHandler, Route


def validate_color(value):
  if value not in ['red', 'blue']:
    raise ValidationError('Expected red or blue, got {}'.format(value))


class ValidatorTestHandler(RequestHandler):

  @validate('key', basestring, required=True)
  def test_function(self):
    pass

  @validate('key', basestring, extra_validators=[validate_color], required=True)
  def test_function_extra_validators(self):
    pass


class ValidatorTest(SimpleAppEngineTestCase):

  def setUp(self):
    super(ValidatorTest, self).setUp()
    self.app = create_simple_test_app([
      Route(
        '/test',
        handler=ValidatorTestHandler,
        handler_method='test_function',
        methods=['GET'],
      ),
      Route(
        '/test/unicode_post',
        handler=ValidatorTestHandler,
        handler_method='test_function_extra_validators',
        methods=['POST'],
      )
    ])

  def test_required_validator(self):
    response = self.app.get('/test', expect_errors=True)
    self.assertEqual(response.status_int, 400)

  def test_extra_validator(self):
    response = self.app.post(
      '/test/unicode_post',
      {'key': 'orange'},
      expect_errors=True,
    )
    self.assertEqual(response.status_int, 400)
