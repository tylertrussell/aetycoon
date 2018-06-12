# 










## Classes
    
    
###`KeyProperty`

Property that stores a key without automatically dereferencing it.

  Note that the default alternative, `db.ReferenceProperty`, performs a
  datastore RPC when it is accessed, which can lead to hidden performance
  problems.

  Furthermore, it needs to have the Kind specified when it is declared, which
  creates a code dependency between models that can be undesirable.

  `KeyProperty` helps alleviate these concerns.
  

        
        
            

`validate`

Validate value is a key or model.

    Args:
      value: The value to validate.
    Returns:
      google.appengine.ext.db.Key
    Raises:
      TypeError if the value can't be converted into a `db.Key`
    

            

        

    
