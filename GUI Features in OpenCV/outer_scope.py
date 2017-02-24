#test outer scope
n = 1
def f():
    #global n
    n = 2
    print(n)

f()
print(n)
