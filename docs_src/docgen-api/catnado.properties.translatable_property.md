# 




## Attributes
    
`FALLBACK_LANGUAGE`
    





## Functions
    
### `is_valid_iso639_language_code`

 Check a 2 letter ISO-639 language code is valid

  Args:
    language_code: 2 letter ISO-639 language code

  Returns:
    boolean indicating whether the language was found in pycountries.languages
  

    
    




## Classes
    
    
###`TranslatableStringProperty`

 A PickleProperty subclass intended to store translations of a string as a
  dictionary mapping two-letter language codes to Unicode translations:

  {
    'en': 'translation',
    'es': 'translation'
  }

  Validator checks each language key against ISO-639 and converts all key/value
  pairs to Unicode.
  

        
        
            

`make_value_from_datastore`



            

`validate`


    Raises:
      db.BadValueError: if any language code is invalid or any entry is not a
        string
    

            

        

    
    
###`InvalidLanguageError`

 Raised when a requested 2-letter language code cannot be found
  

        
        
            

        

    
    
###`MissingTranslationError`

 Raised when the requested language is missing
  

        
        
            

        

    
    
###`TranslationDictionary`

 A dictionary with convenience functions for fetching a translation.
  

        
        
            

`get_translation`

 Get the translation of the string in the given language.

    Args:
      model_instance: model instance this property is attached to
      language_code: str; an ISO-639 2 letter language code
      fallback: str; fallback language code (or True for English)

    Raises:
      MissingTranslationError: if a translation could not be found
      InvalidLanguageError: if `language_code` is not a valid ISO-639 2 letter
        language code

    Returns:
      unicode string
    

            

        

    
