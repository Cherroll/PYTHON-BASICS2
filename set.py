
'''
my_set ={1,2,3,4,5}
print(my_set)
my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)
'''
set1 ={1,2,3}
set2 ={3,4,5}

#union add sets and removes duplicates
union_set=set1.union(set2)
print(union_set)

#intersection  finds whats common between sets 
inter_set =set1.intersection(set2)
print(inter_set)

#Difference
dif_set=set1.difference(set2)
print(dif_set)
#Sets are useful when we want to work with collections of unique elements to perfom operations 
#like finding intersections , differences , unions.
#you can use sets to remove duplicate data 