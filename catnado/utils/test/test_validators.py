from decimal import Decimal, InvalidOperation

from webapp2 import Route

from catnado.handlers import CatnadoHandler
from catnado.testing.app import create_simple_test_app
from catnado.testing.testcase import SimpleAppEngineTestCase
from catnado.utils.validators import validate, ValidationError


def validate_color(value):
  if value not in ['red', 'blue']:
    raise ValidationError('Expected red or blue, got {}'.format(value))


class ValidatorTestHandler(CatnadoHandler):

  # TODO ungross this
  def respond_with_type_and_value(self, value):
    t = type(value)
    v = value
    if isinstance(v, Decimal):  # not json serializable
      v = str(v)
    self.json_response({
      'type': t.__name__,
      'value': v,
    })

  @validate('test', unicode, required=True)
  def test_function(self):
    pass

  @validate('test', unicode, extra_validators=[validate_color], required=True)
  def test_function_extra_validators(self):
    pass

  @validate('test', bool, required=True)
  def test_bool_validator(self):
    pass

  @validate('test', Decimal, required=True, excs=(InvalidOperation))
  def test_decimal_validator(self):
    pass


class ValidatorTest(SimpleAppEngineTestCase):

  def setUp(self):
    super(ValidatorTest, self).setUp()
    self.app = create_simple_test_app([
      Route(
        '/test',
        handler=ValidatorTestHandler,
        handler_method='test_function',
        methods=['POST'],
      ),
      Route(
        '/test/extra_validators',
        handler=ValidatorTestHandler,
        handler_method='test_function_extra_validators',
        methods=['POST'],
      ),
      Route(
        '/test/bool_validator',
        handler=ValidatorTestHandler,
        handler_method='test_bool_validator',
        methods=['POST'],
      ),
      Route(
        '/test/decimal_validator',
        handler=ValidatorTestHandler,
        handler_method='test_decimal_validator',
        methods=['POST'],
      )
    ])

  def test_required_validator(self):
    response = self.app.post('/test', expect_errors=True)
    self.assertEqual(response.status_int, 400)
    response = self.app.post('/test', params={'test': 'gizmo'})
    self.assertEqual(response.status_int, 200)

  def test_extra_validator(self):
    self.assertEqual(
      self.app.post(
        '/test/extra_validators',
        {'test': 'orange'},
        expect_errors=True,
      ).status_int, 400
    )
    self.assertEqual(
      self.app.post(
        '/test/extra_validators',
        {'test': 'blue'},
      ).status_int, 200
    )

  def test_boolean_validator(self):
    target = '/test/bool_validator'

    for item in ['True', 'bloop', '1', 1]:
      response = self.app.post(target, {'test': item})
      self.assertEqual(response.status_int, 200)

    response = self.app.post(target, '', expect_errors=True)
    self.assertEqual(response.status_int, 400)

  def test_decimal_validator(self):
    target = '/test/decimal_validator'
    for item in ['1', '1.0', '1.00']:
      self.assertEqual(self.app.post(target, {'test': item}).status_int, 200)
    response = self.app.post(target, {'test': 'notdecimal'}, expect_errors=True)
    self.assertEqual(response.status_int, 400)
