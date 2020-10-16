# swiggy -- 
places=['MGRoad','BrigadeRoad','ABC','CDF']
print("======list=====")
for driver_place in places: 
    print(driver_place)
    
places=('MGRoad','BrigadeRoad','ABC','CDF')
print("======tuple=====")
for driver_place in places: 
    print(driver_place)
    
    
places={'MGRoad','BrigadeRoad','ABC','CDF','MGRoad'}
print("======set=====")
for driver_place in places: 
    print(driver_place)

print("======range=====")
for number in range(19):
    print(number,end=' ')
    
    
print("======String=====")

for char in "python":
    print(char,end=' ')
print("")


print("======Dict=====")

for k,v in {'one':1,"two":2}.items():
    print(k,"---------",v)
    
    

    
    



