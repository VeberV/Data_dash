import numpy as np
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    start = 0
    end = 101
    count = 1
    while True:
        predict = (start + end) // 2
        if number == predict:
            break
        count += 1
        if number > predict:
            start = predict
        elif number < predict:
            end = predict


    # Ваш код заканчивается здесь

    return count
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
# if __name__ == '__main__':
#     score_game(random_predict)