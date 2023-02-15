print('1+2+3+4+...+100 <= Shunga oxshash ifodalarni hisoblash dasturi.')
print('e.g. "1" - birinchi son \n "100" - oxirgi son \n "2 - 1 = 1" - sonlar orasidagi farq')

starter_num = int(input('Ifodaning birinchi sonini kiriting:'))
end_num = int(input('Ifodaning oxirgi sonini kiriting:'))
dif_num = int(input('Sonlar orasidagi farqni kiriting:'))

def calculate(start, end, dif):
    numbers = []
    for num in range(start, end, dif):
        numbers.append(num)
    result = sum(numbers)
    return print('Javob:', result)    
if dif_num > end_num :
    print('Oxirgi son va sonlar ustidagi farq mos emas.')
else:
    calculate(starter_num, end_num, dif_num)