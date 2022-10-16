n = [10,20,[10,20,30],[40,50,60],[70,80,90]]
print(n)
print("Elements by row wise:")
for r in n:
    print(r)
    if type(r)==list:
        print("Elements By Matrix Style:")
        for i in range(len(n)):
            for j in range(len(n[i])):
                print(n[i][j],end=' ')
            print()
    print("Invalid Matrix")