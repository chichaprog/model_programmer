#This programm is old and it for password.

#password
import hashlib
import base64
salt = 'Ваша соль'.encode()
file = open("my_hash.txt","r")
hash = file.readline() 
salt = file.readline() 
salt = base64.b64decode(salt)
print (salt)
print(hash)
file.close()
print(hash)

s = '0123456789qwertyuiopasdfghjklzxcvbnm' 
#s = "0123456789"
cont = True
for c1 in s:
    if cont:
        for c2 in s:
            if cont:
                for c3 in s:
                    if cont:
                        for c4 in s:
                            password = (c4 + c3 + c2 + c1).encode()
                            dk = hashlib.pbkdf2_hmac('sha512', password, salt, 10)

                            print(password)
                            hashed_password_b64 = base64.b64encode(dk.decode()).decode()
                            if hash == hashed_password_b64:
                                cont = False
                                print("пароль совпал",password)
                                print(password.decode())
                                break
print("перебор закончен")