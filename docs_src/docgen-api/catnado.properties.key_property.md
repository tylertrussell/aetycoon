# 










## Classes
    
    
###`KeyProperty`

A property that stores a key without automatically dereferencing it or
  requiring a dependency between model classes.

  `db.ReferenceProperty` performs a datastore RPC when it is accessed, which
  can lead to unforeseen performance problems.

  Furthermore, it needs to have the Kind specified when it is declared, which
  creates a code dependency between models that can be undesirable.

  `KeyProperty` helps alleviate these concerns.
  

        
#### Class Functions
            
            
`validate`


    Args:
      value: The value to validate.
    Returns:
      A valid key.
    Raises:
      TypeError if the value can't be converted into a `db.Key`
    
 
            

        

    
