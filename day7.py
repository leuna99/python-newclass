# tuples and sets


# tuples dupilacte data can be added order list
a = [1,2,3,4,5]
a[0] = 100
print(a)

a = (1,2,"hello",3,4,5)
print(type(a))
print(len(a))
print(a)


# unorder list data cannot be change iif place once both if wanted to change can type casting

a = {1,2,3,"test","nepal"}
print(type(a))
print(a)
b = list(a)

b.append("luna")

print(b)
a = set(b)
print(a)


# function
print("----------function-------")

def test():
    print("this is inside func")
    print("hello world")
test()
test()
test()
test()
test()


def check_even_num():
    n = 10
    if n%2==0:
        print("even")
    else:
        print("odd")
print(check_even_num())   




