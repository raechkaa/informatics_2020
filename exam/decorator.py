def decorator_maker():
    def decorator(func):  # внутри декоратора декоратор определяет функцию-обертку, которая будет обернута
        # вокруг декорируемой функции func, чтобы исполнять произвольный код до и после нее
        def wrapped():
            print("Depricated")  # Обертка вокруг декорируемой функции
            return func()  # Сама функция
        return wrapped  # Возвращаем обернутую функцию
    return decorator


@decorator_maker()
def decorated_function():
    print("Декорируемая функция.")


decorated_function()
