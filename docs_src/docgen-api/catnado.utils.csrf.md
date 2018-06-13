# 




## Attributes
    
`CSRF_TOKEN_COOKIE_KEY`
    
`CSRF_TOKEN_FORM_KEY`
    





## Functions
    
### `validate_csrf_token`

Validate a CSRF token on behalf of a handler.

  A CSRF token is considered valid if it exists and matches the CSRF token
  found in the Cookie.

  Args:
    handler: webapp2.RequestHandler subclass instance

  Returns:
    bool; True if CSRF token present and valid
  

    
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
  

    
    



