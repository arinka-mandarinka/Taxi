from Lab2 import convert_int_to_str 

count = int(input('\nВведите количество сотрудников: '))

distances = []
for i in range(count):
    distances.append(int(input('Введите количество км до дома сотрудника ' + str(i + 1) + ': ')))

tariffs = []
for i in range(count):
    tariffs.append(int(input('Введите тариф для такси ' + str(i + 1) + ': ')))

taxis = []
sum = 0
for i in range(count):
    taxis.append(0)
for i in range(count):
    minD = distances.index(min(distances))
    maxT = tariffs.index(max(tariffs))
    taxis[minD] = maxT + 1
    sum += min(distances) * max(tariffs)
    distances[minD] = max(distances) + 1
    tariffs[maxT] = 0

print('\nСотрудник\tТакси')
for i in range(count):
    print(str(i + 1) + '\t\t' + str(taxis[i]))
print('\nМинимальная требуемая сумма с учетом введенных данных:', convert_int_to_str(sum))