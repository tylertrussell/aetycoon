

class ValidationError(Exception):
  pass


def validate(key, types, required=False):
  """Decorator to validate request data.

  Args:
    key: the request data key to validate
    types: a type or list or list of types that are acceptable
    required: optional bool; whether this field is required (defaults False)

  Raises:
    AssertionError: if types is not a type or list of types
    ValidationError: if the request contains invalid data
  """

  def outer_decorator(func):
    def inner_decorator(self, *args, **kwargs):

      assert isinstance(types, (list, type))
      value = self.request.get(key)
      if not value and required:
        raise ValidationError('{} is required but missing'.format(key))
      if not isinstance(value, types):
        found = type(value)
        raise ValidationError('Expected type {}, got {}'.format(types, found))
      func(self, *args, **kwargs)

    return inner_decorator
  return outer_decorator
