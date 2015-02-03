### Utils

Some utility functions I create for little tasks.

#### replace_non_ascii

Function to replace tipycal spanish characters such as accents and ñ to create variable names from strings.
Example:

```python
var = "Coño, tengo ácéntós"
new_var = replace_spanish_alphabet(var)
print new_var #u'conTILDEocCOMMA_tengo_aCuteceCutentoCutes'
reversed_new_var = replace_spanish_alphabet(var, new_var)
print reversed_new_var #Coño, tengo ácéntós
```

#### timers

Function to repeat periodically another function

```python
def print_hw():
    print "hola mundo"
repeat_func(print_hw, 1)
```
