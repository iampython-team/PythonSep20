

from types import new_class


country_names=['India','SouthKorea','SouthAfrica','Peru','USA']
# insert functions -insert, append, extend 
country_names.insert(0,'Poland')
country_names.insert(0,True)
country_names.insert(0,False)
print(country_names)

country_names.append('Srilanka')
print(country_names)

country_names.extend(['China',1234])  # c h i n a 
print(country_names)

# delete functions  - pop, clear,remove 

country_names.pop()#IndexError: pop index out of range
print(country_names) #by default last item will be  deleted 

# list - stack - LIFO - 
# queue - FIFO 


country_names.remove('China')  # delete an item 
print(country_names) 


country_names.clear() # empty 
print(country_names) 

del country_names # __del__
#print(country_names)  NameError: name 'country_names' is not defined


# utility functions  - index,count,find
colors=['red','blue','red','white','orange','yellow','white','black']

print(colors.index('white',4,7) )

# start index 
# stop index  

print(colors.count('white'))
for each_color in colors:
    print('Color ',each_color,colors.count(each_color))
    
# find is available in the string ... not in the list 

new_colors=colors.copy()
print(new_colors)
new_colors_2=colors
print(new_colors_2)


# memory -- shallow copy and deep copy 

