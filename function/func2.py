def fun():
    print("this is my frist function")

def add(c:int,y:int,*args,**kwargs):
    print(args)
    print(kwargs)
    result:int=(c+y)
    return result
value=add(y=33,c=67,z=23)
print(value)