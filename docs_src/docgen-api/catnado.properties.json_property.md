# 










## Classes
    
    
###`JSONProperty`

Property for storing simple JSON objects backed by a schema.

        
        
            

`make_value_from_datastore`

Convert the datastore blob to a Python object.

            

`validate`

Validate that the value is valid JSON that conforms to the self.schema.

    Args:
      value: JSON-serializable object
    Returns:
      value, unchanged
    

            

`get_value_for_datastore`

Convert the Python object value into a string for the datastore.

            

        

    
