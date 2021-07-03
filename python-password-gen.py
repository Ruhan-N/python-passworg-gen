import string
from random import randint, choice

# validSpecialCharacters = ['!','@','#','$','&','<','>','?']
# characters = string.ascii_letters + string.digits + ''.join(validSpecialCharacters)0
characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(choice(characters) for x in range(32))
print(password)