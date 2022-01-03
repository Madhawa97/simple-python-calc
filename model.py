import arithmetic
import view

def selection(c):
    if c==1:
        num1, num2 = view.ask2()
        return arithmetic.add(num1, num2)
    elif c==2:
        num1, num2 = view.ask2()
        return arithmetic.sub(num1, num2)
    elif c==3:
        num1, num2 = view.ask2()
        return arithmetic.mul(num1, num2)
    elif c==4:
        num1, num2 = view.ask2()
        return arithmetic.div(num1, num2)
    elif c==5:
        num1 = view.ask1()
        return arithmetic.fac(num1)
    elif c==6:
        num1 = view.ask1()
        return arithmetic.root(num1)
    elif c==7:
        num1 = view.ask1()
        return arithmetic.squared(num1)