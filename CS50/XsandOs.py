def XsandOs(og):
    count1=0
    count2=0
    for i in range(0,len(og)):
        if og[i]=="X" or og[i]=="x":
            count1+=1
        if og[i]=="O" or og[i]=="o":
            count2+=1
    if count1==count2:
        return True
    else:
        return False


def main():
    _=XsandOs(input("Enter a string:"))
    if _==True:
        print("Xs = Os")
    else:
        print("Xs not equal to Os")

if __name__=="__main__":
    main()