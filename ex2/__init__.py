from ex2 import fetcher
import time

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """

    def wrapper(func):
        def inner(*args, **kwargs):
            start_all = time.time()
            for i in range(num):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                print(f'Время выполнения: {end - start}')
            end_all = time.time()
            print(f'Среднее время выполнения: {(end_all - start_all) / num}')
        return inner
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
