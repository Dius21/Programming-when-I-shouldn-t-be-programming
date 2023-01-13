import random


class Cat():
    @classmethod
    def getnumber(cls,msg):
        n=input(msg)
        try:
            n=int(n)
        except ValueError:
            print("That's not an Integer: ")
            n=Cat.getnumber()
        return n
    
    @classmethod
    def meow(cls,n):
        for i in range(0,n):
            print("meow",end=(round(random.randint(0,1))*"\n"))
    
    @classmethod
    def main(cls):
        n=Cat.getnumber("Enter no. of meows: ")
        Cat.meow(n)

if __name__=="__main__":
    Cat.main()

    
    
