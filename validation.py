from passlib.hash import pbkdf2_sha256

hash = pbkdf2_sha256.hash(input("Input password: "))

if (pbkdf2_sha256.verify(input("Password: "), hash) == True):
    print("Password correct!")
else:
    print("Password incorrect.")