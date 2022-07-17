# 1 loop kad daugiau output butu ir duot useriui isjungt
# kada nori paklaus ar nori baigt ar nori generuot dar +++

# 2 pasirinkt kuriuos simbolius (ne)deti pvz nedeti !@#$% ar skaiciu ir t.t +++

# 3 patikrinti kad tikrai iraso int o ne kazka kitka +++

# 4 storintu visus pass i kazkoki isorini dok pvz .txt +++

# 5 encryption/decryption pvz  storina i .txt faila
# encryptinta pass, kuri istraukus programa decryptintu +++

# 6 paziuri ar panaudotas pass

# 7 pasiziureti hashinima/saltinima

# 8 loginima - ivykio aprasymas, ip is kur atsidare ir t.t

# is kokiu simboliu sugeneruoja pass > input with loop > ... +++

# turbut reikes datetime

# import hashlib (de/encryption)

# def int inpt function uses 12 lines instead of 28.
# easy to manipulate the code, easy to reuse.
# compartmentalization: funcion and flow
# kiekviena funkcija turi savo tam tikrai atskira flow


import datetime
import string
import random
import os
from cryptography.fernet import Fernet

letters = list(string.ascii_letters)
numbers = list(string.digits)
spec_char = list("!@#$%^&*()")
characters = letters + numbers + spec_char


def get_key():
    if os.path.exists("keyfile.txt"):
        with open("keyfile.txt", "rb") as f:
            key = f.read()
    else:
        key = Fernet.generate_key()
        with open("keyfile.txt", "wb") as f:
            f.write(key)
    return key


def get_int_inpt(message):
    while True:
        try:
            user_inpt = int(input(message))
        except ValueError:
            print("Invalid input, please input a number. ")
        else:
            return user_inpt


def generate_password():
    length = get_int_inpt("Enter password length: ")
    letters_count = get_int_inpt("Enter alphabets count in password: ")
    numbers_count = get_int_inpt("Enter digits count in password: ")
    spec_char_count = get_int_inpt(
        "Enter special characters count in password: ")
    characters_count = letters_count + numbers_count + spec_char_count

    if characters_count > length:
        print("Characters total count is greater than password length")
        return

    password = []

    for i in range(letters_count):
        password.append(random.choice(letters))

    for i in range(numbers_count):
        password.append(random.choice(numbers))

    for i in range(spec_char_count):
        password.append(random.choice(spec_char))

    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(letters))
        print("".join(password))
    random.shuffle(password)
    password = "".join(password)
    print(password)
    encrypted_passw = encrypt_pass(password, get_key())

    print(encrypted_passw.decode())

    with open("passwords.txt", "a") as f:
        f.write(encrypted_passw.decode())
        f.write("\n")


def gen_pass_flow():
    while True:
        generate_password()

        while True:
            continue_loop = str(input("Continue? Y/N: ")).lower()
            if continue_loop == "y" or continue_loop == "n":
                break
            print("Input is incorrect, input y or n. ")

        if continue_loop == "n":
            break


def encrypt_pass(plaintext, key):
    fernet = Fernet(key)
    ciphertext = fernet.encrypt(plaintext.encode())
    return ciphertext


def decrypt_pass(ciphertext, key):
    fernet = Fernet(key)
    plaintext = fernet.decrypt(ciphertext).decode()
    return plaintext


while True:
    print("1: passsword generator\n2: Decrypt\n3: quit")
    while True:
        selection = get_int_inpt("")
        if selection not in [1, 2, 3]:
            print("Please input a valid selection:")
        else:
            break
    if selection == 1:
        gen_pass_flow()
    elif selection == 2:
        ciphertext = input("Enter the encrypted password").encode()
        key = get_key()
        plaintext = decrypt_pass(ciphertext, key)
        print(plaintext)
    else:
        print("Exiting")
        break

path = "passwords.txt"

timestamp = os.path.getmtime(path)
datestamp = datetime.datetime.fromtimestamp(timestamp)

print('Modified Date/Time:', datestamp)

c_timestamp = os.path.getctime(path)
c_datestamp = datetime.datetime.fromtimestamp(c_timestamp)

print('Created Date/Time on:', c_datestamp)

with open("log.txt", "w") as f:
    f.write("Modified datetime: {}".format(datestamp))