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

## Tests
In order to run tests locally, you'll need to set an environment variable 
`APPENGINE_SDK_DIR` containing your Google App Engine SDK directory (which will
look something like `/your/path/to/google-cloud-sdk/platform/google_appengine`).

This environment variable allows `conftest.py` to add the required paths to 
`sys.path` so that the tests may run.


## Cats
They're pretty great.
