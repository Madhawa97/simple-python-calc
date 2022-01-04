def ask1(op):
    n1 = int(input("Enter a number : "))
    print(f"\nAnswer for : {op} of {n1} = ", end=' ')

    return n1

def ask2(op):
    n1 = int(input("Enter first number : "))
    n2 = int(input("Enter second number : "))
    print(f"\nAnswer for : {n1} {op} {n2} = ", end=' ')

    return n1, n2

def pref():
    print("-"*41 + "\n" + "-"*10 + " Integer Calclulater " + "-"*10 + "\n")
    
    print("0)  Exit App\n1)  Addition\t2)  Subtraction\n3)  Multiply\t4)  Division\n5)  Factorial\t6)  Square Root\n7)  Squared\n")

    choice = int(input("Enter Choice : "))

    return choice

def answer(ans):
    #final = "\n" + "Answer is : " + str(ans) + "\n" + "-"*41 + "\n\n"
    final_ans = str(ans) + "\n" + "-"*41 + "\n\n"
    print(final_ans)

def saybye():
    print("\nBye...")


