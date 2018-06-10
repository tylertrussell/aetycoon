# gae-catnado

***This is a work in progress subject to sudden change.***

A collection of useful properties and helpers for use with Google App Engine.

Install with pip: `pip install gae-catnado`.

See the [docs on GitHub](https://tylertrussell.github.io/gae-catnado).

# Changelog

### 0.0.1dev14
* Unit tests for `catnado.utils.validators`

### 0.0.1dev13
* Updates to `catnado.utils.validators`

### 0.0.1dev12
* Added `catnado.utils.api` and `catnado.handlers.service_api_handler`; helpers 
for making secure API calls and building API handlers that validate requests are
coming from another service within the same application.
* Added `catnado.utils.validators`
* Added `flake8-docstrings-catnado` and related bits and pieces

> "we've traced the call... it's coming from inside the house!"

### 0.0.1dev11
* Added `JSONProperty` and basic unit tests
    * A way to store JSON data validated by a [JSON Schema](http://www.json-schema.org) (draft 3 or 4)
    * This new property adds the new pip requirement [`jsonschema`](https://github.com/Julian/jsonschema)
