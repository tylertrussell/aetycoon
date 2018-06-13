from catnado.handlers.simple_public_handler import SimplePublicHandler


class CSRFProtectedHandler(SimplePublicHandler):
  """SimplePublicHandler that requires a CSRF token on POST."""

  def dispatch(self):
    """Override dispatch to CSRF-validate POST requests."""
    if self.request.method == 'POST':
      if not validate_csrf_token(self):
        self.abort(403)

    super(CSRFProtectedHandler, self).dispatch()
