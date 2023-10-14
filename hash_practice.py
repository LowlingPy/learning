# # just practice hashing
# import bcrypt
#
# password = b'123'
#
# # Adding the salt to password
# salt = bcrypt.gensalt()
# # Hashing the password
# hashed = bcrypt.hashpw(password, salt)
#
# # printing the salt
# print("Salt :")
# print(salt)
#
# # printing the hashed
# print("Hashed")
# print(hashed)
# # Declaring our password

# import json
# password = 'akbar'
# hash_pw = hash(password)
# print(hash_pw)
# data_opened = open('testig_hash.txt', 'w+')
# save = json.dumps(hash_pw)
# data = data_opened.write(save)
# data_opened.close()

import hashlib
password = b'123'
m = hashlib.sha256()
m.update(password)