from google.appengine.ext import db


class ImmutablePropertyException(Exception):
  pass


class ImmutableMixin(db.Property):
  """ Mixin to make a property immutable.
  """

  def __set__(self, instance, value):
    if getattr(instance, self.name):
      raise ImmutablePropertyException('Property %s is immutable'.format(self.name))
    super(ImmutableMixin, self).__set__(instance, value)


class ImmutableStringProperty(db.StringProperty, ImmutableMixin):
  """ A StringProperty that is immutable after it is created.
  """
  pass
