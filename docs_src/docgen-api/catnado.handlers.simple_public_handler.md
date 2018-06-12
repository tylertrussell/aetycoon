# 




## Attributes
    
`CONTENT_TYPE`
    
`CONTENT_TYPE_HTML`
    





## Functions
    
### `create_jinja_environment`

Get a Jinja environment for rendering a template.

  Args:
    template_path: required str; base location of templates
  

    
    




## Classes
    
    
###`SimplePublicHandler`

Handler for serving a microservice's internal API.

  Ensures that incoming requests are coming from within the same application by
  verifying that the X-Appengine-Inbound-Appid matches the current application's
  ID.
  

        
        
            

`jinja_render`

Set Content-Type and write JSON data in a response.

    Arguments:
      kwargs: an optional dict to pass to the Jinja template
    

            

        

    
