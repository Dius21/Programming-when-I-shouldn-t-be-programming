import math


def inputfloat(msg):
    print( msg, end = "")
    try:
        number=float(input())
        return number
    except ValueError:
        print("Expected Input is a number")


def radiantodegrees():
    rad=inputfloat("Enter Angle in Radians: ")
    if rad!=None:
        deg = (rad*180)/math.pi
        print (f"Given Angle in Degrees is: {deg}")
    else:
        radiantodegrees()

if __name__=="__main__":
    radiantodegrees()