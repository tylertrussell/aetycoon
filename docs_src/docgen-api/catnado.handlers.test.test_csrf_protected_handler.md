# 




## Attributes
    
`TEST_TOKEN`
    
`CSRF_TOKEN_FORM_KEY`
    





## Functions
    
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
    
    
###`CSRFProtectedHandlerTest`



        
        
            

`test_csrf_token_required_on_post`



            

`setUp`



            

        

    
    
###`CSRFProtectedTestHandler`



        
        
            

`test_post`



            

`test_get`



            

        

    
