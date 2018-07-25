import logging


CLEAN_DATA = 'clean_data'
EMPTY_STRING = ''
ERROR = 'error'
ERROR_EXTRA_VALIDATORS_NO_TYPE = 'one of type or extra validators is required'
VALIDATION_FAILED_HTTP_STATUS_CODE = 400


class ValidationError(Exception):
  """Raise when a request validation decorator fails.

  See: validate.
  """

  pass


def default_validation_failed_handler(key, message, handler):
  """Handle a ValidationError with an HTTP 400.

  Args:
    key: the key that failed validation
    message: description of why the ValidationError was raised
    handler: reference to the RequestHandler subclass

  """
  logging.info('request param "{}" failed validation: {}'.format(key, message))
  handler.abort(VALIDATION_FAILED_HTTP_STATUS_CODE)


def validate(key, new_type, extra_validators=None, required=False, excs=None,
             custom_error_handler=None):
  """Use as a decorator to validate incoming request data.

  The validated request data is stored on `self.request.clean_data` so that it
  can be used by the handler later.

  Note that, from within an inner function, you cannot assign to a variable that
  was defined in an outer function, so this pattern
  >>> def func_name(some, variable=None):
  >>>   variable = variable or default
  cannot be followed, hence the verbose variable naming.

  Args:
    key: the request data key to validate
    new_type: optional desired type; if None, you must specify extra_validators
      note: arg (not kwarg) because it should be specified most of the time.
      This type must be instantiable! i.e. use unicode, not basestring.
    extra_validators: optional validator func (or funcs)
    required: optional bool; whether this field is required (defaults False)
    excs: optional Exception class (or tuple thereof) to catch when casting the
      request data to new_type, (i.e. InvalidOperation for Decimal). Defaults to
      ValueError.
    custom_error_handler: optional callable to handle ValidationErrors, matching
      the signature of (and defaulting to) default_validation_failed_handler.

  Raises:
    AssertionError: if type_ is not a type
    ValidationError: if the value is missing and required or if the value can't
      be converted to the given type
  """
  def outer_decorator(func):
    def inner_decorator(self, *args, **kwargs):

      assert isinstance(new_type, (list, type))

      error_handler = custom_error_handler or default_validation_failed_handler

      value = self.request.params.get(key, EMPTY_STRING)
      if value == EMPTY_STRING:
        if required:
          message = 'required value missing'
          error_handler(key, message, self)
          return
        else:  # don't run extra validators on EMPTY_STRING, just continue
          func(self, *args, **kwargs)
          return

      if new_type:
        try:
          new_value = new_type(value)
        except excs or ValueError, e:
          message = 'not a valid {}'.format(key, new_type)
          error_handler(key, message, self)
          return
      else:
        assert extra_validators, ERROR_EXTRA_VALIDATORS_NO_TYPE
        new_value = value

      if extra_validators:
        if not isinstance(extra_validators, list):
          validators_to_run = [extra_validators]
        else:
          validators_to_run = extra_validators

        for extra_validator in validators_to_run:
          try:
            new_value = extra_validator(new_value)
            if not new_value:
              logging.warn('validator {} returned None'.format(extra_validator))
          except ValidationError as e:
            error_handler(key, e.message, self)
            return

      clean_data = self.request.registry.setdefault(CLEAN_DATA, {})
      clean_data[key] = new_value

      func(self, *args, **kwargs)

    return inner_decorator
  return outer_decorator
