import random
import string

symbols = ['!', '#', '$', '%']

numletters = int(input("How many letters would you like?"))
numsymbols = int(input("How many symbols would you like?"))
numnums = int(input("How many numbers would you like?"))

password =[]

for i in range(numletters):
    password.append(random.choice(string.ascii_letters))

for j in range(numsymbols):
    password.append(random.choice(symbols))

for m in range(numnums):
    password.append(random.randint(0, 9))

random.shuffle(password)
s = ''.join(str(x) for x in password)
print(f"Your password is {s}")