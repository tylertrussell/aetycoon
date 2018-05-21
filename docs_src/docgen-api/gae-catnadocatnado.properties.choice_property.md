# 










## Classes
    
    
###`ChoiceProperty`

A property for efficiently storing choices made from a finite set.

  This works by mapping each choice to an integer.  The choices must be hashable
  (so that they can be efficiently mapped back to their corresponding index).

  Example usage:

  >>> class ChoiceModel(db.Model):
  ...   a_choice = ChoiceProperty(enumerate(['red', 'green', 'blue']))
  ...   b_choice = ChoiceProperty([(0,None), (1,'alpha'), (4,'beta')])

  You interact with choice properties using the choice values:

  >>> model = ChoiceModel(a_choice='green')
  >>> model.a_choice
  'green'
  >>> model.b_choice == None
  True
  >>> model.b_choice = 'beta'
  >>> model.b_choice
  'beta'
  >>> model.put() # doctest: +ELLIPSIS
  datastore_types.Key.from_path(u'ChoiceModel', ...)

  >>> model2 = ChoiceModel.all().get()
  >>> model2.a_choice
  'green'
  >>> model.b_choice
  'beta'

  To get the int representation of a choice, you may use either access the
  choice's corresponding attribute or use the c2i method:
  >>> green = ChoiceModel.a_choice.GREEN
  >>> none = ChoiceModel.b_choice.c2i(None)
  >>> (green == 1) and (none == 0)
  True

  The int representation of a choice is needed to filter on a choice property:
  >>> ChoiceModel.gql("WHERE a_choice = :1", green).count()
  1
  

    
