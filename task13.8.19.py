count_of_tickets = int(input("Введите количество билетов: ")) #запрашиваем количество билетов у пользователя на мероприятие
visitors = count_of_tickets #заводим переменные
total_cost = 0


while visitors != 0: #обозначим условие, что количество билетов должо быть больше нуля
    age_of_visitors = int(input(f"Укажите возраст посетителя для билета № {visitors}? ")) #запрашиваем возраст посетителей для каждого билета
    if age_of_visitors < 18: #добавляем условие, если возраст меньше 18, то вход бесплатный
        print("Билет бесплатный")
    elif 18 <= age_of_visitors < 25: #условие возраст посетителя от 18 до 25, то цена 990 руб.
        total_cost += 990
        print("Цена билета: 990 рублей")
    else:                            #иначе возраст посетителя больше 25 и цена 1590 руб.
        total_cost += 1590
        print("Цена билета: 1590 рублей")
    visitors -= 1                    #повторяем для каждого посетителя, по циклу, пока количество не равно нулю

if count_of_tickets > 3:            #добавляем условие, при регистрации больше 3х посетителей, будет скидка
    discount = total_cost*0.9
    print(f"Общая сумма к оплате составит: {discount} рублей, с учетом скидки 10% при регистрации более 3х посетителей")
else:
    print(f"Общая сумма к оплате составит: {total_cost} рублей")