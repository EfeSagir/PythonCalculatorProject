import utilities

stack = []
turn_start = False

while True:

    if (stack == []):
        turn_start = False
        first_input_from_user = float(input())
        stack.append(first_input_from_user)
        operator = input()
        if isinstance(operator, float):
            stack.append(stack[-1] + "operator")

        if(operator == "="):
            print(stack[-1])

        second_input_from_user = float(input())

        match operator:
            case "+":
                 stack.append(utilities.summation(stack[-1],second_input_from_user))
            case "-":
                  stack.append(utilities.substraction(stack[-1],second_input_from_user))
            case "*":
                  stack.append(utilities.multiplication(stack[-1],second_input_from_user))
            case "/":
                if (second_input_from_user != 0):
                    stack.append(utilities.division(stack[-1],second_input_from_user))
                else:
                    print("Denominator Can't Be 0!")
                    third_input_from_user = float(input())
                    if (third_input_from_user != 0):
                        stack.append(utilities.division(stack[-1],third_input_from_user))

    user_input = input()

    if (user_input not in ("+","-","*","/","=")):
        stack.append(float(user_input))
        turn_start = False
        continue

    match user_input:
        case "+":
            if (turn_start):
                continue
            c = float(input())
            stack.append(utilities.summation(stack[-1], c))
        case "-":
            if (turn_start):
                continue
            d = float(input())
            stack.append(utilities.substraction(stack[-1], d))
        case "*":
            if (turn_start):
                continue
            e = float(input())
            stack.append(utilities.multiplication(stack[-1], e))
        case "/":
            if (turn_start):
                continue
            f = float(input())
            if (f != 0):
                stack.append(utilities.division(stack[-1], f))
            else:
                print("Denominator Can't Be 0!")
                fourth_input_from_user = float(input())
                if (fourth_input_from_user != 0):
                    stack.append(utilities.division(stack[-1],fourth_input_from_user))

        case "=":
            if (turn_start == True):
                continue
            print(stack[-1])
            turn_start = False