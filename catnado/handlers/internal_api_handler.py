from webapp2 import RequestHandler

from catnado.utils.api import validate_api_request, InsecureAPIRequestError


class MicroserviceAPIHandler(RequestHandler):
  """ Handler for serving a microservice's internal API.

  Ensures that incoming requests are coming from within the same application by
  verifying that the X-Appengine-Inbound-Appid matches the current application's
  ID.
  """

  def dispatch(self):
    """ Override dispatch to validate incoming requests are secure.

    A request is secure if its X-Appengine-Internal-Appid header matches the
    applications current application ID.
    """
    try:
      validate_api_request(self.request)

    except InsecureAPIRequestError:
      self.abort(403)

    super(MicroserviceAPIHandler, self).dispatch()
