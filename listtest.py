a = [10,20,10,10,30]
print(a)
for i in a:
    if a.count(i) > 1:
        a.remove(i)
    print(a, i)
 
print(a)