
def calculation ():
    first_number= int(input("enter your number: "))
    operator= input("what operator are you using(+,-,*,/): ")
    second_number = int(input("enter your second number: "))

    if operator == '+':
        output= first_number + second_number
        print(output)
    elif operator == '-':
        output= first_number - second_number
        print(output)
    elif operator == '*':
        output= first_number * second_number
        print(output)
    elif operator == '/':
        output= first_number / second_number
        print(output)
    else:
        print("your operator is invalid")
        return
    
    print(f"the answer is: {output}")
    return
    

calculation()
