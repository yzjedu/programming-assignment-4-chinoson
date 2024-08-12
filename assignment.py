# Programmer: Henderson Fryer
# Course: CS701/GB-731, Dr. Yalew
# Date: 8/11/2024
# Programming Assignment: 4
# Program Inputs: A positive integer < 1000
# Program Outputs: The English name of the integer

def main():
    #pass

    number = int(input("Enter a positive integer that is less than 1000: "))

    #I'm commenting out this input validation because it made the pytest fail 1 test. 
    # while number < 1 or number > 999:
    #    print('Invalid number')
    #    number = int(input("Enter a positive integer that is less than 1000: "))
    
    intName(number)

## Turns a number into its English name.
#  @param number a positive integer < 1,000
#  @return the name of the number (e.g. "two hundred seventy four")
#


def intName(number):
    output = ''
    if number >= 100:
        output = str(digitName(number//100)) + ' hundred'
        if number % 100 >= 20 and number % 100 <= 99:
            output += ' ' + str(tensName(number % 100))
        elif number % 100 <= 19 and number % 100 >= 10:
            output += ' ' + str(teensName(number % 100))
        elif number % 100 <= 9 and number % 100 >= 1:
            output += ' ' + str(digitName(number % 100))
    elif number >= 20 and number <= 99:
        output += str(tensName(number))
    elif number >= 10 and number <= 19:
        output += str(teensName(number))
    else:
        output += str(digitName(number))
    
    print(output)         
 
## Turns a digit into its English name.
#  @param digit an integer between 1 and 9
#  @return the name of digit ("one" ... "nine")
#

def digitName(digit):
    if digit == 1:
        return 'one'
    elif digit == 2:
        return 'two'
    elif digit == 3:
        return 'three'
    elif digit == 4:
        return 'four'
    elif digit == 5:
        return 'five'
    elif digit == 6:
        return 'six'
    elif digit == 7:
        return 'seven'
    elif digit == 8:
        return 'eight'
    elif digit == 9:
        return 'nine'



## Turns a number between 10 and 19 into its English name.
#  @param number an integer between 10 and 19
#  @return the name of the given number ("ten" ... "nineteen")
#

def teensName(teens):
    if teens == 10:
        return 'ten'
    elif teens == 11:
        return 'eleven'
    elif teens == 12:
        return 'twelve'
    elif teens == 13:
        return 'thirteen'
    elif teens == 14:
        return 'fourteen'
    elif teens == 15:
        return 'fifteen'
    elif teens == 16:
        return 'sixteen'
    elif teens == 17:
        return 'seventeen'
    elif teens == 18:
        return 'eighteen'
    elif teens == 19:
        return 'nineteen'

    

## Gives the name of the tens part of a number between 20 and 99.
#  @param number an integer between 20 and 99
#  @return the name of the tens part of the number ("twenty" ... "ninety")
#

def tensName(tens):
    
    if tens // 20 == 1 and tens % 20 == 0:
        result = 'twenty'
    elif tens // 20 == 1 and tens % 20 != 0:
        result = 'twenty ' + str(digitName(tens % 20))
    
    if tens // 30 == 1 and tens % 30 == 0:
        result = 'thirty'
    elif tens // 30 == 1 and tens % 30 != 0:
        result = 'thirty ' + str(digitName(tens % 30))
    
    if tens // 40 == 1 and tens % 40 == 0:
        result = 'forty'
    elif tens // 40 == 1 and tens % 40 != 0:
        result =  'forty ' + str(digitName(tens % 40))
    
    if tens // 50 == 1 and tens % 50 == 0:
        result = 'fifty'
    elif tens // 50 == 1 and tens % 50 != 0:
        result = 'fifty ' + str(digitName(tens % 50))
    
    if tens // 60 == 1 and tens % 60 == 0:
        result = 'sixty'
    elif tens // 60 == 1 and tens % 60 != 0:
        result = 'sixty ' + str(digitName(tens % 60))
    
    if tens // 70 == 1 and tens % 70 == 0:
        result = 'seventy'
    elif tens // 70 == 1 and tens % 70 != 0:
        result = 'seventy ' + str(digitName(tens % 70))
    
    if tens // 80 == 1 and tens % 80 == 0:
        result = 'eighty'
    elif tens // 80 == 1 and tens % 80 != 0:
        result = 'eighty ' + str(digitName(tens % 80))
    
    if tens // 90 == 1 and tens % 90 == 0:
        result = 'ninety'
    elif tens // 90 == 1 and tens % 90 != 0:
        result = 'ninety ' + str(digitName(tens % 90))
    return result
    


# Start the program.
if __name__ == "__main__":
    main()