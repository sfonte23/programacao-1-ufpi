def func():
    global x
    x=1 #global
    print(x)
 
x = 42 #v. global
func()
print(x)

