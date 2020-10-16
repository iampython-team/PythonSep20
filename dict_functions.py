students={
    
    's1':[75,67,88], # maths physics chemistry
    's2':[79,67,88], # maths physics chemistry
    's3':[75,79,80], # maths physics chemistry
    's4':[35,62,88], # maths physics chemistry [95,67,98]
    's5':[75,67,83], # maths physics chemistry
    's6':[65,37,48], # maths physics chemistry   

}

print("length of students dict",len(students))

pupils=students.copy()
print('----Pupils-----')
print(pupils)


print(students['s4']) # retirving the value of dict 
students['s4']=[95,67,98] # updating the dict 
print(students)


print(students.keys()) # only keys
print(students.values()) # only values
print(students.items()) #  items - keys and values


for sid,smarks in students.items():
    print(sid,"====",smarks)
    
    
students.pop('s5') # deleting the record/item based on key
print(students)


students.popitem() # by default - it deletes last key/value pair 
print(students)


students.clear()  # it makes dict as empty -- deletes all current items for dict 
print(students)


del students  # deleting an object from the memory 
#print(students) #NameError: name 'students' is not defined


# is there any max value of int in python? 
x=1234444444444444444444444444444444444444444444444444444444444444444444444444444444
print(x)




# {k:v} -operator 
# dict - function 

tv=[
    ('Samsung',{'UHD','LED'}),
    ('LG','LED'),
    ('Sony','CURVE'),
    
    ]  # tuple data(2) in list(n)
d3=dict(tv)
print(d3)
print(d3['LG'])

tv=(['Samsung','UHD'],['LG','LED']) # list data(2) in tuple(n)
d4=dict(tv)
print(d4)
print(d4['LG'])



tv=(('Samsung','UHD'),('LG','LED')) # tuple data(2) in tuple 
d5=dict(tv)
print(d5)