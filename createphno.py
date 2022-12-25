def create_phone_number(n):
    a1=''.join(str(e) for e in n)
    return(f'"({a1[:3]}) {a1[3:6]}-{a1[6:]}"')

num=[1,2,3,4,5,6,7,8,9,0]
print(create_phone_number(num))
