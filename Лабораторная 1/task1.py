numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
s = 0
for k in numbers:
    if k!=None:
        s = s + k
h=s/len(numbers)
for i in  range (len(numbers)):
    if numbers[i] is None:
        numbers[i]=h

print("Измененный список:", numbers)
