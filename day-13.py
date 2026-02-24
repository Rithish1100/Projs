'''try:
    age=int(input("How old are you?"))
except ValueError:
    print("You have enterd an invalid number try again with an numeric value")
    age=int(input("How old are you"))
if age>=18:
    print(f"you can drive at\n{age}.")'''
'''
word_per_page=0
pages=int(input("Number of pages:"))
word_per_page = int(input("Number of words per page:"))
total_words=(pages*word_per_page)
print(total_words)
'''
'''
import random
import maths

def mutate(a_list):
    b_list=[]
    new_item=0
    for item in a_list:
        new_item=item*2
        new_item+=random.randint(1,3)
        new_item=maths.add(new_item,item)
        b_list.append(new_item)
    print(b_list)
mutate([1,2,3,4,5,6])
'''
number=10
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print(f"{number}")
