# 




## Attributes
    
`TEST_TOKEN`
    
`CSRF_TOKEN_FORM_KEY`
    





## Functions
    
### `csrf_token_required`

Use as a decorator to protect handler functions from CSRF attacks.

    
### `get_csrf_token`

Get a CSRF token to embed in an HTML page.

  The token is also stored in a Cookie and verified upon POST/PUT.

  Arguments:
    request: webapp2 Request object
    response: webapp2 Response object

  Returns:
    str; a CSRF token, having been saved to the Cookie
  

    
### `create_simple_test_app`

Create a simple webtest.TestApp with the specified routes.

  Args:
    routes: list of webapp2.Routes

  Returns:
    webtest.TestApp wrapping a webapp2.WSGIApplication
  

    
    




## Classes
    
    
###`CSRFUtilitiesTest`



        
        
            

`test_csrf_token_required_decorator`



            

`setUp`



            

        

    
    
###`SimpleCSRFTestHandler`



        
        
            

`inner_decorator`



            

`test_get`



            

        

    
