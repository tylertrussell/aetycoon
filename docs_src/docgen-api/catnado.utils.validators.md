# 








## Functions
    
### `validate`

Use as a decorator to validate incoming request data.

  Args:
    key: the request data key to validate
    types: a type or list or list of types that are acceptable
    extra_validators: an optional function or list of functions to call on the
      specified key
    required: optional bool; whether this field is required (defaults False)

  Raises:
    AssertionError: if types is not a type or list of types
    ValidationError: if the request contains invalid data
  

    
    




## Classes
    
    
###`ValidationError`

Raise when a request validation decorator fails.

  See: validate.
  

        
        
            

        

    
