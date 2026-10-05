def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    return "Zero"

number = float(input("Enter a number: "))
print("Result:", check_number(number))
