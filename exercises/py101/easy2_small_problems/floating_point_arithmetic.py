

def calculate(num1, num2, operator):
    match operator:
        case "+": return num1 + num2
        case "-": return num1 - num2
        case "*": return num1 * num2
        case "/": return num1 / num2
        case "//": return num1 // num2
        case "%": return num1 % num2
        case "**": return num1 ** num2


num1 = float(input("==> Enter the first number:"))
num2 = float(input("==> Enter the second number:"))

for operator in ["+", "-", "*", "/", "//", "%", "**"]:
    operation = f"{num1} {operator} {num2}"
    result = calculate(num1, num2, operator)
    print(f"==> {operation} = {result:.1f}")
