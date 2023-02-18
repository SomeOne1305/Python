from termcolor import cprint, colored

# print('1+2+3+4+...+100 <= Shunga oxshash ifodalarni hisoblash dasturi.')
# print(
#     'e.g. "1" - birinchi son \n "100" - oxirgi son \n "2 - 1 = 1" - sonlar orasidagi farq'
# )
# a = colored(text="Hello", color="green")
# print(a)
# starter_num = int(input('Ifodaning birinchi sonini kiriting:'))
# end_num = int(input('Ifodaning oxirgi sonini kiriting:'))
# dif_num = int(input('Sonlar orasidagi farqni kiriting:'))

# def calculate(start, end, dif):
#     numbers = []
#     for num in range(start, end, dif):
#         numbers.append(num)
#     numbers.append(end)
#     result = sum(numbers)
#     print(*numbers, sep="+", end='=')
#     return cprint(result, color='green')

# if dif_num > end_num:
#     print('Oxirgi son va sonlar ustidagi farq mos emas.')
# else:
#     calculate(starter_num, end_num, dif_num)
Y = 'yes'
y = 'yes'
n = 'no'
N = 'no'

# class start:

#     def program():
#         print(
#             '1+2+3+4+...+100 <= Shunga oxshash ifodalarni hisoblash dasturi.')
#         print(
#             'e.g. "1" - birinchi son \n "100" - oxirgi son \n "2 - 1 = 1" - sonlar orasidagi farq'
#         )
#         a = colored(text="Hello", color="green")
#         print(a)
#         starter_num = int(input('Ifodaning birinchi sonini kiriting:'))
#         end_num = int(input('Ifodaning oxirgi sonini kiriting:'))
#         dif_num = int(input('Sonlar orasidagi farqni kiriting:'))

#         def calculate(start, end, dif):
#             numbers = []
#             for num in range(start, end, dif):
#                 numbers.append(num)
#             numbers.append(end)
#             result = sum(numbers)
#             print(*numbers, sep="+", end='=')
#             return cprint(result, color='green')

#         if dif_num > end_num:
#             print('Oxirgi son va sonlar ustidagi farq mos emas.')
#         else:
#             calculate(starter_num, end_num, dif_num)


def count():
    print('1+2+3+4+...+100 <= Shunga oxshash ifodalarni hisoblash dasturi.')
    print('e.g. "1" - birinchi son \n "100" - oxirgi son \n "2 - 1 = 1" - sonlar orasidagi farq')
    a = colored(text="Hello", color="green")
    print(a)
    starter_num = int(input('Ifodaning birinchi sonini kiriting:'))
    end_num = int(input('Ifodaning oxirgi sonini kiriting:'))
    dif_num = int(input('Sonlar orasidagi farqni kiriting:'))


    def calculate(start, end, dif):
        numbers = []
        for num in range(start, end, dif):
            numbers.append(num)
        numbers.append(end)
        result = sum(numbers)
        print(*numbers, sep="+", end='=')
        return cprint(result, color='green')


    if dif_num > end_num:
        print('Oxirgi son va sonlar ustidagi farq mos emas.')
    else:
        calculate(starter_num, end_num, dif_num)
count()
ask = input('Yana xohlaysizmi ? [y]-yes, [n]-no:  ') #in lines 26-27-28-29 y = 'yes', n = 'no' 
if ask == 'y':
    count()
else:
    cprint(" #" * 10 + '====  FINISH  ====' + '# ' * 10, color='cyan')
