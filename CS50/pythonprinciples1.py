def capital_indexes(og=str()):
    list=[]
    for i in range(0,len(og)):
        if ord(og[i]) in range(41,60):
            list.append(i)
    return list


def main():
    print(capital_indexes(input("What's the sentence? ")))


if __name__=="__main__":
    main()