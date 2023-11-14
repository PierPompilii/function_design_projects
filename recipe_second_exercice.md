1. describe the problem 

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

2.desing the function signature

```python

def improve_my_grammar():
    # paramenter:
    # a string = text
    # return 
    # words that start with capital and end with punctuation mark
    pass

3 - examples 

given a text starts without capital and punctuation mark
return false

improve_my_grammar (hello world) = false

given a text starts with capital but no punctuation mark
return false

improve_my_grammar (Hello world) = false

given a text with capital and punctuation mark

improve_my_grammar (Hello world!) => True 


