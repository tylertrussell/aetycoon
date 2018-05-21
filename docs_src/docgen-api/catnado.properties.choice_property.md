# 










## Classes
    
    
###`ChoiceProperty`

A property for efficiently storing choices made from a finite set.

  This works by mapping each choice to an integer.  The choices must be hashable
  (so that they can be efficiently mapped back to their corresponding index).
  

        
#### Class Functions
            
            
`c2i`

Converts a choice to its datastore representation.
 
            
`get_choices`

Gets a list of values which may be assigned to this property.
 
            
`make_value_from_datastore`


 
            
`get_value_for_datastore`


 
            

        

    
