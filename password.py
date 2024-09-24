import random
import string
def main():
    length = int(input("Enter the length of the password: "))
    print(generate_password(length))


def generate_password(length):

    uppercase = string.ascii_uppercase  # A-Z
    lowercase = string.ascii_lowercase  # a-z
    digits = string.digits              # 0-9
    special_chars = string.punctuation  # !@#$%^&*() etc.

    pool = uppercase + lowercase + digits + special_chars
    
    password = []
                       
    for _ in range(length):
        password.append( random.choice(pool) )
        

    return ''.join(password)  #This joins all the randomly selected characters together into a single string.


if __name__=="__main__":
    main()