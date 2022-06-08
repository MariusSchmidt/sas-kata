def convert(arabic_number: int) -> str:
    if str(arabic_number).isnumeric():
        arabic_number = int(arabic_number)
    if arabic_number == 1:
        return "I"
    elif arabic_number == 5:
        return "V"
    return "X"


if __name__ == '__main__':
    user_input = input("Enter an arabic number: ")
    roman_number = convert(int(user_input))
    print(roman_number)
