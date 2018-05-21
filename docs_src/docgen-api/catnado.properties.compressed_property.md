# 










## Classes
    
    
###`CompressedProperty`

An unindexed, compressed property.

  CompressedTextProperty and CompressedBlobProperty derive from this class.
  

        
        
            

`make_value_from_datastore`



            

`value_to_str`

Returns the value stored by this property encoded as a (byte) string,
    or None if value is None.  This string will be stored in the datastore.
    By default, returns the value unchanged.

            

`get_value_for_datastore`



            

        

    
    
###`CompressedTextProperty`

A string that will be stored in a compressed form (encoded as UTF-8).
  

        
        
            

`value_to_str`



            

        

    
    
###`CompressedBlobProperty`

A byte string that will be stored in a compressed form.
  

        
        
            

        

    
