# 




## Attributes
    
`ERROR_EXTRA_VALIDATORS_NO_TYPE`
    
`CLEAN_DATA`
    





## Functions
    
### `validate`

Use as a decorator to validate incoming request data.

  The validated request data is stored on `self.request.clean_data` so that it
  can be used by the handler later.

  Args:
    key: the request data key to validate
    new_type: optional desired type; if None, you must specify extra_validators
      note: arg (not kwarg) because it should be specified most of the time
    extra_validators: optional validator func (or funcs)
    required: optional bool; whether this field is required (defaults False)

  Raises:
    AssertionError: if type_ is not a type
    ValidationError: if the value is missing and required or if the value can't
      be converted to the given type
  

    
    




## Classes
    
    
###`ValidationError`

Raise when a request validation decorator fails.

  See: validate.
  

        
        
            

        

    
