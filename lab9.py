from time import time


def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        count = args[0]
        print(f'Начало выполнения функции: {start_time}')
        print(f'Количество товара: {count}')
        return result
    return wrapper


@decorator
def cost(count):
    if count == 1:
        return 10.95
    return 10.95 + 2.95 * (count - 1)


if __name__ == "__main__":
    cost(3)
    cost(1)
