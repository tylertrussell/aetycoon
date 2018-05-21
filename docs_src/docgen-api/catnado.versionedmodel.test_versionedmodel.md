# 










## Classes
    
    
###`VersionUnifier`

 Common datastore ancestor for every version of a versioned model.
  Authoritative source of which version is active.
  

        
#### Class Functions
            
            
`inner_wrapper`


 
            

        

    
    
###`TestVersionedModelVersions`



        
#### Class Functions
            
            
`test_putting_new_version`


 
            
`test_creating_first_version`

 The first version should create a `VersionUnifier` to act as parent
    for all versions and automatically be set active. 
 
            
`test_private_put_doesnt_save_new_version`


 
            

        

    
    
###`SimpleAppEngineTestCase`



        
#### Class Functions
            
            
`tearDown`


 
            
`setUp`


 
            

        

    
    
###`TestVersionedModelParents`



        
#### Class Functions
            
            
`test_creating_versioned_model_with_parent_entity_or_key`

 Create datastore relationships using `parent` kwarg, access the feaux
    parent through parent() or parent_key() 
 
            
`test_versioned_model_parent_always_returns_active_version`


 
            

        

    
    
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
    
 
            

        

    
    
###`TestVersionedModelQueries`



        
#### Class Functions
            
            
`test_query_only_returns_active_version`


 
            
`test_all_versions_query`


 
            

        

    
    
###`SimpleEntity`

 A simple versioned model for testing. 

        
#### Class Functions
            
            

        

    
