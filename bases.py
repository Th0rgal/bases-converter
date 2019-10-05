def switch_base(input_base, input_number, output_base):
    number = 0
    for digit_index in range(len(input_number)):
        number += input_base ** digit_index * input_number[-digit_index - 1]

    output = []
    while number != 0:
        output.append(number % output_base)
        number = number // output_base

    return output[::-1]  # shortcut to reverse the list

representation_dictionnary = (
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
)
# 64 is the maximum base that can be represented using this method
def get_representation(input_number):
    # for digit in input_number:
    ouput_representation = ""
    for digit in input_number:
        ouput_representation += representation_dictionnary[digit]
    return ouput_representation

def to_digit_array(string_representation):
    digit_array = []
    for char in string_representation:
        digit_array.append(representation_dictionnary.index(char))
    return digit_array


input_representation = input("please enter a number in any base (e.g. 123 or A0):")
input_base = int(input("please enter this number base (e.g. 2, 10 or 16):"))
input_number = to_digit_array(input_representation)
output_base = int(
    input("please enter the base you want your number to be converted in:")
)
output_number = switch_base(input_base, input_number, output_base)

print(
    "{} in base {} is equals to {} in base {}".format(
        input_representation, input_base, get_representation(output_number), output_base
    )
)

