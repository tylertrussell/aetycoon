# 










## Classes
    
    
###`CurrentDomainProperty`

A property that restricts access to the current domain.

  Example usage:

  >>> class DomainModel(db.Model):
  ...   domain = CurrentDomainProperty()

  >>> os.environ['HTTP_HOST'] = 'domain1'
  >>> model = DomainModel()

  The domain is set automatically:

  >>> model.domain
  u'domain1'

  You cannot change the domain:

  >>> model.domain = 'domain2'  # doctest: +ELLIPSIS
  Traceback (most recent call last):
      ...
  InvalidDomainError: Domain 'domain1' attempting to illegally access data for domain 'domain2'

  >>> key = model.put()
  >>> model = DomainModel.get(key)
  >>> model.domain
  u'domain1'

  You cannot write the data from another domain:

  >>> os.environ['HTTP_HOST'] = 'domain2'
  >>> model.put() # doctest: +ELLIPSIS
  Traceback (most recent call last):
      ...
  InvalidDomainError: Domain 'domain2' attempting to allegally modify data for domain 'domain1'

  Nor can you read it:

  >>> DomainModel.get(key)  # doctest: +ELLIPSIS
  Traceback (most recent call last):
      ...
  InvalidDomainError: Domain 'domain2' attempting to illegally access data for domain 'domain1'

  Admin users can read and write data for other domains:

  >>> os.environ['USER_IS_ADMIN'] = '1'
  >>> model = DomainModel.get(key)
  >>> model.put()  # doctest: +ELLIPSIS
  datastore_types.Key.from_path(u'DomainModel', ...)

  You can also define models that should permit read or write access from
  other domains:

  >>> os.environ['USER_IS_ADMIN'] = '0'
  >>> class DomainModel2(db.Model):
  ...   domain = CurrentDomainProperty(allow_read=True, allow_write=True)

  >>> model = DomainModel2()
  >>> model.domain
  u'domain2'
  >>> key = model.put()

  >>> os.environ['HTTP_HOST'] = 'domain3'
  >>> model = DomainModel2.get(key)
  >>> model.put()  # doctest: +ELLIPSIS
  datastore_types.Key.from_path(u'DomainModel2', ...)
  

    
    
###`InvalidDomainError`

Raised when something attempts to access data belonging to another domain.

    
