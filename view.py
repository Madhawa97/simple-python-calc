def ask1():
    n1 = int(input("Enter a number : "))
    return n1

def ask2():
    n1 = int(input("Enter first number : "))
    n2 = int(input("Enter second number : "))
    return n1, n2

def pref():
    print("-"*41 + "\n" + "-"*10 + " Integer Calclulater " + "-"*10 + "\n")
    
    print("0)  Exit App\n1)  Addition\t2)  Subtraction\n3)  Multiply\t4)  Division\n5)  Factorial\t6)  Square Root\n7)  Squared\n")

    choice = int(input("Enter Choice : "))

    return choice

def answer(ans):
    final = "\n" + "Answer is : " + str(ans) + "\n" + "-"*41 + "\n\n"
    print(final)

def saybye():
    print("\nBye...")


