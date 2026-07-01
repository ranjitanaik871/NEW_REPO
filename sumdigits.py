try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")
else:
    sum_digits = 0
    for digit in str(abs(n)):
        sum_digits += int(digit)
    print("Sum of digits:", sum_digits)