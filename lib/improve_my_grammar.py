import re
# def improve_my_grammar(text):
#     result = re.search(r"^[A-Z]+[a-z]+[\s]+[a-z]+[\.!\?]$", text)
#     return result is not None
    
    
def improve_my_grammar(text):
    # Check if the first letter is a capital.
    first_letter = text[0]
    last_letter = text[-1]
    capitalised =  first_letter == first_letter.upper()
    punctuated = last_letter in '?.!'

    return capitalised and punctuated
    # Check if the final letter is a punctuation