a = 1  
def x():
    print("f():", a)  
def y():
    a = 2  
    print("g():", a)
def z():
    global a
    a = 3 
    print("h():", a)
print("global:", a)
x()
print("global:", a)
y()
print("global:", a)
z()
print("global:", a)
