# 







## Functions
    
### `TransformProperty`

Implements a 'transform' datastore property.

  TransformProperties are similar to DerivedProperties, but with two main
  differences:
  - Instead of acting on the whole model, the transform function is passed the
    current value of a single property which was specified in the constructor.
  - Property values are calculated when the property being derived from is set,
    not when the TransformProperty is fetched. This is more efficient for
    properties that have significant expense to calculate.

  TransformProperty can be declared as a regular property, passing the property
  to operate on and a function as the first arguments, or it can be used as a
  decorator for the function that does the calculation, with the property to
  operate on passed as an argument.

  Example:

  >>> class DatastoreFile(db.Model):
  ...   name = db.StringProperty(required=True)
  ...
  ...   data = db.BlobProperty(required=True)
  ...   size = TransformProperty(data, len)
  ...
  ...   @TransformProperty(data)
  ...   def hash(val):
  ...     return hashlib.sha1(val).hexdigest()

  You can read transform properties the same way you would regular ones:

  >>> file = DatastoreFile(name='Test.txt', data='Hello, world!')
  >>> file.size
  13
  >>> file.data
  'Hello, world!'
  >>> file.hash
  '943a702d06f34599aee1f8da8ef9f7296031d699'

  Updating the property being transformed automatically updates any
  TransformProperties depending on it:

  >>> file.data = 'Fubar'
  >>> file.data
  'Fubar'
  >>> file.size
  5
  >>> file.hash
  'df5fc9389a7567ddae2dd29267421c05049a6d31'

  Attempting to set a transform property directly will throw an error:

  >>> file.size = 123
  Traceback (most recent call last):
      ...
  DerivedPropertyError: Cannot assign to a TransformProperty

  When persisted, transform properties are stored to the datastore, and can be
  filtered on and sorted by:

  >>> file.put() # doctest: +ELLIPSIS
  datastore_types.Key.from_path(u'DatastoreFile', ...)

  >>> DatastoreFile.all().filter('size =', 13).get().hash
  '943a702d06f34599aee1f8da8ef9f7296031d699'
  

    



