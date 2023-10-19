import random
def even_numbers():
    print("\t\t\t\t\tEven numbers")
    try:
        n = int(input())
        a = 1
        while a<n:
            a += 1
            if a%2==0:
                print(a)

    except:
        print()

#--------------------------------------

def  Factorial():
    print("\t\t\t\t\tFactorial")
    try:
        n = int(input())
        a = 1
        res = 1
        while a<=n:
            res *= a
            a += 1
            print(res)

    except:
        print("Error!")

#---------------------------------------

def Number_search():
    print("\t\t\t\t\tNumber Search")
    try:
        while True:
            num = int(input())

            if num == 42:
                break

    except:
        print("Error!")


#---------------------------------------

def Character_Counting():
    print("\t\t\t\t\tCharacter Counting")
    str = input("insert string:")
    print(str.count("a"))


#---------------------------------------


def Sum_of_digits_of_a_number():
    print("\t\t\t\t\tCharacter Counting")
    number = input()
    sum = 0

    for digit in number:
        if digit.isdigit():
            sum += int(digit)


    print(sum)

#---------------------------------------

def Fibonacci_numbers():
    print("\t\t\t\t\tFibonacci_numbers")
    n = int(input())
    a=0
    b=1
    sum = 0
    while sum<n:
        print(a)
        a, b = b, a + b
        sum+=1
    print()

#---------------------------------------

def Reverse_a_string():
    print("\t\t\t\t\tReverse_a_string")

    str = input()
    print(''.join(list(reversed(str))))



def Skip_even_ones():
    print("\t\t\t\t\tSkip_even_ones")

    odd_sum = 0

    while True:
        number = input()

        if number.lower() == "stop":
            break

        try:
            number = int(number)
            if number % 2 == 0:
                continue
            else:
                odd_sum += number
        except ValueError:
            print()

    print(odd_sum)


#---------------------------------------

def Guess_the_number():
    print("\t\t\t\t\tGuess_the_number")
    r = random.randint(0, 100)

    print(r)
    while True:
        guess = input()
        if guess.lower() == "stop":
            print("Correct!")
            break
        try:
            guess = int(guess)
            if guess == r:
                print("Correct")
                break
            if guess<r:
                print("Too small")
            elif guess > r:
                print("Too big")
            elif guess == "stop":
                break

        except:
            print("Error!")



#---------------------------------------


def Palindrome():
    print("\t\t\t\t\tPalindrome")
    str = input()
    str2 =""
    str2 = ''.join(reversed(str))
    if str==str2:
        print("Palindrome")
    else:
        print("not Polindrome")



#---------------------------------------


def Number_to_the_power():
    print("\t\t\t\t\tNumber_to_the_power")
    x = int(input())
    y = int(input())
    res = 1
    while y > 0:
        res *= x
        y -= 1
    print(res)

#---------------------------------------

def Counting_Prime_Numbers():
    print("\t\t\t\t\tCounting_Prime_Numbers")
    N = int(input("Введите положительное целое число N: "))
    num = 2
    while num <= N:
        is_prime = True
        divisor = 2

        while divisor * divisor <= num:
            if num % divisor == 0:
                is_prime = False
                break
            divisor += 1

        if is_prime:
            print(num, end=" ")

        num += 1

    print()


def Reverse_number():
    print("\t\t\t\t\tReverse_number")

    number = input()
    sum = 0

    rev = number[::-1]
    print(rev)



def Check_for_primality():
    print("\t\t\t\t\tCheck_for_primality")
    num = int(input())
    print(int(str(num)[::-1]))
    is_prime = True

    if num < 2:
        is_prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

    if is_prime:
        print("простое число.")
    else:
        print("не является простым числом.")


def caesar_cipher(text, shift):


    encrypted_text = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
        else:
            encrypted_text += char

    return encrypted_text

user_input = input("строка:")
shift = int(input("число:"))

encrypted_text = caesar_cipher(user_input, shift)
print("Зашифрованная строка:", encrypted_text)




even_numbers()
Factorial()
Number_search()
Character_Counting()
Sum_of_digits_of_a_number()
Fibonacci_numbers()
Reverse_a_string()
Skip_even_ones()
Guess_the_number()
Palindrome()
Number_to_the_power()
Counting_Prime_Numbers()
Reverse_number()
Check_for_primality()
caesar_cipher()