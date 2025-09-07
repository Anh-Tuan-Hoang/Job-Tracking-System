import random
import string

def random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_float(min_val, max_val):
    return round(random.uniform(min_val, max_val), 2)
