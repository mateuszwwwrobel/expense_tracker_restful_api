from passlib.hash import pbkdf2_sha512


def hash_password(password):
    salt = 'Gb89b283dNmOa'
    salted_password = password + salt
    return pbkdf2_sha512.hash(salted_password)


def check_password(password, hashed):
    return pbkdf2_sha512.verify(password, hashed)
