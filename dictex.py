d={'A':'apple','B':'ball','c':'apple','A':'ant'}

#an item = key not dup :value dup
# keys  - immutable 

print(d)



#print({[1,2]:'one'})
print({1+8j:'one'})


person={
    
    'name':'John',
    'age':45,
    'city':'NY',
    'languages':['English','French','Italian'],
    'address':{'Office','Res'},
    'USA Citizen':False,
    'Education':('B.commerce','MBA')
   
}


#print(person['umbrellla']) #KeyError: 'umbrellla'
print(person.get('languagesnnnnnnn')) # if key is not found there is no exception


print(person.keys())
print(person.values())
print(person.items())



for t in person.values():
    print(t,'----')
    
    
listx=[('name','Robert'),('age',56)]
print(dict(listx))

tuplex=(['name','Robert'],['age',56])
print(dict(tuplex))
