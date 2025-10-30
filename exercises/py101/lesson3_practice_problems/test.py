


def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    NUMBER_OF_NUMBER_IN_IP = 4
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != NUMBER_OF_NUMBER_IN_IP:
        return False
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

print(is_dot_separated_ip_address("255.255.255.0"))
print(is_dot_separated_ip_address("255.255.255.0.0"))
print(is_dot_separated_ip_address("256.255.255.0"))