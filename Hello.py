# print("Hello")
# lst = []
# while True:
#     input1 = input("Enter the input:- ")

#     if input1=="s":
#         break
#     lst.append(input1)
# print(lst)


str = "1,2,3,4,5"

str1 =" "

for i in str:

    if i == ",":
        continue
    str1 += i
print(str1)    

print("swathi areu doing something that is not required any more")
str3 = "swathi, naresh"
res = str3.removeprefix(1)
print(res, "result")