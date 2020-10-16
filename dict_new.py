
bank_customer={
    'id':123,
    'accounts':('savings','current')
}

print(type(bank_customer))
print(bank_customer.keys())
print(bank_customer.values())

# {} - empty dict 
# keys cannot be duplicated but values can be duplicated 
# keys are immutable - str,int,float,complex, tuple ,boolean 


bank_customer={
    'id':123,
    'accounts':('savings','current'),
     True:1,
     #{1,2}:'onetwo'
}

print(bank_customer)

# retrieving a value based on the key 
print(bank_customer['accounts']) #KeyError: 'accounts1'
print(bank_customer.get('accounts1')) # None -- but no exception


dict2={
    1:'one', 'two':2,1:'four'
}

print(dict2)