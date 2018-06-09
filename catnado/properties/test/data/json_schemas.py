"""
Example schemas adapted from http://json-schema.org/examples.html.

Since the jsonschema Python package available through PyPi currently only
supports Draft 4, see these docs:
- http://json-schema.org/draft-04/json-schema-core.html
- http://json-schema.org/draft-04/json-schema-validation.html
"""


GEO = {
  'description': 'A simple geographical coordinate',
  'type': 'object',
  'properties': {
    'latitude': {'type': 'number'},
    'longitude': {'type': 'number'},
  },
  'additionalProperties': False,
  'required': ['latitude', 'longitude']
}


ADDRESS = {
  'description': 'An Address following the convention of http://microformats.org/wiki/hcard',
  'type': 'object',
  'properties': {
    'post-office-box': {'type': 'string'},
    'extended-address': {'type': 'string'},
    'street-address': {'type': 'string'},
    'locality': {'type': 'string'},
    'region': {'type': 'string'},
    'postal-code': {'type': 'string'},
    'country-name': {'type': 'string'},
  },
  'additionalProperties': False,
  'required': ['locality', 'region', 'country-name'],
  'dependencies': {
    'post-office-box': ['street-address'],
    'extended-address': ['street-address'],
  }
}
