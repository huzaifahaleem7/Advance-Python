a = [1,2,3,4,5]
even = [i for i in a if i%2==0]
print(even)

srq_root = [i*i for i in a]
print(srq_root)

b = set([1,2,3,2,3,4,5,6,7])
print(b)

even_set = {o for o in b if o %2 == 0}
print(even_set)


countires = {"Pakistan", "India", "Usa"}
cities = {"Islambad", "Dehli", "Washington"}
z = zip(countires, cities)

for i in z:
    print(i)
    
d = {country:city for country, city in zip(countires, cities)}
print(d)