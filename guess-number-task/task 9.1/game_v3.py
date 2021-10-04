"""Игра угадай число v3.0
Компьютер загадывает, а алгоритм угадывает число"""


import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    min_number = 1 # Устанавливаем минимальную границу
    max_number = 100 # И максимальную границу для первой итерации
    count = 0
    
    while True:
        
        count += 1
        # Предположили число из установленного диапазона:
        suggested_number = np.random.randint(min_number, max_number + 1)
        
        if suggested_number > number:
            max_number = suggested_number # Уточняем верхнюю границу
            
        elif suggested_number < number:
            min_number = suggested_number # Уточняем нижнюю границу
            
        else:
            return count

        
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


score_game(random_predict)