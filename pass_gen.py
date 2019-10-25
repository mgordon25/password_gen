# randomly generated password from character list

import random

s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-=+"

pass_len = 8

p = "".join(random.sample(s, pass_len))

print(p)

