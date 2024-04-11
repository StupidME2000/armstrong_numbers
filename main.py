def armstrong_numbers():
    armstrong_numbers_list = []

    for number in range(0, 100001):
        # Count number of digits
        number_str = str(number)
        number_digits = len(number_str)

        # Calculate sum of nth power of each digit
        digit_sum = sum(int(digit) ** number_digits for digit in number_str)

        # Check if the sum equals the original number
        if digit_sum == number:
            armstrong_numbers_list.append(number)

    return armstrong_numbers_list

if __name__ == "__main__":
    print("Armstrong numbers within the range of 0 to 100,000:")
    print(armstrong_numbers())
