<h1 id="catnado.properties.key_property">catnado.properties.key_property</h1>


<h2 id="catnado.properties.key_property.KeyProperty">KeyProperty</h2>

```python
KeyProperty(self, *args, **kwargs)
```
A property that stores a key without automatically dereferencing it or
requiring a dependency between model classes.

`db.ReferenceProperty` performs a datastore RPC when it is accessed, which
can lead to unforeseen performance problems.

Furthermore, it needs to have the Kind specified when it is declared, which
creates a code dependency between models that can be undesirable.

`KeyProperty` helps alleviate these concerns.

<h3 id="catnado.properties.key_property.KeyProperty.validate">validate</h3>

```python
KeyProperty.validate(self, value)
```

Args:
  value: The value to validate.
Returns:
  A valid key.
Raises:
  TypeError if the value can't be converted into a `db.Key`
