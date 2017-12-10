#Program to find value of acceleration(a) in the formula v=u+at
def function(v,u,t):
    a = ((v - u) / t)
    return a

v = float(input("Enter final velocity: "))
u = float(input("Enter initial velocity: "))
t = float(input("Enter time period: "))

acc = function(v,u,t)

print("{0} m/s^2 is the required acceleration".format(acc))