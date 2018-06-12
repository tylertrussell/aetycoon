# 




## Attributes
    
`CONTENT_TYPE_JSON`
    
`CONTENT_TYPE`
    





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
  

    
    




## Classes
    
    
###`ServiceAPIHandler`

Handler for serving a microservice's internal API.

  Ensures that incoming requests are coming from within the same application by
  verifying that the X-Appengine-Inbound-Appid matches the current application's
  ID.
  

        
        
            

`json_response`

Set Content-Type and write JSON data in a response.

    Arguments:
      data: a dict to JSON-stringify and return
    

            

`dispatch`

Override dispatch to validate incoming requests are secure.

    A request is secure if its X-Appengine-Internal-Appid header matches the
    applications current application ID.
    

            

        

    
