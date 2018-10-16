import hashlib

def hashPassword():

    password = input("Password:")

    global hash

    hash = hashlib.sha512(password.encode('utf-8')).hexdigest()

    return print(hash)

hashPassword()

def checkPassword():

    check = input("Input the password:")

    hashpass = hashlib.sha512(check.encode('utf-8')).hexdigest()

    if hashpass == hash:
        print("Password correct!")

    else:
        print("Wrong password")

checkPassword()