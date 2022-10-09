from Lab2 import convert_int_to_str 

# Проверка на ввод положительного числа.
def check_input_int(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print('Ошибка: неверно введено значение! Попробуйте ещё раз...')
            continue
        if num<1:
            print('Ошибка: число должно быть положительным! Попробуйте ещё раз...')
            continue
        return num

count = int(input('\nВведите количество сотрудников: '))

# Добавление данных в списки.
distances = []
for i in range(count):
    distances.append(check_input_int('Введите количество км до дома сотрудника ' + str(i + 1) + ': '))

tariffs = []
for i in range(count):
    tariffs.append(check_input_int('Введите тариф для такси ' + str(i + 1) + ': '))

taxis = []
sum = 0

# Заполняем список нулями, чтобы была возможность обратиться к любому элементу.
for i in range(count):
    taxis.append(0)

for i in range(count):
    # Ищем индекс минимальной дистанции и максимального тарифа.
    minD = distances.index(min(distances))
    maxT = tariffs.index(max(tariffs))
    
    # Записываем номер такси на индекс сотрудника в списке.
    taxis[minD] = maxT + 1

    # Считаем сумму выбранного варианта.
    sum += min(distances) * max(tariffs)

    # Записываем значения для дальнейшего игнорирования элементов.
    distances[minD] = max(distances) + 1
    tariffs[maxT] = 0

# Вывод результатов.
print('\nСотрудник\tТакси')
for i in range(count):
    print(str(i + 1) + '\t\t' + str(taxis[i]))
print('\nМинимальная требуемая сумма с учетом введенных данных:', convert_int_to_str(sum))