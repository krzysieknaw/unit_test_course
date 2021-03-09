# import unittest
#
#
# clMyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()

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


print(string_calculator())


# class StringCalculator
# {
#     int add(string input)
#     {
#         if (isEmpty(input))
#         {
#             return 0;
#         }
#         else
#         {
#             numbers = split(intput, ",")
#             result = 0;
#
#             for (number in numbers)
#             {
#                 result += getIntFrom(number);
#             }
#             return result;
#         }
#     }
# }
