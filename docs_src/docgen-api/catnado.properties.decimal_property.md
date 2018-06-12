# 










## Classes
    
    
###`DecimalProperty`

Property for storing Decimal types.

        
        
            

`make_value_from_datastore`

Convert str from datastore back to Decimal.

            

`validate`

Validator.

    Args:
      value: either a string or Decimal
    Returns:
      Decimal
    Raises:
      db.BadValueError: if value is not a Decimal or valid string
    

            

`get_value_for_datastore`

Convert Decimal to str for datastore.

            

        

    
