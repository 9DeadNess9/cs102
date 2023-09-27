import math
import typing as tp
def calc(num_1: float, num_2: float, command: str) -> tp.Union[float, str]:
    if command == "+":
        return num_1 + num_2
    if command == "-":
        return num_1 - num_2
    if command == "/":
        if num_2 == 0:
            return "Так нельзя делать"
        return num_1 / num_2
    if command == "*":
        return num_1 * num_2
    if command == "^":
        return num_1**num_2
    if command == "^2":
        return num_1**2
    if command == "sin":
        return math.sin(math.radians(num_1))
    if command == "cos":
        return math.cos(math.radians(num_1))
    if command == "tg":
        return math.tan(math.radians(num_1))
    if command == "ln":
        if num_1 <= 0:
            return "Так нельзя делать"
        return math.log(math.radians(num_1))
    if command == "log10":
        if num_1 <= 0:
            return "Так нельзя делать"
        return math.log10(math.radians(num_1))
    else:
        return f"Неизвестный оператор: {command!r}."


if __name__ == "__main__":
    while True:  # программа выполняется до ввода 0 вместо команды
        COMMAND = input("Введите оперцию > ")
        if COMMAND.isdigit() and int(COMMAND) == 0:
            break
        if COMMAND in ("^2", "sin", "cos", "tg", "ctg", "ln", "log10"):
            NUM_1 = float(input("Первое число > "))
            result = calc(NUM_1, 0, COMMAND)
        else:
            NUM_1 = float(input("Первое число > "))
            NUM_2 = float(input("Второе число > "))
            result = calc(NUM_1, NUM_2, COMMAND)
        print(result)
