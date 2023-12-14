#Описать функию AddLeftDigit(D, K), добавляющую к целому положительному числу K слева цифру D (D — входной параметр целого типа, лежащий в диапазоне 1-9, K — параметр целого типа, являющийся одновременно входным и выходным).
#С помощью этой функции последовательно добваить к данному числу слева данные цифры D1 и D2, ВЫВОДЯ результат каждого добавления.
def AddLeftDigit(D, K):
    K = str(K)
    new_num = str(D) + K
    print(new_num)

while True:
    try:
        D = int(input('D (1 - 9): '))
        K = int(input("K: "))
        if D > 9:
            raise ValueError

        D1 = int(input('D1 (1-9): '))
        AddLeftDigit(D, K)
        if D1 > 9:
            raise ValueError
        D2 = int(input('D2 (1-9): '))
        if D2 > 9:
            raise ValueError
        AddLeftDigit(D1, K)
        break
    except ValueError:
        print('error')

