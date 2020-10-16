
#4types 
# default - params - arguments 
# required positional  - params 
# * - vargs - variable length args 
# ** - KWARGS - keyword length args 



def person(id,name,country='India'):
    print("id ",id)
    print("name ",name)
    print("country ",country)
    
    
person(12345,'Rahul','IN')



# 2 and 3 
# 3.7.3.8 3.9 
# 3.8 
def person(id,name,countryphonecode='+91',country='India'):
    print("id ",id)
    print("name ",name)
    print("countryphonecode",countryphonecode)
    print("country ",country)
    
    
person(12345,'Rahul','IN')
person("rahul",12345,'+91','IN')



def studentMarks(**sub):
    print(type(sub))
    
studentMarks(maths=78,science=87,english=97)




    
    
    