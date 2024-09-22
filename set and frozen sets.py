
#Creation of set variables


set2 = set('a')
set3 = {None}

print(f'{set1} and {type(set1)}')
print(f'{set2} and {type(set2)}')
print(f'{set3} and {type(set3)}')


#addition of elements to an existing set
set1 = {'a'}
print('set1  ',set1)
#adding the element 'b' to a set containing the element 'a'
set1.add('b')
#print the resultant set
print(set1)



#To check whether an element exists in a set

set1 = {'a','b','c'}

if 'a' in set1:
    print('Element "a" exists in set1 ')
else:
    print('Element "a" does not exists in set1')

if 'd' in set1:
    print('Element "d" exists in set1 ')
else:
    print('Element "d" does not exists in set1')

#Remove an existing element from a set

basket = {'apple','orange','kiwi'}

basket.remove('apple')

print(basket)

#set operations

fruit_basket1 = {'apple','banana'}
fruit_basket2 = {'orange','apple'}

print('union result',fruit_basket1.union(fruit_basket2))
print('intersection result',fruit_basket1.intersection(fruit_basket2))



#frozen sets
fs1 = frozenset(('a','b'))
print(fs1,type(fs1))



#Food for thought

list1 = [1,2,3,4,5,1,2,5]
set1 = set(list1)
list1 = list(set1)
print(list1)

