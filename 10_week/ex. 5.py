import multiprocessing


def worker():
    LIST.append('item')


LIST = []


if __name__ == "__main__":
    processes = [multiprocessing.Process(target=worker()) for _ in range(5)]  # в исходном коде не хватает круглых
    # скобок после target=worker (т.к. worker() - это функция, а у функции есть аргументы, которые перечисляются в
    #  круглых скобках; если же у функции нет аргументов, пишутся просто пустые круглые скобки  worker() ).
    # В измененном мной коде они добавлены.
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(LIST)
