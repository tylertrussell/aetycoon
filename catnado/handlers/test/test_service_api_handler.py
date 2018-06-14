import json

from google.appengine.api import app_identity
from webapp2 import Route

from catnado.handlers import CONTENT_TYPE, CONTENT_TYPE_JSON
from catnado.handlers.service_api_handler import ServiceAPIHandler
from catnado.testing.app import create_simple_test_app
from catnado.testing.testcase import SimpleAppEngineTestCase
from catnado.utils.api import INBOUND_APP_ID


TEST_REQUEST_DATA = {
  'message': 'hello world'
}


class SimpleServiceAPIHandler(ServiceAPIHandler):

  def test_function(self):
    self.json_response(TEST_REQUEST_DATA)


class ServiceAPIHandlerTest(SimpleAppEngineTestCase):

  def setUp(self):
    super(ServiceAPIHandlerTest, self).setUp()
    self.app = create_simple_test_app([
      Route(
        '/test',
        handler=SimpleServiceAPIHandler,
        handler_method='test_function',
        methods=['GET']
      )
    ])

  def test_normal_requests_rejected(self):
    response = self.app.get('/test', expect_errors=True)
    self.assertEqual(response.status_int, 403)

  def test_urlfetch_requests_accepted(self):
    response = self.app.get('/test', headers={
      INBOUND_APP_ID: app_identity.get_application_id()
    })
    self.assertEqual(response.status_int, 200)

  def test_json_response(self):
    response = self.app.get('/test', headers={
      INBOUND_APP_ID: app_identity.get_application_id()
    })
    self.assertEqual(response.status_int, 200)
    self.assertEqual(response.headers.get(CONTENT_TYPE), CONTENT_TYPE_JSON)
    raw_response = response.body
    json_response = json.loads(raw_response)
    self.assertEqual(json_response, TEST_REQUEST_DATA)
