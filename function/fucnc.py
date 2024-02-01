li=[22,23,1,7,33,100,378]
def get_even_list(a):
    even_list=[]
    for x in a:
        if x %2==0:
            even_list.append(x)

    return even_list

    
print(get_even_list(li))