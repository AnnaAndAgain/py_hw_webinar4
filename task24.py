# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод —
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

# Итого у нас на входе круг из N кустов черники и случайная урожайность каждого куста.
# N буду запрашивать у пользователя, урожайность генерировать в пределах 50 ягод на куст.


def create_garden():
    # огород у нас будет списком, чтобы по индексам можно было различать
    # кусты и находить соседние

    N = int(input("Сколько кустов черники на грядке? "))
    import random as rd
    tmp_list = [rd.randint(0, 51) for i in range(N)]
    #print(tmp_list)
    return tmp_list


def find_best_place(tmp_garden_bed):
    # считаем кол-во ягод, которая соберет собиралка в каждой позицц
    num_bushes = len(tmp_garden_bed)
    tmp_berries = [(tmp_garden_bed[0]+tmp_garden_bed[1]+tmp_garden_bed[-1])] # в эл. 0 - сумма кустов 0, 1 и последнего
    for i in range (1, num_bushes-1): # для остальных кустов, кроме последнего, - их с соседями урожай
        tmp_berries.append(tmp_garden_bed[i]+tmp_garden_bed[i+1]+tmp_garden_bed[i-1])
    # и для последнего отдельно, чтобы не выйти за индексы
    tmp_berries.append(tmp_garden_bed[num_bushes-1] + tmp_garden_bed[num_bushes - 2] + tmp_garden_bed[0])
    # print(tmp_berries)
    # получился список, где индексы соответсвуют "номерам" кустов, а значения -- кол-ву ягод
    # с соответствующего и соседнего с ним кустов
    # ищем максимальный урожай
    result = max(tmp_berries)
    # print(result)
    return result


list_garden_bed = create_garden() # высаживаем чернику
print(list_garden_bed)

best_crop = find_best_place(list_garden_bed) # находим самый успешный урожай за один сбор
print(best_crop)
