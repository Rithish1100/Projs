import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H''I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','(',')','*','+']
print("welcome to py password generator")
nr_letters=int(input("how many letters u like in password\n"))
nr_symbols=int(input(f"how many symbols would u like\n"))
nr_numbers=int(input(f"how many numbers would u like \n "))
a=0
c=[]
for i in range (0,nr_letters):
    a=random.randint(0,52)
    c+=letters[a]
# print(c)

for i in range (0,nr_symbols):
    a=random.randint(0,9)
    c+=numbers[a]
# print(c)

for i in range (0,nr_numbers):
    a=random.randint(0,8)
    c+=symbols[a]
# print(c) actual output

random.shuffle(c)
# print(c) rearranged output
password=''
for i in  c:
    password+=i
print(f"your password is:{password}")
