
#stringtolist
def stringtolist(slist):
    nlist=[]
    for i in slist:
        nlist.append(int(i))
    return nlist


#main
def main():
    _=input("Enter List (seperated with ' ' only):").strip()
    list=stringtolist(_.split())
    sorttype=input("\nChoose sorting algorithm:\n1.Bubble Sort\n2.Quick Sort\n3.Merge Sort\nChoice: ")
    order=input("\nChoose Order:\n(asc):ascending\n(dsc):decending\n(n):none,I'm just a troll\nChoice: ")
    match sorttype:
        case "1":
            list=bubblesort(list,order)
        case default:
            print("Unimplemented")
            list.insert(0,"List Returned with no change")
    print("Result is: " , list)


#importablefunction
def sort(list,type,order):
    match type:
        case 1:
            list=bubblesort(list,order)
    return list


#bubblesort
def bubblesort(nlist,type):
    if type!="n":
        for i in range(0,len(nlist)):
            for j in range(0,len(nlist)-1):
                if nlist[j]>nlist[j+1] and type=="asc":
                    nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
                else:
                    if nlist[j]<nlist[j+1] and type=="dsc":
                        nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
    return nlist


if __name__=="__main__":
    main()

if __name__=="sort":
    ...