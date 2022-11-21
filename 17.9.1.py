n = list(map(int,input('Введите количество чисел в последовательности через пробел: ').split())) #На вход подается последовательность чисел через пробел
number = (int(input("Введите любое число: "))) #Просим пользователя ввести любое число


for i in range(0, len(n)): #Сортировка алгоритмом вставки по возрастанию
    x = n[i]
    idx = i # определяем число для сортировки
    while idx > 0 and n[idx-1] > x: #запускаем цикл с условием
        n[idx] = n[idx-1]
        idx -= 1
    n[idx] = x
print("Сортированный список по возрастанию: ", n) #Выводим сортированный список


def binary_search(n, number, left, right): #Сортируем с помощью двоичного поиска и устанавливаем позицию введенного элемента
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if n[middle] == number: #определяем середину списка
            return middle
        elif number < n[middle]:
            return binary_search(n, number, left, middle-1)
        else:
            return binary_search(n, number, middle+1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.' #Используем конструкцию try-except, чтобы предупредить об ошибке при выходе за верхнюю границу диапазона

if not binary_search(n,number, 0, len(n)):
    n_1 = min(n, key=lambda x: (abs(x - number), x)) #оценивается абсолютная разница между элементом и числом, и можно видеть число, которое ближе всего к введенному пользователем
    ind = n.index(n_1)
    max_ind = ind + 1
    min_ind = ind - 1
    if n_1 < number:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {n_1}, его индекс: {ind}
Ближайший больший элемент: {n[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {n_1}, его индекс: {n.index(n_1)}
В списке нет меньшего элемента''')
    elif n_1 > number:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {n_1}, его индекс: {n.index(n_1)}
Ближайший меньший элемент: {n[min_ind]}, его индекс: {min_ind}''')
    elif n.index(n_1) == 0:
        print(f'Индекс введенного элемента: {n.index(n_1)}')
else:
    print(f'Индекс введенного элемента: {binary_search(n, number, 0, len(n))}')


