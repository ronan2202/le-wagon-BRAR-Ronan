# Start with some pseudo-code!
#For each number between 1 and 100
#If the number n is divisible by 3
#Then write "fizz"
#If the number is divisible by 5
#Then wirte buzz
#If the number n is divisible by 3 and 5 
#Then write fizz_buzz
#Or else
#Write n

for n in range(1, 100 + 1):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
        