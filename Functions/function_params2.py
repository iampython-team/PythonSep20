# * and ** 


def studentNames(*names):
   for name in names:
       print('Mr.',name)
    
    
studentNames('Goutham','John','Dhoni')
# studentNames('John')
# studentNames('Dhoni')


def person(id,name,*languages,country='India'):
    country='IN'
    print("id ",id)
    print("name ",name)
    print("languages",languages)
    print("country ",country)
    
person(12345,'John','Hindi','English','Telugu','Kannada')
    
    
