

num = int(input("\nEnter the number of elements: "))

newList = [];
for i in range(num):
    element = int(input(f'Enter the {i+1} number: '))
    newList.append(element)

print('\n Your entered list: ',newList)
 
    #Map function

square_list = list(map(lambda x: x*x, newList))
print('\n Square of list items: ', square_list)

    #Filter function 

def filter_func(x):
    return x % 2 == 0

filter_list = list(filter(filter_func, newList))
print('\n Filtered list: ',filter_list)

    # Reduce function
    
from functools import reduce

def multi_func(x,y):
    return x*y


multiply = reduce(multi_func,newList)
print('\n Your multiplication of list is: ', multiply)