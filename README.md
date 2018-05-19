# gae-catnado

A collection of useful Google App Engine datastore properties and helpers.

Forked from [aetycoon](https://github.com/Arachnid/aetycoon)
with additions and modifications.

**This package is a work-in-progress.** Most notably, the tests are incomplete.

## Setup
Install via `pip`
```
pip install gae-catnado
```

#### Requirements
[Google Cloud SDK](https://cloud.google.com/appengine/downloads).

#### Running tests
In order to run tests locally, you'll need to set an environment variable 
`APPENGINE_SDK_DIR` containing your Google App Engine SDK directory (which will
look something like `/your/path/to/google-cloud-sdk/platform/google_appengine`).

This environment variable allows `conftest.py` to add the required paths to 
`sys.path` so that the tests may run.

## `catnado.versionedmodel`
Rudimentary versioning system for Google App Engine and Cloud Datastore.

User classes inherit from `VersionedModel` to gain automatic versioning. 

Every call to `put` on an existing entity will create a new version of that
entity instead of overwriting it. Consequently, new versions must be marked
active deliberately via `set_active`.

```
class SimpleEntity(VersionedModel):
  name = db.StringProperty(required=True)

# create the first version, which automatically becomes active
foo = SimpleEntity(name='foo')
foo.put()

# editing an existing entity puts a new version
foo.name = 'bar'
bar = SimpleEntity.get(foo.put())

# but it won't be returned by queries until it's not active
SimpleEntity.all().filter('name', 'bar').get()  # None
foo.set_active()
SimpleEntity.all().filter('name', 'bar').get()  # bar

# we can view all versions of any instance, sorted by creation date
obj.all_versions().fetch(None)  # [foo, bar]
```

#### Datastore Indexes
Only the active version of any `VersionedModel` descendant is returned by
datastore queries. This is accomplished by overriding `VersionedModel.all`
to add a filter on the `active` property. Thus any indexes you create on 
`VersionedModel` descendants will need to start with `active`.

```
- kind: Cat
  properties:
  - name: active  # required because Cat descends from VersionedModel
  - name: name
  - name: age
    direction: desc
```

#### Datastore Ancestry
Every unique versioned entity shares a common `VersionUnifier` parent which
keeps track of the current version. 

Any version can access its unifier via `version_unifier`. `parent()` returns 
whatever parent was specified when creating the first version. If the specified 
parent is another instance of `VersionedModel`, then the active version of that
entity is returned.

```
parent_obj = SimpleEntity(name='foo')
parent_obj.put()

child_obj = SimpleEntity(name='child foo', parent=parent_obj)
child_obj.put()

""" Real Datastore Ancestry
- VersionUnifier
  - SimpleEntity(name='foo')
  - VersionUnifier
    - SimpleEntity(name='child foo')
"""

parent_obj.name = 'foo fighter'
parent_obj.put()
parent_obj.set_active()

child_obj.parent()  # foo fighter
```


## Cats
They're pretty great.
