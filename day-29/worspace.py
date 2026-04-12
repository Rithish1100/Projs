# try:
#     file=open("a_file.txt")
#     a_dictonary={"key":"value"}
#     print(a_dictonary["key"])
# except FileNotFoundError:
#     file=open("a_file.txt","w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"This vlaue{error_message}is not found")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is not an error but it is by me")

height=float(input("Height:"))
weight=int(input("Weight:"))
height=height/100

if height>3:
    raise ValueError("Human height is not >3 meters")

bmi=weight+height**2
print(bmi)

