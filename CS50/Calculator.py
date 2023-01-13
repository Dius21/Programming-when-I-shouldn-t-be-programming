
class Calculator():
    n1=float(input("Enter a number:"))
    o=input("enter an operator (+,-,*,/,%,^)")
    n2=float(input("Enter a number:"))
    match o:
        case "+":
            print(n1+n2)
        case "-":
            print(n1-n2)
        case "*":
            print(n1*n2)
        case "/":
            print(n1/n2)
        case "%":
            print(n1%n2)
        case "^":
            print(n1**n2)
        case default:
            print("Operator not indentified.")
            
if __name__=="__main__":
    Calculator()
