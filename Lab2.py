def parse_two_digit_num(Dict1, Dict2, words, money):
    # Здесь работаем с Dict1 или Dict2
    if money % 100 < 20:
        words.append(Dict1[money % 100])
    else:
        words.append(Dict1[money % 10])
        money //= 10
        words.append(Dict2[money % 10 - 2])

# Парсим трехзначное число
def parse_three_digit_num(Dict1, Dict2, Dict3, words, money):
    # Применяем функцию parse_two_digit_num и добавляем Dict3
    parse_two_digit_num(Dict1, Dict2, words, money)
    money //= 100
    words.append(Dict3[money % 10 - 1])

def get_thousand(money):
    if money % 100 != 11 and money % 10 == 1:
        return "тысяча"
    elif not (money % 100 >= 12 and money % 100 <= 14) and (money % 10 >= 2 and money % 10 <= 4):
        return "тысячи"
    else:
        return "тысяч"

def get_rubles(money):
    if money % 100 != 11 and money % 10 == 1:
        return "рубль"
    elif not (money % 100 >= 12 and money % 100 <= 14) and (money % 10 >= 2 and money % 10 <= 4):
        return "рубля"
    else:
        return "рублей"

def change_end(words):
    for i in range(len(words)):
        match words[i]:
            case "один":
                words[i] = "одна"
                break        
            case "два":
                words[i] = "две"
                break            

def convert_int_to_str(money): 
    Dict1 = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать",
            "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    Dict2 = ["двадцать", "тридцать", "сорок", "пятьдесят",
            "шестьдесят", "семьдесять", "восемьдесят", "девяносто"]
    Dict3 = ["сто", "двести", "триста", "четыреста", "пятьсот",
            "шестьсот", "семьсот", "восемьсот", "девятьсот", ]
    
    words = []

    # Запоминаем является ли число больше тысячи
    isThousand = True if money >= 1000 else False
    # Запоминаем нужно ли нам менять падеж младшего разряда тысячи
    isOneOrTwo = True if isThousand and (money // 1000 % 10 == 1 or money // 1000 % 10 == 2) and \
                            (money // 1000 % 100 != 11 and money // 1000 % 100 != 12) else False

    # Добавляем слово рубль с правильным падежом
    words.append(get_rubles(money))

    while (money > 0):
        if money < 1000 and isThousand:
            # Добавляем слово тысяча в наш список с правильным падежом 
            words.append(get_thousand(money))

        # Работаем с сотнями
        if money % 1000 >= 100:
            parse_three_digit_num(Dict1, Dict2, Dict3, words, money)
        # Работаем с числом до 100 
        else: 
            parse_two_digit_num(Dict1, Dict2, words, money)

        money //= 1000

    # Переворачиваем список
    words.reverse()

    # При необходимости заменяем слово один/два на одна/две тысячи
    if isOneOrTwo:
        change_end(words)

    # Удаляем пустые строки
    words = list(filter(None, words))
    # Выводим как строку, первое слово с заглавной буквы
    return ' '.join(words).capitalize()