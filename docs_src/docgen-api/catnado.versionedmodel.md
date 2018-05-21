# 




## Attributes
    
`EVENT_TYPE_CHANGED_ACTIVE_VERSION`
    
`ERROR_WRONG_VERSION_PARENT`
    
`ERROR_WRONG_PARENT_TYPE`
    
`ERROR_MISSING_VERSION_UNIFIER`
    
`EVENT_DATA_OLD_ACTIVE_VERSION`
    
`EVENT_KEY`
    
`EVENT_DATA_TIMESTAMP`
    
`EVENT_DATA_NEW_ACTIVE_VERSION`
    







## Classes
    
    
###`KeyProperty`

A property that stores a key without automatically dereferencing it or
  requiring a dependency between model classes.

  `db.ReferenceProperty` performs a datastore RPC when it is accessed, which
  can lead to unforeseen performance problems.

  Furthermore, it needs to have the Kind specified when it is declared, which
  creates a code dependency between models that can be undesirable.

  `KeyProperty` helps alleviate these concerns.
  

        
#### Class Functions
            
            
`validate`


    Args:
      value: The value to validate.
    Returns:
      A valid key.
    Raises:
      TypeError if the value can't be converted into a `db.Key`
    
 
            

        

    
    
###`VersionUnifier`

 Common datastore ancestor for every version of a versioned model.
  Authoritative source of which version is active.
  

        
#### Class Functions
            
            
`inner_wrapper`


 
            

        

    
    
###`PickleProperty`

A property for storing complex objects in the datastore in pickled form.
  

        
#### Class Functions
            
            
`default_value`

If possible, copy the value passed in the default= keyword argument.
    This prevents mutable objects such as dictionaries from being shared across
    instances.
 
            
`make_value_from_datastore`


 
            
`get_value_for_datastore`


 
            

        

    
    
###`datetime`

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints or longs.


        
#### Class Functions
            
            

        

    
    
###`VersionedModel`

 Model with built-in versioning. Each entity represents a single version
  and all versions share a common `VersionUnifier` datastore parent.
  

        
#### Class Functions
            
            
`parent`

 Get this entity's feaux datastore parent (as opposed to its real parent
    which is a `VersionUnifier`).

    Returns:
      Datastore entity.
    Raises:
      The entity is loaded using `google.appengine.ext.db.get` which can raise
      exceptions (`KindError`?) if the Parent's Kind is not imported.
    RPC Cost:
      2x fetch-by-key if parent is `VersionedModel` descendant
      1x fetch-by-key otherwise
    
 
            
`all_versions`

 Get a query that will fetch all of the versions of the given instance of
    VersionedModel, ordered by their ascending creation date.

    This function requires the following datastore index

    kind: VersionedModel
    properties:
      - name: version_unifier_key
        direction: asc

    Args:
      instance: Any instance of any `VersionedModel` subclass.
    Returns:
      google.appengine.ext.db.Query
    
 
            
`put`

 Put a new version of this model to the datastore. Iff this is a new
    model, create a new `VersionUnifier` to track all of its versions.
    Args:
      Keyword args passed to super call
    Returns:
      `db.Key` for the newly-put version
    
 
            
`parent_key`

 See: `parent`.

    Returns:
      The `db.Key` of this entity's feaux parent.
    RPC Cost:
      1x fetch-by-key if parent is `VersionedModel` descendant
      Free otherwise
    
 
            
`set_active`

 Transactionally activate this version.

    Args:
      info: optional `dict` of info to record with the change
    
 
            

        

    
