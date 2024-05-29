logo = '''
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝'''
def add(a , b):
    return a + b

def subtract(a , b):
    return  a - b

def divide(a , b):
    return  a / b

def multiply(a , b):
    return  a * b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
print(logo)
num1 = float(input("What is the first number?\n"))
def repetition(num1):

    for key in operations:
        print(key)

    operation = input("Pick an operation from the line above:\n")
    num2 = float(input("What is the next number?\n"))
    function = operations[operation]
    result = round(function(num1 , num2),5)
    print(f"{num1} {operation} {num2} = {result}")
    decision = input("Do you wish to do another operation?Y or N ").lower()
    if decision == "y":
        repetition(result)
    else:
        print('''
░█▀▀█ █▀▀█ █▀▀█ █▀▀▄ █▀▀▄ █──█ █▀▀ 
░█─▄▄ █──█ █──█ █──█ █▀▀▄ █▄▄█ █▀▀ 
░█▄▄█ ▀▀▀▀ ▀▀▀▀ ▀▀▀─ ▀▀▀─ ▄▄▄█ ▀▀▀''')
repetition(num1)