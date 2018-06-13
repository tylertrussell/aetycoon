# 








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



            

`inner_decorator`



            

`inner_decorator`



            

`respond_with_type_and_value`



            

        

    
    
###`ValidatorTest`



        
        
            

`test_required_validator`



            

`test_extra_validator`



            

`test_decimal_validator`



            

`test_boolean_validator`



            

`json_post`

Helper for testing validator endpoints.

            

`setUp`



            

        

    
