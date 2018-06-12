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
  

    
### `validate_color`



    
### `create_simple_test_app`

Create a simple webtest.TestApp with the specified routes.

  Args:
    routes: list of webapp2.Routes

  Returns:
    webtest.TestApp wrapping a webapp2.WSGIApplication
  

    
    




## Classes
    
    
###`ValidatorTestHandler`



        
        
            

`inner_decorator`



            

`inner_decorator`



            

        

    
    
###`ValidatorTest`



        
        
            

`test_required_validator`



            

`test_extra_validator`



            

`setUp`



            

        

    
