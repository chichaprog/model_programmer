import hashlib
import os
import base64
salt = os.urandom(32)

password = input("Enter password ").encode()
#password = 'mouse_15964_dfeh_6732'.encode() # Превращаем строку в последовательность байтов 
dk = hashlib.pbkdf2_hmac('sha512', password, salt,10)
hashed_password_b64 = base64.b64encode(dk).decode()
salt_b64 = base64.b64encode(salt).decode()
print(hashed_password_b64)
print(salt_b64)
file = open('my_hash.txt','w') 
file.write(hashed_password_b64 + "\n")
file.write(salt_b64)
file.close()