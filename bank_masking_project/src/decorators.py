import datetime


def log(filename=None):
    """Функция-декоратор, логирующая результат и время выполнения функций"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                if filename:
                    with open(filename, "a") as file:
                        result = func(*args, **kwargs)
                        file.write(f"{str(datetime.datetime.now())} {func.__name__} started\n")

                        file.write(f"{str(datetime.datetime.now())} {func.__name__} finished\n")
                        file.write(f"{func.__name__} ok\n")
                    return result

                else:
                    result = func(*args, **kwargs)
                    print(f"{str(datetime.datetime.now())} {func.__name__} started\n")

                    print(f"{str(datetime.datetime.now())} {func.__name__} finished\n")
                    print(f"{func.__name__} ok\n")
                return result

            except Exception as e:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args} {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {e}. Inputs: {args} {kwargs}\n")
                raise
        return wrapper
    return decorator


@log(filename="mylog.txt")
def slog(a, b):
    return a + b


print(slog(5, 4))
