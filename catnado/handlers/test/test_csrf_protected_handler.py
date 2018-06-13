from catnado.handlers.csrf_protected_handler import CSRFProtectedHandler
from catnado.testing.app import create_simple_test_app
from catnado.testing.testcase import SimpleAppEngineTestCase
from catnado.utils.csrf import (
  CSRF_TOKEN_FORM_KEY,
  csrf_token_required,
  get_csrf_token,
)
import mock
from webapp2 import Route


class CSRFProtectedTestHandler(CSRFProtectedHandler):

  def test_get(self):
    # generates the csrf token and stores it in the cookie. normally we would
    # render this into the page as a hidden form element, but since this is
    # a test we won't bother with the HTML side of things
    get_csrf_token(self.request, self.response)

  def test_post(self):
    pass


TEST_TOKEN = 'verysecurecsrftoken'


class CSRFProtectedHandlerTest(SimpleAppEngineTestCase):

  def setUp(self):
    super(CSRFProtectedHandlerTest, self).setUp()
    self.app = create_simple_test_app([
      Route(
        '/test',
        handler=CSRFProtectedTestHandler,
        handler_method='test_get',
        methods=['GET'],
      ),
      Route(
        '/test',
        handler=CSRFProtectedTestHandler,
        handler_method='test_post',
        methods=['POST'],
      )
    ])

  def test_csrf_token_required_on_post(self):
    csrf_patch = mock.patch(
      'catnado.utils.csrf._generate_csrf_token',
      return_value=TEST_TOKEN,
    )
    with csrf_patch:
      response = self.app.get('/test')
      self.assertEqual(response.status_int, 200)

    # HTTP 200 as long as CSRF token is present in form
    response = self.app.post('/test', {
      CSRF_TOKEN_FORM_KEY: TEST_TOKEN
    })
    self.assertEqual(response.status_int, 200)

    # HTTP 403 if it is missing
    response = self.app.post('/test', expect_errors=True)
    self.assertEqual(response.status_int, 403)
