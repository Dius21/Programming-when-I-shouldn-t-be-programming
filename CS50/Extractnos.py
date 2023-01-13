class Extractnos():
    @classmethod
    def main(cls):
        og=input("Enter a string:")

        nos=[]
        temp=0
        for i in range(0,len(og)):
            if og[i] in ['0','1','2','3','4','5','6','7','8','9']:
                temp=int(og[i])+temp*(10)
            else:
                if temp!=0:
                    nos.append(temp)
                    temp=0

        print("String Contains the following numbers in order of occurence:",nos)


if __name__=="__main__":
    Extractnos()