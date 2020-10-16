t=()
print(t)
print(type(t))

a,b,c=1,2,3
print(a)
print(b)
print(c)

a='raja',1,True,45.678,[1,2,34]
print(a)
print(type(a))

listx=[(1,2,3),'Raja',45,'NY,56.7']
print(listx)


colors=('white','red','blue','green','red','white','black')
#colors[2]='mattblue' #TypeError: 'tuple' object does not support item assignment
print(colors)

# tuple - immutable object 

print(colors.count('white'))
print(colors.index('white',2,len(colors)))

# len , min, max 

tuplenested=(
    [1,2,3], # 0
    'games', # 1 
    (12,13,14
     ,(99,98,96)) # 2
)

print(tuplenested[2][3][1])