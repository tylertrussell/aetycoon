# 




## Attributes
    
`APP_ENGINE_URL_FORMAT`
    
`DEFAULT_BASE_PATH`
    
`INBOUND_APP_ID`
    





## Functions
    
### `validate_api_request`

Validate the API Request by looking for an internal AppEngine header.

  The header should contain INBOUND_APP_ID (added securely by AppEngine) and its
  value should match this service's application ID.

  Arguments:
    request: webapp2 Request

  Raises:
    InsecureAPIRequestError: if the application ID header is missing from the
      request or the ID does not match the current application
  

    
### `async_api_call`

Make an asynchronous API call to another service in this GAE application.

  This function utilizes urlfetch with follow_redirects=False so AppEngine will
  securely add the INBOUND_APP_ID header which the target service will used to
  authenticate the request.

  Arguments:
    service: str; service name
    version: str; API version
    path: str; the API path to request
    payload: payload for urlfetch
    base_path: optional str; base API path (defaults to "api")
    method: optional int, method flag from urlfetch (defaults to urlfetch.GET)
    deadline: optional deadline in seconds

  Returns:
    urlfetch RPC object
  

    
### `blocking_api_call`

Make a blocking API call to another service in this GAE application.

  If you're going to make multiple calls in a single handler, consider using
  async_api_call.

  See async_api_call for full documentation.
  

    
    




## Classes
    
    
###`ApiDict`

Subclass dict and add helper funcs for passing data between services.

        
        
            

`stringify`

Convert this object to a str.

    Returns:
      str; object dumped to JSON string then base64 encoded
    

            

        

    
    
###`InsecureAPIRequestError`

Raised when a handler receives a request without the appropriate header.

  See validate_api_request.
  

        
        
            

        

    
