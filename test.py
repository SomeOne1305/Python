print("Bu n sondan m songacha bolgan sonlar yig'indisini hisoblash dasturi.");
print('1+2+3+4+ ... + 100 ==> e.g birinchi son bunda 1');

def calculate():
    starterNumber = int(input('Ifodadagi birinchi sonni kiriting:'))
    EndNumber = int(input('Oxirgi sonni kiriting:'))
    differenceBtwNum = int(input('Sonlar orasidagi farqni kiriting:'))
    if differenceBtwNum > EndNumber:
	    EOFError 

    listOfnumbers = []
    for num in range(starterNumber, EndNumber, differenceBtwNum):
        listOfnumbers.append(num);
    result = sum(listOfnumbers) + EndNumber
    print("Javob:", result)
    return result
calculate()
print('Yana ishlashni xohlaysizmi ?')
print('Iltimos kichik harflarda "ha" yoki yoq javoblarini bering')
ask = input('Javobingiz:')
if ask == 'ha':
	calculate()
else:
	print( '='*30 + ' FINISH ' + '='*30)
	
