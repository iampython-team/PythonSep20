# '',"",'''

name1="India"
name2='India'
name3=''' India ''' # oops - docString , ''' multi line comments

''' print(name1,name2,name3)
print(type(name1))
print(type(name2))
print(type(name3))
 '''
 
game='baseball'

# indexing - starts 0 and ends with n-1. n- length of the string 
print('Length of the substring',len(game[0]),"Total length of the string ",len(game))

# b- 0   -8 
# a -1   -7 
# s -2   -6
# e -3   -5 
# b -4   -4
# a -5   -3 
# l -6   -2 
# l -7   -1 

# []
print(game[7])  #IndexError: string index out of range
print(game[-1]) 
