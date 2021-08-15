

l = (1,2,3,4,5,6,7,8,9,10,11,12)

b = 0
many = 10
e = many
ll = len(l)

while b < ll:

    if b > ll-many:
        for ee in range(b,b+(ll-b)):
            print(l[ee],b)
    else:
        for ee in range(b,e):
            print(l[ee],b)
    
    b = e
    e = e + many