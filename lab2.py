# # a = "12"
# # list_roba = []
# # while a.isnumeric():
# #     a = input("metti: ")
# #     if a.isnumeric():
# #         list_roba.append(int(a))
# #
# # print("min", min(list_roba))
# # print("max", max(list_roba))
# #
# # print(list_roba[0])
# # for i in range(1, len(list_roba)):
# #     print(list_roba[i] + list_roba[i - 1])
# #
# # for i in range(1, len(list_roba)):
# #     if list_roba[i] == list_roba[i - 1]:
# #         print(list_roba[i])
#
# strngazza = input("Metti: ")
#
# for i in strngazza:
#     if i.isupper():
#         print(i)
#
#
# print(strngazza[1::2])
#
# listazza = list(strngazza)
# lista= []
# for i in listazza:
#     if i in ['a', 'e', 'i', 'o', 'u']:
#         lista.append("_")
#     else:
#         lista.append(i)
# print("".join(lista))
#
# num = 0
# for i in strngazza:
#     if i.isdigit():
#         num = num + 1
# print(num)
#
# for i in range(len(strngazza)):
#     if strngazza[i] in ['a', 'e', 'i', 'o', 'u']:
#         print(i)

# num = int(input("NUmero:"))
#
# for i in range(num):
#     print("* " * num)
# lista = list(range(1, num*2, 2))
# for i in range(num):
#     print("  " * (num - i), "* " * (lista[i]))
# for i in range(num-1).__reversed__():
#     print("  " * (num - i), "* " * (lista[i]))

# strn =  input("string")
# print(strn[::-1])


# numello = int(input("numello > 1:"))
# flag = False
# for num in range(2, numello):
#     flag = False
#     for i in range(2, num):
#         flag = False
#         if num % i == 0:
#             break
#         else:
#             flag = True
#     if flag:
#         print(num)
import itertools

strinf = input("Stringa:")
listone = []
for i in range(0, len(strinf)):
    for a in range(i+1, len(strinf) + 1):
        listone.append(strinf[i:a:1])
listone.remove(strinf)
listone.sort()
for i in sorted(listone, key=len):
    print(i)
