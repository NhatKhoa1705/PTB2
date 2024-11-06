import math

def firstDegree(a,b):
    if a==0 and b==0:
        return "Infinity!"
    elif a==0 and b!=0:
        return "No Solution!"
    else:
        x=-b/a
        return f"x={x}"
def quadraticEquation(a,b,c):
    if a==0:
        return firstDegree(b,c)
    else:
        delta=math.pow(b,2)-4*a*c
        if delta<0:
            return ("No Solution!")
        elif delta==0:
            return f"Double No. x1=x2={-b/(2*a)}"
        else:
            x1=(-b-math.sqrt(delta))/(2*a)
            x2 = (-b + math.sqrt(delta))/ (2*a)
            return f"x1={x1}; x2={x2}"