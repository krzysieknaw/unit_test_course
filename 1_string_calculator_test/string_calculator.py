def string_calculator(user_input):
    if user_input == "":
        return 0
    else:
        numbers = user_input.split(",")
        result = 0
        for number in numbers:
            try:
                result += int(number)
            except:
                pass
        return result


# def main():
#     user_input = input("enter the numbers ")
#     print(string_calculator(user_input))
#
#
# main()
