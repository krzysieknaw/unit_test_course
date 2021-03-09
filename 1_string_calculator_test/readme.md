## To do:
1. convert string calculator pseudocode into python 
    ```
    class StringCalculator
    {
        int add(string input) 
        {
            if (isEmpty(input)) 
            {
                return 0;
            } 
            else 
            {
                numbers = split(intput, ",")
                result = 0;
    
                for (number in numbers) 
                {
                    result += getIntFrom(number);
                }
                return result;
            }
        }
    }
    ```

    ready  <a href='https://raw.githubusercontent.com/krzysieknaw/unit_test_course/main/1_string_calculator_test/string_calculator.py'> string_calculator.py  </a> file


2. Create some basic tests:  
<a href='https://github.com/krzysieknaw/unit_test_course/1_string_calculator_test/string_calculator_test.py'> string_calculator_test.py  </a>
### My comments:
1. Had to extract user input outside the function - check 'mock'
2. Two of five tests created to fail 
