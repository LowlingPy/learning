# mahdi mohammadi khah 982011056

import re

def sign_changer(text):
    new_text = re.sub(r'[\s,.]', ':', text)
    return new_text


text = input()
text_with_change = sign_changer(text)
print(text_with_change)
