def calc(num_1: float, num_2: float, command: str) -> tp.Union[float, str]:
    if command == "+":
        return num_1 + num_2
    elif command == "-":
        return num_1 - num_2
    elif command == "/":
        if num_2 == 0:
            return "Ошикба! Деление на 0."
        else:
            return num_1 / num_2
    elif command == "*":
        return num_1 * num_2
    elif command == "Power":
        return num_1**num_2
    elif command == "Square":
        return num_1**2
    elif command == "sin":
        return math.sin(math.radians(num_1))
    elif command == "cos":
        return math.cos(math.radians(num_1))
    elif command == "tan":
        return math.tan(math.radians(num_1))
    elif command == "ln":
        if num_1 > 0:
            return math.log(num_1)
        else:
            return "Ошибка! Отрицательный логарифм."
    elif command == "log":
        if num_1 > 0:
            return math.log10(num_1)
        else:
            return "Ошибка! Отрицательный логарифм."
    else:
        return f"Неизвестный оператор: {command!r}."


if __name__ == "__main__":
    while True:  # программа выполняется до ввода 0 вместо команды
        COMMAND = input("Введите оперцию > ")
        if COMMAND.isdigit() and int(COMMAND) == 0:
            break
        if COMMAND == "help":
            print("Доступные операции: +, -, /, *, Power, Square, sin, cos, tan, ln, log")
        elif COMMAND == "complex mode":
            a = list(input().split())
            print("work in progress")
        else:
            try:
                if COMMAND in ["Square", "sin", "cos", "tan", "ln", "log"]:
                    NUM_1 = float(input("Число > "))
                    NUM_2 = 0.0
                else:
                    NUM_1 = float(input("Первое число > "))
                    NUM_2 = float(input("Второе число > "))
                print(calc(NUM_1, NUM_2, COMMAND))
            except:
                print("Ошибка при вводе данных!")
