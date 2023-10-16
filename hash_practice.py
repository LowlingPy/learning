# # just practice hashing
import bcrypt

password = b'123'

# Adding the salt to password
salt = bcrypt.gensalt()
x= salt
# Hashing the password
hashed = bcrypt.hashpw(password, x)

# printing the salt
print("Salt :")
print(salt)

# printing the hashed
print("Hashed")
print(hashed)

pw = input('enter pass: ')
bpw = pw.encode()
cp = bcrypt.checkpw(bpw, hashed)
print(cp)





#print("ramz :")
#x = input()
#z = bcrypt.hashpw(x,salt)
#if z==hashed :print("okaye")

# # Declaring our password

# import json
# password = 'akbar'
# hash_pw = hash(password)
# print(hash_pw)
# data_opened = open('testig_hash.txt', 'w+')
# save = json.dumps(hash_pw)
# data = data_opened.write(save)
# data_opened.close()


# import hashlib
# password = b'123'
# m = hashlib.sha256()
# m.update(password)