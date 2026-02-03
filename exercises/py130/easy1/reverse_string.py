# Use a generator expression to yield each character of a string in reverse order.
string = 'hello'

reversed_string = (string[i] for i in range(len(string) - 1, -1, -1))

for char in reversed_string:
    print(char)