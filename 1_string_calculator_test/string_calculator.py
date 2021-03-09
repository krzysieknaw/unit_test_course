def string_calculator(user_input):
    if user_input == "":
        return 0  # todo isnumeric?
    else:
        numbers = user_input.split(",")
        result = 0
        for number in numbers:
            result += int(number)
        return result


# def main():
#     user_input = input("enter the numbers ")
#     print(string_calculator(user_input))
#
#
# main()
