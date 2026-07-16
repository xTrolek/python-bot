import random
import string
def gen_pass(pass_length):
    elements = string.ascii_letters + string.digits
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
