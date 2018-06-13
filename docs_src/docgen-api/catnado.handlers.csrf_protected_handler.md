# 








## Functions
    
### `validate_csrf_token`

Validate a CSRF token on behalf of a handler.

  A CSRF token is considered valid if it exists and matches the CSRF token
  found in the Cookie.

  Args:
    handler: webapp2.RequestHandler subclass instance

  Returns:
    bool; True if CSRF token present and valid
  

    
    




## Classes
    
    
###`CSRFProtectedHandler`

SimplePublicHandler that requires a CSRF token on POST.

        
        
            

`dispatch`

Override dispatch to CSRF-validate POST requests.

            

        

    
