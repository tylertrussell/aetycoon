# 




## Attributes
    
`EVENT_TYPE_CHANGED_ACTIVE_VERSION` =  `changed active version`
    
`ERROR_WRONG_VERSION_PARENT` =  `The provided datastore key does not correspond to a version of this model.`
    
`ERROR_WRONG_PARENT_TYPE` =  `Expected VersionedModel to have a VersionUnifier parent, but got a %s instead.`
    
`ERROR_MISSING_VERSION_UNIFIER` =  `Missing VersionUnifier datastore entity`
    
`EVENT_DATA_OLD_ACTIVE_VERSION` =  `old version`
    
`EVENT_KEY` =  `event`
    
`EVENT_DATA_TIMESTAMP` =  `timestamp`
    
`EVENT_DATA_NEW_ACTIVE_VERSION` =  `new version`
    







## Classes
    
    
###`KeyProperty`

A property that stores a key without automatically dereferencing it or
  requiring a dependency between model classes.

  `db.ReferenceProperty` performs a datastore RPC when it is accessed, which
  can lead to unforeseen performance problems.

  Furthermore, it needs to have the Kind specified when it is declared, which
  creates a code dependency between models that can be undesirable.

  `KeyProperty` helps alleviate these concerns.
  

    
    
###`VersionUnifier`

 Common datastore ancestor for every version of a versioned model.
  Authoritative source of which version is active.
  

    
    
###`PickleProperty`

A property for storing complex objects in the datastore in pickled form.

  Example usage:

  >>> class PickleModel(db.Model):
  ...   data = PickleProperty()

  >>> model = PickleModel()
  >>> model.data = {"foo": "bar"}
  >>> model.data
  {'foo': 'bar'}
  >>> model.put() # doctest: +ELLIPSIS
  datastore_types.Key.from_path(u'PickleModel', ...)

  >>> model2 = PickleModel.all().get()
  >>> model2.data
  {'foo': 'bar'}
  

    
    
###`datetime`

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints or longs.


    
    
###`VersionedModel`

 Model with built-in versioning. Each entity represents a single version
  and all versions share a common `VersionUnifier` datastore parent.
  

    
