import numpy as np

def game_core_v3(number: int=1) -> int:
    """
    Алгоритм угадывает число от 1 до 100, путем генерации случайных чисел и
      сравнения их с зегаданным до совпадения.
    Уменьшение количества попыток за счет установки ограничителей генерации случайного
      числа. Из значений меньше загаданного вибирается наибольшее для нижней границы,
      а из значений больше выбирается наименьшее для верхней.


    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    min = 1
    max = 101

    np.random.seed(1)  # Фиксируем сид для воспроизводимости
    predict = np.random.randint(min, max) # Случайное число в установленных границах

    while number != predict:
        count += 1

        # В PEP 8 есть рекомендация не выделять пробелами операторы в "if" с несколькими
        # условиями, но тут код теряет читабельность, если так сделать
        if predict < number and predict > min:
            min = predict # Обновление нижней границы
        elif predict > number and predict < max:
            max = predict # Обновление верхней границы
        
        predict = np.random.randint(min, max) # Случайное число в новых границах
        
    return count



def score_game(predict_func) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_func(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


score_game(game_core_v3)