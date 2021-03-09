def string_calculator():
    add = input("enter the numbers ")
    if add == "":
        return 0  # todo isnumeric?
    else:
        numbers = add.split(",")
        result = 0
        for number in numbers:
            result += int(number)
        return result


def main():
    print(string_calculator())


main()
