num1={1,2,3,4}
num2={3,4,5,6}

print(num1.symmetric_difference(num2)) #{1, 2, 5, 6}
print(num2.symmetric_difference(num1)) #{1, 2, 5, 6}


num2.symmetric_difference_update(num1)
print(num1)
print(num2)

print(max(num2))



fruits=(('orange','apple'),('berry','grapes'))
print(fruits)

fruits=((('orange','apple'))) 
print(fruits)
print(fruits[0])

fruits=[[['orange','apple'],]] 
print(fruits)
print(fruits[0])

# packing unpacking 



s={1,'one',9,6,'Two'}

#print(s[2]) #TypeError: 'set' object is not subscriptable