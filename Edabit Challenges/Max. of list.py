class Lmax():
    @classmethod
    def Lmax(list=[]):
        temp=list[0]
        for i in range(1,list.len()):
            if list[i]>temp:
                temp=list[i]
        return temp