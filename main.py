def armstrong_numbers(start, end):
    armstrong_numbers_list = []

    for number in range(start, end + 1):
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
    start_range = 0
    end_range = 100000

    print(f"Armstrong numbers within the range of {start_range} to {end_range}:")
    print(armstrong_numbers(start_range, end_range))
