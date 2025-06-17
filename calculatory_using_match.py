def calculator(inp_1, inp_2):
    op = input("Select one from +,-,*,/ : ")

    match op:
        case '+':
            return(inp_1 + inp_2)

        case '-':
            return(inp_1 - inp_2)
        case '*':
            return(inp_1 * inp_2)
        case '/':
            if inp_2 == 0:
                return("You cannot divide a number by 0.")
            else:
                return(inp_1 // inp_2)
        case '_':
            return("Invalid Input")


num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
print(calculator(num1, num2))