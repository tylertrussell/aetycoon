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
    
    
###`VersionUnifier`

Common datastore ancestor for every version of a versioned model.

  Authoritative source of which version is active.
  

        
        
            

`inner_wrapper`



            

        

    
    
###`VersionedModel`

Model with built-in versioning.

  Each entity represents a single version and all versions share a common
  `VersionUnifier` datastore parent.
  

        
        
            

`parent`

Get this entity's feaux datastore parent.

    To get the entity's underlying datastore parent (a `VersionUnifier`, use
    `version_unifier`.

    Returns:
      Datastore entity.
    Raises:
      The entity is loaded using `google.appengine.ext.db.get` which can raise
      exceptions (`KindError`?) if the Parent's Kind is not imported.
    RPC Cost:
      2x fetch-by-key if parent is `VersionedModel` descendant
      1x fetch-by-key otherwise
    

            

`all_versions`

Get a query for all of the versions of the given instance.

    Query ordered by ascending creation date.

    Args:
      instance: Any instance of any `VersionedModel` subclass.
    Returns:
      google.appengine.ext.db.Query
    

            

`put`

Put a new version of this model to the datastore.

    Iff this is a new model, create a new `VersionUnifier` to track all of its
    versions.

    Args:
      Keyword args passed to super call
    Returns:
      `db.Key` for the newly-put version
    

            

`parent_key`

See `parent`.

    Returns:
      The `db.Key` of this entity's feaux parent.
    RPC Cost:
      1x fetch-by-key if parent is `VersionedModel` descendant
      Free otherwise
    

            

`set_active`

Transactionally activate this version.

    Args:
      info: optional `dict` of info to record with the change
    

            

        

    
