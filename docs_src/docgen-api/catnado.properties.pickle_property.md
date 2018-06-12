# 










## Classes
    
    
###`PickleProperty`

Property for storing complex objects in the datastore in pickled form.

        
        
            

`default_value`

If possible, copy the value passed in the default= keyword argument.

    This prevents mutable objects such as dictionaries from being shared across
    instances.
    

            

`make_value_from_datastore`

Pickle data to store it.

            

`get_value_for_datastore`

Un-pickle data from the datastore.

            

        

    
