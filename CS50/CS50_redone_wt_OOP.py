import os
import sort
import cat
import doublevision
import Extractnos
import Tinkeringwttkinter
import pythonprinciples1
import radiantodegrees
import XsandOs


class AdvancedIp():
    @classmethod
    def get_float(cls, str):
        n=input(str)
        try:
            n=float(n)
        except ValueError:
            print("Not a valid number, pls try again.")
            i+=1
            n=AdvancedIp.get_float(str)
        return float(n)
        
    @classmethod
    def get_int(cls, str):
        n=input(str)
        try:
            n=int(n)
        except ValueError:
            print("Not a valid number, pls try again.")
            n=AdvancedIp.get_float(str)
        return int(n)


class Calculator():
    @classmethod
    def ui(cls):
        n1=AdvancedIp.get_float("Enter a number: ")
        o=input("Enter an operator (+,-,*,/,%,**): ")
        n2=AdvancedIp.get_float("Enter another number: ")
        print("Result is ", end="")
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
            case "**":
                print(n1**n2)
            case default:
                print ("Unsupported Operator")

def main():
    app=AdvancedIp.get_int("Apps in Module-\n1. Caculator\n2. Sort\n3. The Start\n4. Cat\n5. Double Vision\n6. Extract nos.\n7. Tinkering With Tkinter\n8. Capital Indices\n9. Radian to Degrees\n10. Xs and Os\nWhat app do you want to run?: ")
    match app:
        case 1:
            Calculator.ui()
        case 2:
            sort.main()
        case 3:
            print("Hello World\n note this is not using OOP, because essense of original program would be lost if OOP was implemented")
        case 4:
            cat.Cat.main()
        case 5:
            doublevision.doublevision.main()
        case 6:
            Extractnos.Extractnos.main()
        case 7:
            Tinkeringwttkinter.main()
        case 8:
            pythonprinciples1.main()
        case 9:
            radiantodegrees.radiantodegrees()
        case 10:
            XsandOs.main()
        case default:
            print("I don't think you entered a valid selection 🫤")
    ask=input("press enter to exit")




if __name__=="__main__":
    main()

            