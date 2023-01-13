

class decimalbinary():
    number=int(input("Enter a number:"))
    _=len(str(number))

    binary=0
    for i in range(0,_):
        binary+=(10**i)*((int((str(number))[i]))%2)
    print(binary)

if __name__=="__main__":
    decimalbinary()