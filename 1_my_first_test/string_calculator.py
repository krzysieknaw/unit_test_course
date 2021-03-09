def string_calculator():
    add = input("enter the number ")
    if add == "":
        return 0  # todo isnumeric?
    else:
        numbers = [x for x in str(add)]
        result = 0
        for number in numbers:
            result += int(number)
        return result


def main():
    print(string_calculator())


main()
