import random
import string
def generate_password(len):
    letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits="0123456789"
    spl_chrs="!@#$%^&*|\?"
    all_chrs=letters+digits+spl_chrs
    if length < 4:
        print("Password length should be at least 4 character")
    else:
        password ="". join(random.choice(all_chrs)
                       for  i in range(length))
        return password
if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    print("Generated password:", generate_password(len))
