per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} # процентные ставки для каждого банка

money = int(input("Введите сумму, которую Вы планируете положить под процент: ")) # ввод суммы пользователем
TKB = int((per_cent["ТКБ"])*(money/100)) # при условии
SKB = int((per_cent["СКБ"])*(money/100))
VTB = int((per_cent["ВТБ"])*(money/100))
SBER = int((per_cent["СБЕР"])*(money/100))

deposit = [TKB, SKB, VTB, SBER] # доход от депозита в каждом банке

print("Накопленные средства за год в каждом из представленных банков = ", deposit) #вывод накопленных средств для каждого банка

print("Максимальная сумма, которую Вы заработаете в одном из банков: ", max(deposit)) #максимально выгодный доход по депозиту
