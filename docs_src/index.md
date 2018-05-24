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
In order to run tests locally, you'll need to:

- set an environment variable `APPENGINE_SDK_DIR` containing your Google App 
Engine SDK directory (which will end in `/platform/google_appengine`)

- call `catnado.utils.environment.setup_cloud_sdk_paths` during test startup

The provided `conftest.py` will perform required setup for the `pytest` test runner.

## Cats
They're pretty great.
