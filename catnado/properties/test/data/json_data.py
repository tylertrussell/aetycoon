

GOOD_GEO_DATA = [
  {'latitude': 0.25, 'longitude': 0.15},
]


BAD_GEO_DATA = [
  {'latitude': '0.25', 'longitude': '0.15'},
]


GOOD_ADDRESS_DATA = [
  {
    'street-address': '1234 Made-Up Lane',
    'extended-address': 'Department of Software Testing',
    'locality': 'San Francisco',
    'region': 'CA',
    'postal-code': '94108',
    'country-name': 'USA'
  },
]


BAD_ADDRESS_DATA = [
  {  # missing country
    'street-address': '1234 Made-Up Lane',
    'extended-address': 'Department of Disguised Felines',
    'locality': 'San Francisco',
    'region': 'CA',
    'postal-code': '94108',
  },
]
