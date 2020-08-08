def string_to_integer(input_string):
    if len(input_string) == 0:
        return 0

    small_string = input_string[1:]
    small_ans = string_to_integer(small_string)
    small_cal = (input_string[0] - '0') * (10 ** (len(input_string) -1))
    return small_cal + small_ans

input_string = '1234'
output = string_to_integer(input_string)
print(output)
