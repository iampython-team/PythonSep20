x={
    1,2,3,4,
}

y={
    1,4,5,6,7
}


print(x.intersection(y))  # with function
print(x & y) # with operator 

print(x.union(y))
print(x | y)

print(x.difference(y))
print(x - y)

print(y.difference(x))
print(y-x)


#print(x+y)

# x.difference_update(y)
# print("after diff update",x)
# print("after diff update",y)
# y.difference_update(x)
# print("after diff update",x)
# print("after diff update",y)

# x.intersection_update(y)
# print("after inter update",x)
# print("after inter update",y)

print("===========")
print(x.difference(y))
print(y.difference(x))
print(x.symmetric_difference(y))
print(y.symmetric_difference(x))
# print(x) #  1,2,3,4,
# print(y) #1,4,5,6,7


y.symmetric_difference_update(x)
print(x) #  1,2,3,4,
print(y) #1,4,5,6,7


# update on set .... 

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
s={8,9,1,2,8,8,1,0,6}
print(s)
s.pop()
print(s)
s.discard(19) # no exception raised when item is not found 
print(s)

s.remove(8)#KeyError: 9 when item is not found 
print(s)

