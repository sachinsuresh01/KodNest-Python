#No arg+ No return value
def add():
    a,b=10,10
    c=a+b
    print(c)
add()

#No arg +Return Value
def add1():
    a,b=10,20
    c=a+b
    return c
add1()
#argumnets+no return value
def add2(a,b):
  print(a+b)
add2(10,20)
#multiple return value


def calc(a,b):
    return a+b, a-b
sum,diff=calc(100,200)

print(sum)
print(diff)
