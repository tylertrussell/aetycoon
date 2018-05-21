# 










## Classes
    
    
###`SetProperty`

A property that stores a set of things.

  This is a parameterized property; the parameter must be a valid
  non-list data type, and all items must conform to this type.

  Example usage:

  >>> class SetModel(db.Model):
  ...   a_set = SetProperty(int)

  >>> model = SetModel()
  >>> model.a_set = set([1, 2, 3])
  >>> model.a_set
  set([1, 2, 3])
  >>> model.a_set.add(4)
  >>> model.a_set
  set([1, 2, 3, 4])
  >>> model.put() # doctest: +ELLIPSIS
  datastore_types.Key.from_path(u'SetModel', ...)

  >>> model2 = SetModel.all().get()
  >>> model2.a_set
  set([1L, 2L, 3L, 4L])
  

    
